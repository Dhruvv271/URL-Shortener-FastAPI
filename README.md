# 🚀 URL Shortener (FastAPI + SQLite + Docker)

A high-performance URL shortener service built for speed and simplicity. This project demonstrates a production-ready API architecture using **FastAPI**, containerization with **Docker**, and automated deployment on **Render**.

---

## 📌 Features

* **⚡ Instant Shortening:** Converts long URLs into concise, shareable links.
* **🔗 Smart Redirection:** Automatically redirects visitors to the original destination.
* **📊 Live Analytics:** Tracks click counts and timestamps for every access event.
* **🐳 Dockerized:** Fully containerized for consistent deployment across any environment.
* **☁️ Cloud Ready:** Live deployment on Render web services.

---

## 🛠️ Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (High-performance Python web framework)
* **Database:** SQLite (Lightweight, serverless relational DB)
* **Containerization:** Docker
* **Deployment:** Render

---

## 📖 API Usage Guide

### 1. Create a Short Link
**Endpoint:** `POST /shorten`
Input a JSON body with your target URL.

**Request:**
```json
{
  "url": "[https://www.example.com](https://www.example.com)"
}
Response:

JSON

{
  "short_url": "[https://your-domain.com/abc123](https://your-domain.com/abc123)"
}
2. Redirect
Endpoint: GET /{short_code}

Accessing the shortened URL (e.g., /abc123) in a browser automatically redirects you to the original website.

This action increments the click counter in the background.

3. View Analytics
Endpoint: GET /analytics/{short_code} Get detailed stats on link performance.

Response:

JSON

{
  "short_code": "abc123",
  "original_url": "[https://www.example.com](https://www.example.com)",
  "clicks": 5,
  "history": [
    "2025-01-01T12:00:00",
    "2025-01-01T12:05:00"
  ]
}
⚙️ Local Installation & Setup
Follow these steps to run the project on your local machine.

Prerequisites
Python 3.9+

Git

Steps
Clone the Repository

Bash

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
Create a Virtual Environment

Bash

# Create the environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate
Install Dependencies

Bash

pip install -r requirements.txt
Run the Server

Bash

uvicorn main:app --reload
Test the API Open your browser and navigate to the interactive documentation: 👉 http://localhost:8000/docs

🐳 Docker Deployment
To run this application as a container:

Build the Image

Bash

docker build -t url-shortener .
Run the Container

Bash

docker run -p 8000:8000 url-shortener
🌐 Live Demo
The project is deployed and live on Render. You can test the API endpoints directly via the Swagger UI.

👉 Live Link: https://url-shortener-cx2i.onrender.com/docs

Note: Ensure you append /docs to the URL to access the interactive API interface.

Author: Dhruv Vijay