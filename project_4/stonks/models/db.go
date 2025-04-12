package models

import (
    "log"

    "gorm.io/driver/sqlite"
    "gorm.io/gorm"
    "gorm.io/gorm/logger"
)

var DB *gorm.DB

func InitDB(dbPath string) (*gorm.DB, error) {
    var err error

    DB, err = gorm.Open(sqlite.Open(dbPath), &gorm.Config{
        Logger: logger.Default.LogMode(logger.Info),
    })

    if err != nil {
        return nil, err
    }

    err = DB.AutoMigrate(&StockExchange{}, &Stock{})
    if err != nil {
        return nil, err
    }

    return DB, nil
}

func SeedData() error {
    var count int64
    DB.Model(&StockExchange{}).Count(&count)

    if count == 0 {
        exchanges := []StockExchange{
            {
                Name:        "New York Stock Exchange",
                Code:        "NYSE",
                Country:     "USA",
                Description: "Największa giełda papierów wartościowych na świecie",
            },
            {
                Name:        "NASDAQ",
                Code:        "NASDAQ",
                Country:     "USA",
                Description: "Druga co do wielkości giełda papierów wartościowych na świecie",
            },
            {
                Name:        "Warsaw Stock Exchange",
                Code:        "WSE",
                Country:     "Polska",
                Description: "Giełda Papierów Wartościowych w Warszawie",
            },
        }
        
        if err := DB.Create(&exchanges).Error; err != nil {
            return err
        }

        stocks := []Stock{
            {
                Symbol:        "AAPL",
                CompanyName:   "Apple Inc.",
                ExchangeID:    2, // NASDAQ
                CurrentPrice:  0,
                PreviousClose: 0,
                Change:        0,
                ChangePercent: 0,
            },
            {
                Symbol:        "MSFT",
                CompanyName:   "Microsoft Corporation",
                ExchangeID:    2, // NASDAQ
                CurrentPrice:  0,
                PreviousClose: 0,
                Change:        0,
                ChangePercent: 0,
            },
            {
                Symbol:        "GOOG",
                CompanyName:   "Alphabet Inc.",
                ExchangeID:    2, // NASDAQ
                CurrentPrice:  0,
                PreviousClose: 0,
                Change:        0,
                ChangePercent: 0,
            },
            {
                Symbol:        "AMZN",
                CompanyName:   "Amazon.com Inc.",
                ExchangeID:    2, // NASDAQ
                CurrentPrice:  0,
                PreviousClose: 0,
                Change:        0,
                ChangePercent: 0,
            },
            {
                Symbol:        "PKO",
                CompanyName:   "PKO Bank Polski",
                ExchangeID:    3, // WSE
                CurrentPrice:  0,
                PreviousClose: 0,
                Change:        0,
                ChangePercent: 0,
            },
        }
        
        if err := DB.Create(&stocks).Error; err != nil {
            return err
        }
        
        log.Println("Initialized database with example data")
    }
    
    return nil
}
