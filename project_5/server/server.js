const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

const products = [
    {
      id: 1,
      name: "Dog Food - Beef 10kg",
      description: "Complete food for adult dogs with beef.",
      price: 129.99
    },
    {
      id: 2,
      name: "Cat Toy - Feather Wand",
      description: "Interactive cat toy that develops hunting instincts.",
      price: 24.50
    },
    {
      id: 3,
      name: "Aquarium 60L + Filter",
      description: "Modern 60-liter aquarium with a complete filtration system.",
      price: 349.00
    },
    {
      id: 4,
      name: "Automatic Dog Leash",
      description: "Durable automatic leash with a length of 5 meters.",
      price: 79.90
    },
    {
      id: 5,
      name: "Cat Scratching Post",
      description: "Stable cat scratching post with a height of 120 cm.",
      price: 199.00
    }
];

app.get('/products', (req, res) => {
  res.json(products);
});

app.post('/payment', (req, res) => {
  console.log('Payment received:', req.body);
  res.status(200).send('Payment processed');
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
