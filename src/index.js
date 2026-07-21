const express = require('express');
const axios = require('axios');
const _ = require('lodash');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date() });
});

app.post('/api/compute', (req, res) => {
  const { items } = req.body;
  if (!items || !Array.isArray(items)) {
    return res.status(400).json({ error: 'Items array required' });
  }

  // Sample matrix iteration
  let total = 0;
  for (let i = 0; i < items.length; i++) {
    for (let j = 0; j < items.length; j++) {
      total += (items[i] || 0) + (items[j] || 0);
    }
  }

  res.json({ total, count: items.length });
});

app.listen(PORT, () => {
  console.log(`Carbotrace demo Node app running on port ${PORT}`);
});
