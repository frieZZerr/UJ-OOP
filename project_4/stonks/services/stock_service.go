package services

import (
	"os"
    "errors"
    "fmt"
    "stonks/models"
	"stonks/proxy"

    "gorm.io/gorm"
)

type StockService struct {
    stockProxy *proxy.StockDataProxy
}

func NewStockService() *StockService {
    return &StockService{
        stockProxy: proxy.NewStockDataProxy(os.Getenv("API_TOKEN")),
    }
}

func (s *StockService) GetStockInfo(symbol string) (*models.Stock, error) {
    var stock models.Stock
    result := models.DB.Where("symbol = ?", symbol).First(&stock)

    if result.Error != nil {
        if errors.Is(result.Error, gorm.ErrRecordNotFound) {
            newStock := models.Stock{
                Symbol:      symbol,
                CompanyName: "Unknown",
                ExchangeID:  2,
            }

            err := s.stockProxy.UpdateStockData(&newStock)
            if err != nil {
                return nil, fmt.Errorf("Couldn't download data from API: %w", err)
            }

            if err := models.DB.Create(&newStock).Error; err != nil {
                return nil, fmt.Errorf("Couldn't save new stock to database: %w", err)
            }

            return &newStock, nil
        }

        return nil, fmt.Errorf("Error while downloading stock data: %w", result.Error)
    }

    err := s.stockProxy.UpdateStockData(&stock)
    if err != nil {
        return nil, err
    }

    if err := models.DB.Save(&stock).Error; err != nil {
        return nil, fmt.Errorf("Error while saving stock data: %w", err)
    }

    return &stock, nil
}

func (s *StockService) ListExchanges() ([]models.StockExchange, error) {
    var exchanges []models.StockExchange
    if err := models.DB.Find(&exchanges).Error; err != nil {
        return nil, err
    }
    return exchanges, nil
}

func (s *StockService) GetExchange(code string) (*models.StockExchange, error) {
    var exchange models.StockExchange
    if err := models.DB.Where("code = ?", code).First(&exchange).Error; err != nil {
        return nil, err
    }
    return &exchange, nil
}

func (s *StockService) ListStocksByExchange(exchangeID uint) ([]models.Stock, error) {
    var stocks []models.Stock
    if err := models.DB.Where("exchange_id = ?", exchangeID).Find(&stocks).Error; err != nil {
        return nil, err
    }
    return stocks, nil
}
