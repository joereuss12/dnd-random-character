const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const axios = require('axios'); // For making HTTP requests to the Python service

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.post('/generate', async (req, res) => {
    const data = req.body;

    try {
        // Example of calling a python service via HTTP
        const resp = await axios.post('http://localhost:5001/process', data);
        res.json(resp.data);
    } catch (error) {
        res.status(500).json({ error: 'Error processing character data '});
    }
});

app.listen(5000, () => {
    console.log('Node.js server running on port 5000');
});