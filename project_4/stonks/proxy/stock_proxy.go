package proxy

import (
    "fmt"
    "stonks/models"

    "github.com/go-resty/resty/v2"
)

type StockDataProvider interface {
    GetStockQuote(symbol string) (*StockQuote, error)
    GetCompanyProfile(symbol string) (*CompanyProfile, error)
}

type StockQuote struct {
    CurrentPrice    float64
    PreviousClose   float64
    Change          float64
    ChangePercent   float64
    HighPriceOfDay  float64
    LowPriceOfDay   float64
    OpenPriceOfDay  float64
}

type CompanyProfile struct {
    Name             string
    Country          string
    Exchange         string
    Industry         string
    MarketCap        float64
    ShareOutstanding float64
    Logo             string
    WebURL           string
}

type FinnhubAPIClient struct {
    httpClient *resty.Client
    apiKey     string
}

func NewFinnhubAPIClient(apiKey string) *FinnhubAPIClient {
    return &FinnhubAPIClient{
        httpClient: resty.New(),
        apiKey:     apiKey,
    }
}

func (c *FinnhubAPIClient) GetStockQuote(symbol string) (*StockQuote, error) {
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

    url := fmt.Sprintf("https://finnhub.io/api/v1/quote?symbol=%s&token=%s", symbol, c.apiKey)
    resp, err := c.httpClient.R().
        SetResult(&FinnhubQuoteResponse{}).
        Get(url)

    if err != nil {
        return nil, fmt.Errorf("Error while downloading stock data: %w", err)
    }

    quoteData := resp.Result().(*FinnhubQuoteResponse)

    return &StockQuote{
        CurrentPrice:    quoteData.CurrentPrice,
        PreviousClose:   quoteData.PreviousClose,
        Change:          quoteData.Change,
        ChangePercent:   quoteData.PercentChange,
        HighPriceOfDay:  quoteData.HighPriceOfDay,
        LowPriceOfDay:   quoteData.LowPriceOfDay,
        OpenPriceOfDay:  quoteData.OpenPriceOfDay,
    }, nil
}

func (c *FinnhubAPIClient) GetCompanyProfile(symbol string) (*CompanyProfile, error) {
    type FinnhubCompanyResponse struct {
        Name             string  `json:"name"`
        Country          string  `json:"country"`
        Exchange         string  `json:"exchange"`
        IPO              string  `json:"ipo"`
        MarketCap        float64 `json:"marketCapitalization"`
        ShareOutstanding float64 `json:"shareOutstanding"`
        Industry         string  `json:"finnhubIndustry"`
        Logo             string  `json:"logo"`
        WebURL           string  `json:"weburl"`
    }

    url := fmt.Sprintf("https://finnhub.io/api/v1/stock/profile2?symbol=%s&token=%s", symbol, c.apiKey)
    resp, err := c.httpClient.R().
        SetResult(&FinnhubCompanyResponse{}).
        Get(url)

    if err != nil {
        return nil, fmt.Errorf("Error while downloading company data: %w", err)
    }

    companyData := resp.Result().(*FinnhubCompanyResponse)

    return &CompanyProfile{
        Name:             companyData.Name,
        Country:          companyData.Country,
        Exchange:         companyData.Exchange,
        Industry:         companyData.Industry,
        MarketCap:        companyData.MarketCap,
        ShareOutstanding: companyData.ShareOutstanding,
        Logo:             companyData.Logo,
        WebURL:           companyData.WebURL,
    }, nil
}

type StockDataProxy struct {
    realProvider StockDataProvider
}

func NewStockDataProxy(apiKey string) *StockDataProxy {
    return &StockDataProxy{
        realProvider: NewFinnhubAPIClient(apiKey),
    }
}

func (p *StockDataProxy) GetStockQuote(symbol string) (*StockQuote, error) {
    return p.realProvider.GetStockQuote(symbol)
}

func (p *StockDataProxy) GetCompanyProfile(symbol string) (*CompanyProfile, error) {
    return p.realProvider.GetCompanyProfile(symbol)
}

func (p *StockDataProxy) UpdateStockData(stock *models.Stock) error {
    quote, err := p.GetStockQuote(stock.Symbol)
    if err != nil {
        return err
    }

    stock.CurrentPrice = quote.CurrentPrice
    stock.PreviousClose = quote.PreviousClose
    stock.Change = quote.Change
    stock.ChangePercent = quote.ChangePercent

    if stock.CompanyName == "Unknown" {
        profile, err := p.GetCompanyProfile(stock.Symbol)
        if err == nil && profile.Name != "" {
            stock.CompanyName = profile.Name
        }
    }

    return nil
}
