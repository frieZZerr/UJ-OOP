#!/bin/bash

curl -X POST http://localhost:8000/products/new \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Test Product",
           "price": 99.99,
           "description": "This is a test product"
         }'
