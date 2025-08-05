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

