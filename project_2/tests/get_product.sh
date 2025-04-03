#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <PRODUCT_ID>"
  exit 1
fi

PRODUCT_ID=$1

curl -X GET http://localhost:8000/products/$PRODUCT_ID
