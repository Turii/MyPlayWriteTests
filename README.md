# 🧪 MyPlayWriteTests

This project combines API and UI testing using **Flask**, **Playwright**, and **Pytest**.  
It demonstrates a full testing flow for CRUD operations through a web interface and REST API.

---

## 📁 Project Structure

MyPlayWriteTests/ ├── api/ # Flask API (POST, GET, PUT, DELETE) ├── apitests/ # API tests using Playwright's page.request ├── uitests/ # UI tests using Playwright ├── templates/ # HTML UI (index.html with testable buttons) ├── conftest.py # Shared fixtures (Flask + browser setup) ├── requirements.txt # Python dependencies ├── .github/workflows/ # GitHub Actions config └── README.md # 


## 🚀 Technologies

- Python 3.12
- Flask
- Pytest & Pytest-asyncio
- Playwright (with page API)
- GitHub Actions for CI/CD

---

## ✅ What’s Tested

### API Tests (via `/users` endpoint)
- `POST` create user
- `GET` retrieve user
- `PUT` update user
- `DELETE` remove user

### UI Tests (via index.html)
- Click "Create User" → expect "User created"
- Click "Get User" → expect "oksana"
- Click "Update User" → expect "Sunnyvale"
- Click "Delete User" → expect "User deleted"

---

## 🔧 How to Run Locally

1. Clone the repo & install requirements:
   ```bash
   pip install -r requirements.txt


## ✅ Test Results

After each push or pull request, a full HTML report is generated and attached as an artifact in GitHub Actions.

Look for it in the **Artifacts** section of each workflow run.