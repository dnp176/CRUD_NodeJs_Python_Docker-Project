require('dotenv').config();
const express = require('express');
const axios = require('axios');
const path = require('path');
const os = require('os');

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Set EJS as view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// ENV variables
const PORT = process.env.FRONTEND_PORT || 3000;
const API_BASE_URL = process.env.API_BASE_URL || 'http://localhost:8000';

// Routes
app.get('/', async (req, res) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/users`);
    const users = response.data;

    // Container name from ENV or hostname
    const containerName = process.env.HOSTNAME || os.hostname();

    // Get public IP
    const publicIP = await axios.get('https://api.ipify.org?format=json').then(resp => resp.data.ip);

    res.render('index', { users, containerName, publicIP });
  } catch (error) {
    res.render('index', { users: [], containerName: 'N/A', publicIP: 'N/A' });
  }
});

app.post('/add', async (req, res) => {
    try {
        await axios.post(`${API_BASE_URL}/users`, {
            first_name: req.body.first_name,
            last_name: req.body.last_name,
            email: req.body.email
        });
        res.redirect('/');
    } catch (err) {
        console.error(err.message);
        res.redirect('/');
    }
});

app.post('/delete/:id', async (req, res) => {
    try {
        await axios.delete(`${API_BASE_URL}/users/${req.params.id}`);
        res.redirect('/');
    } catch (err) {
        console.error(err.message);
        res.redirect('/');
    }
});

app.listen(PORT, () => {
    console.log(`✅ Frontend running on http://0.0.0.0:${PORT}`);
});
