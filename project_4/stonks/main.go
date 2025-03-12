package main

import (
    "stonks/controllers"
    "stonks/services"

    "github.com/labstack/echo/v4"
    "github.com/labstack/echo/v4/middleware"
)

func main() {
    e := echo.New()

    e.Use(middleware.Logger())
    e.Use(middleware.Recover())

    stockService := services.NewStockService()

    stockController := controllers.NewStockController(stockService)

    stockController.RegisterRoutes(e)

    e.Logger.Fatal(e.Start(":8080"))
}
