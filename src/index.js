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

  // Optimised: single linear pass using lodash sumBy instead of O(n²) nested loop
  const sum = _.sumBy(items, (v) => v || 0);
  const total = sum * 2 * items.length; // equivalent to previous nested accumulation

  res.json({ total, count: items.length });
});

// New: lightweight stats endpoint
app.get('/api/stats', (req, res) => {
  res.json({
    uptime: process.uptime(),
    memoryMB: (process.memoryUsage().heapUsed / 1024 / 1024).toFixed(2),
    nodeVersion: process.version,
  });
});

app.listen(PORT, () => {
  console.log(`Carbotrace demo Node app running on port ${PORT}`);
});
