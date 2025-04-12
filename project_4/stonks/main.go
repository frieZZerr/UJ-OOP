package main

import (
    "log"
    "stonks/controllers"
    "stonks/models"
    "stonks/services"

    "github.com/labstack/echo/v4"
    "github.com/labstack/echo/v4/middleware"
)

func main() {
    _, err := models.InitDB("stonks.db")
    if err != nil {
        log.Fatalf("Couldn't initialize database: %v", err)
    }

    if err := models.SeedData(); err != nil {
        log.Fatalf("Couldn't load default data: %v", err)
    }

    e := echo.New()

    e.Use(middleware.Logger())
    e.Use(middleware.Recover())

    stockService := services.NewStockService()

    stockController := controllers.NewStockController(stockService)

    stockController.RegisterRoutes(e)

    log.Println("Server starting at port 8080...")
    e.Logger.Fatal(e.Start(":8080"))
}
