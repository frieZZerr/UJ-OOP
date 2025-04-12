package controllers

import (
    "net/http"
    "stonks/services"
    "strconv"

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
    e.GET("/exchanges", c.ListExchanges)
    e.GET("/exchanges/:code", c.GetExchange)
    e.GET("/exchanges/:id/stocks", c.ListStocksByExchange)
}

func (c *StockController) GetStockInfo(ctx echo.Context) error {
    symbol := ctx.Param("symbol")

    stock, err := c.stockService.GetStockInfo(symbol)
    if err != nil {
        return ctx.JSON(http.StatusInternalServerError, map[string]string{
            "error": "Couldn't download stock data: " + err.Error(),
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
            "error": "Couldn't download stock data: " + err.Error(),
        })
    }

    return ctx.JSON(http.StatusOK, stock)
}

func (c *StockController) ListExchanges(ctx echo.Context) error {
    exchanges, err := c.stockService.ListExchanges()
    if err != nil {
        return ctx.JSON(http.StatusInternalServerError, map[string]string{
            "error": "Couldn't download stock exchange list: " + err.Error(),
        })
    }

    return ctx.JSON(http.StatusOK, exchanges)
}

func (c *StockController) GetExchange(ctx echo.Context) error {
    code := ctx.Param("code")

    exchange, err := c.stockService.GetExchange(code)
    if err != nil {
        return ctx.JSON(http.StatusInternalServerError, map[string]string{
            "error": "Couldn't download info about stock exchange: " + err.Error(),
        })
    }

    return ctx.JSON(http.StatusOK, exchange)
}

func (c *StockController) ListStocksByExchange(ctx echo.Context) error {
    idParam := ctx.Param("id")
    id, err := strconv.ParseUint(idParam, 10, 32)
    if err != nil {
        return ctx.JSON(http.StatusBadRequest, map[string]string{
            "error": "Invalid exchange id",
        })
    }

    stocks, err := c.stockService.ListStocksByExchange(uint(id))
    if err != nil {
        return ctx.JSON(http.StatusInternalServerError, map[string]string{
            "error": "Couldn't download stock list: " + err.Error(),
        })
    }

    return ctx.JSON(http.StatusOK, stocks)
}
