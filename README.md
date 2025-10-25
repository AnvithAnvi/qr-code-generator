# 🧠 QR Code Generator – Dockerized Application

## 📘 Overview
This project demonstrates how to containerize a Python-based QR Code Generator application using Docker.  
It follows best practices for secure, lightweight image building and cloud deployment via DockerHub.

---

## 🏗️ Project Setup

### 1️⃣ Clone or Download
```bash
git clone https://github.com/anvith123/qr-code-generator.git
cd qr-code-generator
```

### 2️⃣ Verify Files
Your project folder should contain:
```
main.py
requirements.txt
Dockerfile
README.md
```

---

## 🐳 Build and Run the Docker Container

### 🧱 Build the Image
```bash
docker build -t qr-code-generator-app .
```

### ▶️ Run the Container
```bash
docker run -d --name qr-generator qr-code-generator-app
```

### 🧾 View Logs
```bash
docker logs qr-generator
```

If you want to save QR codes locally:
```bash
docker run -d --name qr-generator   -v $(pwd)/qr_codes:/app/qr_codes   qr-code-generator-app --url https://www.njit.edu
```

---

## ☁️ Push to DockerHub

### 1️⃣ Login
```bash
docker login
```

### 2️⃣ Tag Image
```bash
docker tag qr-code-generator-app anvith123/qr-code-generator-app
```

### 3️⃣ Push Image
```bash
docker push anvith123/qr-code-generator-app
```

View your image here:  
🔗 [DockerHub Repository – anvith123](https://hub.docker.com/repositories/anvith123)

---

## 🧩 Security Best Practices
- Runs as a **non-root user** (`myuser`)
- Uses a **slim base image** (`python:3.12-slim-bullseye`)
- Installs dependencies with `--no-cache-dir`
- Uses limited write permissions for log and QR code directories

---

## 📷 Screenshots (for Submission)
1. **Docker build success**  
2. **Container running (docker ps)**  
3. **Container logs (docker logs qr-generator)**  
4. **DockerHub page showing your image**

---

## 🧠 Learning Reflection
Through this project, I learned how to package a Python application into a secure, portable Docker container.  
I resolved Apple Silicon (Rosetta) compatibility issues by switching to ARM64 base images and gained practical experience in secure containerization, dependency management, and image distribution via DockerHub.

---

## 👤 Author
**Krishna Anvith Vattikuti**  
📧 vattikutianvith@gmail.com  
🔗 [GitHub](https://github.com/anvith123) | [DockerHub](https://hub.docker.com/u/anvith123)

