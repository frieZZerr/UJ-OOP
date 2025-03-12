// src/components/Payments.tsx
import React, { useState } from 'react';
import axios from 'axios';

const Payments: React.FC = () => {
  const [amount, setAmount] = useState('');

  const handlePayment = () => {
    axios.post('http://localhost:3000/payments', {
      amount: parseFloat(amount)
    })
    .then(response => {
      alert('Payment successfull!');
    })
    .catch(error => {
      console.error('Error sending payment:', error);
    });
  };

  return (
    <div>
      <h2>Payments</h2>
      <input
        type="number"
        value={amount}
        onChange={e => setAmount(e.target.value)}
        placeholder="Amount"
      />
      <button onClick={handlePayment}>Pay</button>
    </div>
  );
}

export default Payments;
