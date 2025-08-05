# ✅ Use lightweight Node.js image
FROM node:18-slim

# ✅ Set workdir
WORKDIR /app

# ✅ Copy package files first for better cache
COPY package*.json ./

# ✅ Install dependencies
RUN npm install --only=production

# ✅ Copy rest of the files
COPY . .

# ✅ Expose port (optional)
EXPOSE 3000

# ✅ Command with runtime ENV FRONTEND_PORT & API_BASE_URL
CMD ["sh", "-c", "node app.js"]
