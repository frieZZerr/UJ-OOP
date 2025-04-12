package models

import (
    "time"

    "gorm.io/gorm"
)

type StockExchange struct {
    ID          uint           `gorm:"primaryKey" json:"id"`
    Name        string         `gorm:"size:100;not null" json:"name"`
    Code        string         `gorm:"size:10;not null;uniqueIndex" json:"code"`
    Country     string         `gorm:"size:100" json:"country"`
    Description string         `json:"description"`
    CreatedAt   time.Time      `json:"created_at"`
    UpdatedAt   time.Time      `json:"updated_at"`
    DeletedAt   gorm.DeletedAt `gorm:"index" json:"-"`
    Stocks      []Stock        `gorm:"foreignKey:ExchangeID" json:"stocks,omitempty"`
}

type Stock struct {
    ID            uint           `gorm:"primaryKey" json:"id"`
    Symbol        string         `gorm:"size:20;not null" json:"symbol"`
    CompanyName   string         `gorm:"size:200;not null" json:"companyName"`
    ExchangeID    uint           `json:"exchangeId"`
    Exchange      *StockExchange `gorm:"foreignKey:ExchangeID" json:"-"`
    CurrentPrice  float64        `json:"price"`
    PreviousClose float64        `json:"previousClose"`
    Change        float64        `json:"change"`
    ChangePercent float64        `json:"changePercent"`
    CreatedAt     time.Time      `json:"created_at"`
    UpdatedAt     time.Time      `json:"updated_at"`
    DeletedAt     gorm.DeletedAt `gorm:"index" json:"-"`
}
