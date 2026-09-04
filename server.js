require('dotenv').config();
const express = require('express');
const cookieParser = require('cookie-parser');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const rateLimit = require('express-rate-limit');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 8080;

app.use(express.json());
app.use(cookieParser());

// Rate limiting for the auth route
const authLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 10, // Limit each IP to 10 login requests per window
    message: { error: 'Too many login attempts, please try again later.' }
});

// Authentication endpoint
app.post('/api/auth', authLimiter, async (req, res) => {
    try {
        const { password } = req.body;
        if (!password) {
            return res.status(400).json({ error: 'Password is required' });
        }

        const hash = process.env.MICROSOFT_CASE_STUDY_PASSWORD_HASH;
        const match = await bcrypt.compare(password, hash);

        if (match) {
            const token = jwt.sign({ authenticated: true }, process.env.JWT_SECRET, { expiresIn: '8h' });
            
            res.cookie('auth_token', token, {
                httpOnly: true,
                secure: process.env.NODE_ENV === 'production',
                sameSite: 'lax',
                maxAge: 8 * 60 * 60 * 1000 // 8 hours
            });
            
            return res.json({ success: true });
        } else {
            // Generic error message
            return res.status(401).json({ error: 'Invalid password' });
        }
    } catch (err) {
        console.error(err);
        return res.status(500).json({ error: 'Internal server error' });
    }
});

// Logout endpoint
app.post('/api/logout', (req, res) => {
    res.clearCookie('auth_token');
    return res.json({ success: true });
});

// Middleware to verify auth token
const checkAuth = (req, res, next) => {
    const token = req.cookies.auth_token;
    if (!token) return res.status(401).send('Unauthorized');
    
    try {
        jwt.verify(token, process.env.JWT_SECRET);
        next();
    } catch (err) {
        res.status(401).send('Unauthorized');
    }
};

// Protected assets route
app.get('/protected-assets/:filename', checkAuth, (req, res) => {
    const filename = req.params.filename;
    // Prevent directory traversal
    const safePath = path.normalize(filename).replace(/^(\.\.(\/|\\|$))+/, '');
    const absolutePath = path.join(__dirname, 'protected-assets', safePath);
    
    if (fs.existsSync(absolutePath)) {
        res.sendFile(absolutePath);
    } else {
        res.status(404).send('Not Found');
    }
});

// Serve public static files (the SPA)
app.use(express.static(__dirname));

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});
