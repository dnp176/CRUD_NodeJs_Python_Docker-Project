# ✅ Use lightweight Python image
FROM python:3.12-slim

# ✅ Set workdir
WORKDIR /app

# ✅ Copy files
COPY . .

# ✅ Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn pymongo python-dotenv

# ✅ Expose port (optional)
EXPOSE 8000

# ✅ Command (use runtime ENV BACKEND_PORT)
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${BACKEND_PORT}"]
