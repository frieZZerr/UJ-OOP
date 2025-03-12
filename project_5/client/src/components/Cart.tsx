// src/components/Cart.tsx
import React, { useContext } from 'react';
import { CartContext } from '../contexts/CartContext';

const Cart: React.FC = () => {
  const cartContext = useContext(CartContext);

  if (!cartContext) return <div>Loading cart...</div>;

  const { cart, clearCart } = cartContext;

  return (
    <div>
      <h2>Cart</h2>
      {cart.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          <ul>
            {cart.map((item, index) => (
              <li key={index}>{item.name} - {item.price} PLN</li>
            ))}
          </ul>
          <p><strong>Summary:</strong> {cart.reduce((sum, item) => sum + item.price, 0)} PLN</p>
          <button onClick={clearCart}>Clear cart</button>
        </>
      )}
    </div>
  );
}

export default Cart;
