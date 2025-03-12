package controllers

import (
    "net/http"
    "stonks/services"

    "github.com/labstack/echo/v4"
)

type StockController struct {
    stockService *services.StockService
}

func NewStockController(stockService *services.StockService) *StockController {
    return &StockController{
        stockService: stockService,
    }
}

func (c *StockController) RegisterRoutes(e *echo.Echo) {
    e.GET("/stock/:symbol", c.GetStockInfo)
    e.POST("/stock", c.GetStockInfoPost)
}

func (c *StockController) GetStockInfo(ctx echo.Context) error {
    symbol := ctx.Param("symbol")

    stock, err := c.stockService.GetStockInfo(symbol)
    if err != nil {
        return ctx.JSON(http.StatusInternalServerError, map[string]string{
            "error": "Couldn't download stock data",
        })
    }

    return ctx.JSON(http.StatusOK, stock)
}

func (c *StockController) GetStockInfoPost(ctx echo.Context) error {
    type Request struct {
        Symbol string `json:"symbol"`
    }

    req := new(Request)
    if err := ctx.Bind(req); err != nil {
        return ctx.JSON(http.StatusBadRequest, map[string]string{
            "error": "Invalid input data",
        })
    }

    stock, err := c.stockService.GetStockInfo(req.Symbol)
    if err != nil {
        return ctx.JSON(http.StatusInternalServerError, map[string]string{
            "error": "Couldn't download stock data",
        })
    }

    return ctx.JSON(http.StatusOK, stock)
}
