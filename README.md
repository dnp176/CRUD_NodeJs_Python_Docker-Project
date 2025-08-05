# CRUD_NodeJs_Python_Docker-Project

CRUD Application with Docker

This project provides a simple **CRUD application** consisting of:

- **Frontend:** Node.js (React-based)
- **Backend:** Python (FastAPI)
- **Database:** MongoDB

All components are containerized using **Docker** and connected via a custom Docker network.

---

## ✅ Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine
- Basic knowledge of Docker commands
- (Optional) EC2 instance or any Linux server for deployment

---

## 🏗️ How to Run the Application

Follow the steps below to run the application using Docker.

---

### 1. Pull Images from Docker Hub

```bash
docker pull dnptestaccount/crud-nodejs-frontend
docker pull dnptestaccount/crud-python-backend
docker pull mongo:6
```

### Step 2: (Optional) Build Images Locally
If you have the source code and Dockerfiles, you can build the images using:
```bash
docker build -t crud-backend ./backend
docker build -t crud-frontend ./frontend
```

### Step 3: Create Docker Network
Create a custom network so containers can communicate with each other:
```bash
docker network create crud-net
```

### Step 4: Run MongoDB Container
Start MongoDB with required environment variables:

```bash
docker run -d \
  --name mongo \
  --network crud-net \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=secret \
  -e MONGO_INITDB_DATABASE=crudapp \
  -p 27017:27017 \
  mongo:6
```

### Step 5: Run Backend Container
Start the backend service and link it to MongoDB:
```bash
docker run -d \
  --name backend \
  --network crud-net \
  -e BACKEND_PORT=8000 \
  -e DB_HOST=mongo \
  -e DB_PORT=27017 \
  -e DB_NAME=crudapp \
  -e DB_USER=admin \
  -e DB_PASS=secret \
  -p 8000:8000 \
  dnptestaccount/crud-python-backend
```

### Step 6: Run Frontend Container
Replace <EC2_PUBLIC_IP> with your actual server IP or domain:
```bash
docker run -d \
  --name frontend \
  --network crud-net \
  -e FRONTEND_PORT=3000 \
  -e API_BASE_URL=http://<EC2_PUBLIC_IP>:8000 \
  -p 3000:3000 \
  dnptestaccount/crud-nodejs-frontend
```
### Access the Application
Frontend (React):
**http://<EC2_PUBLIC_IP>:3000**

Backend API (FastAPI):
**http://<EC2_PUBLIC_IP>:8000**

📌 Notes
- Update API_BASE_URL in the frontend container to point to the backend's public IP or domain.
- Ensure ports 3000, 8000, and 27017 are open in your firewall/security groups.
- For production, use environment variables and secrets securely.
