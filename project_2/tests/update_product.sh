#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <PRODUCT_ID>"
  exit 1
fi

PRODUCT_ID=$1

curl -X PUT http://localhost:8000/products/$PRODUCT_ID/edit \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Updated Product",
           "price": 149.99,
           "description": "Updated product description"
         }'
