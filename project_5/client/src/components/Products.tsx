// src/components/Products.tsx
import React, { useEffect, useState, useContext } from 'react';
import axios from 'axios';
import { CartContext } from '../contexts/CartContext';

interface Product {
  id: number;
  name: string;
  price: number;
}

const Products: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const cartContext = useContext(CartContext);

  useEffect(() => {
    axios.get('http://localhost:3000/products')
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.error('Error fetching products:', error);
      });
  }, []);

  const handleAddToCart = (product: Product) => {
    cartContext?.addToCart(product);
    alert(`${product.name} added to cart!`);
  };

  return (
    <div>
      <h2>Products</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            {product.name} - {product.price.toFixed(2)} PLN
            <button onClick={() => handleAddToCart(product)}>Add to cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Products;
