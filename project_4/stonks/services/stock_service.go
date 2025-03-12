package services

import (
    "os"
    "fmt"
    "github.com/go-resty/resty/v2"
)

type Stock struct {
    Symbol      string  `json:"symbol"`
    CompanyName string  `json:"companyName"`
    Price       float64 `json:"price"`
    Change      float64 `json:"change"`
    ChangePercent float64 `json:"changePercent"`
}

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

func (s *StockService) GetStockInfo(symbol string) (*Stock, error) {
    quoteUrl := fmt.Sprintf("https://finnhub.io/api/v1/quote?symbol=%s&token=%s", symbol, s.apiKey)
    quoteResp, err := s.httpClient.R().
        SetResult(&FinnhubQuoteResponse{}).
        Get(quoteUrl)

    if err != nil {
        return nil, fmt.Errorf("Error while dowloading stock data: %w", err)
    }

    quoteData := quoteResp.Result().(*FinnhubQuoteResponse)

    companyUrl := fmt.Sprintf("https://finnhub.io/api/v1/stock/profile2?symbol=%s&token=%s", symbol, s.apiKey)
    companyResp, err := s.httpClient.R().
        SetResult(&FinnhubCompanyResponse{}).
        Get(companyUrl)

    if err != nil {
        return nil, fmt.Errorf("Error while downloading company data: %w", err)
    }

    companyData := companyResp.Result().(*FinnhubCompanyResponse)

    stockData := &Stock{
        Symbol:      symbol,
        CompanyName: companyData.Name,
        Price:       quoteData.CurrentPrice,
        Change:      quoteData.Change,
        ChangePercent: quoteData.PercentChange,
    }

    return stockData, nil
}
