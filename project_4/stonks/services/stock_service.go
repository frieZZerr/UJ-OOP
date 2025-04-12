package services

import (
    "errors"
    "fmt"
    "stonks/models"

    "github.com/go-resty/resty/v2"
    "gorm.io/gorm"
)

type FinnhubQuoteResponse struct {
    CurrentPrice    float64 `json:"c"`
    Change          float64 `json:"d"`
    PercentChange   float64 `json:"dp"`
    HighPriceOfDay  float64 `json:"h"`
    LowPriceOfDay   float64 `json:"l"`
    OpenPriceOfDay  float64 `json:"o"`
    PreviousClose   float64 `json:"pc"`
    Timestamp       int64   `json:"t"`
}

type FinnhubCompanyResponse struct {
    Name          string `json:"name"`
    Country       string `json:"country"`
    Exchange      string `json:"exchange"`
    IPO           string `json:"ipo"`
    MarketCap     float64 `json:"marketCapitalization"`
    ShareOutstanding float64 `json:"shareOutstanding"`
    Industry      string `json:"finnhubIndustry"`
    Logo          string `json:"logo"`
    WebURL        string `json:"weburl"`
}

type StockService struct {
    httpClient *resty.Client
    apiKey     string
}

func NewStockService() *StockService {
    return &StockService{
        httpClient: resty.New(),
        apiKey:     os.Getenv("API_TOKEN"),
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

            companyUrl := fmt.Sprintf("https://finnhub.io/api/v1/stock/profile2?symbol=%s&token=%s", symbol, s.apiKey)
            companyResp, err := s.httpClient.R().
                SetResult(&FinnhubCompanyResponse{}).
                Get(companyUrl)

            if err == nil {
                companyData := companyResp.Result().(*FinnhubCompanyResponse)
                if companyData.Name != "" {
                    newStock.CompanyName = companyData.Name
                }
            }

            err = s.updateStockFromAPI(&newStock)
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

    err := s.updateStockFromAPI(&stock)
    if err != nil {
        return nil, err
    }

    return &stock, nil
}

func (s *StockService) updateStockFromAPI(stock *models.Stock) error {
    quoteUrl := fmt.Sprintf("https://finnhub.io/api/v1/quote?symbol=%s&token=%s", stock.Symbol, s.apiKey)
    quoteResp, err := s.httpClient.R().
        SetResult(&FinnhubQuoteResponse{}).
        Get(quoteUrl)

    if err != nil {
        return fmt.Errorf("Error while downloading company data: %w", err)
    }

    quoteData := quoteResp.Result().(*FinnhubQuoteResponse)

    stock.CurrentPrice = quoteData.CurrentPrice
    stock.PreviousClose = quoteData.PreviousClose
    stock.Change = quoteData.Change
    stock.ChangePercent = quoteData.PercentChange

    if err := models.DB.Save(stock).Error; err != nil {
        return fmt.Errorf("Error while saving stock data: %w", err)
    }

    return nil
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
