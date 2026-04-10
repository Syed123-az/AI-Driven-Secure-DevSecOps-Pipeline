# AI-Driven-Secure-DevSecOps-Pipeline
# 🔐 AI-Driven Secure DevSecOps Pipeline

## 📌 Overview

This project implements an end-to-end **DevSecOps pipeline** integrated with **Machine Learning** to automatically detect and respond to potential security threats in system logs.

The system analyzes incoming logs, classifies them as **normal or malicious**, and enforces automated actions such as **allowing or blocking requests** — simulating real-world secure CI/CD environments.

---

## 🚀 Key Features

* 🤖 Machine Learning-based Threat Detection (Random Forest)
* 🔍 Log Analysis & Feature Extraction
* ⚙️ Automated Security Actions (Allow / Block)
* 🌐 REST API using Flask (`/scan` endpoint)
* 📊 Interactive Frontend Dashboard
* 🔁 Simulated DevSecOps Pipeline Integration

---

## 🏗️ Project Structure

```
Final_year_project/
├── dataset/              # Raw and processed log data
├── ML_Model/             # Trained ML model (.pkl)
├── backend/              # Flask backend & APIs
├── Scripts/              # Dataset creation & model training
├── pipeline/             # DevSecOps pipeline simulation
├── frontend/             # Dashboard UI
```

---

## 🧠 How It Works

1. Logs are collected and preprocessed
2. Features are extracted from log data
3. ML model predicts threat level
4. Backend API returns:

   * Prediction (Normal / Malicious)
   * Confidence Score
   * Action (Allow / Block)
5. Pipeline enforces decision automatically
6. Results are displayed on the dashboard

---

## 🛠️ Tech Stack

* **Python** (Core Logic)
* **Scikit-learn** (ML Model)
* **Flask** (Backend API)
* **HTML, CSS, JavaScript** (Frontend Dashboard)
* **Pandas & NumPy** (Data Processing)

---

## 📊 Use Cases

* Secure CI/CD Pipelines
* Threat Detection Systems
* Log Monitoring & Analysis
* DevSecOps Automation

---

## ⚡ Future Enhancements

* Real-time log streaming
* Integration with Jenkins / GitHub Actions
* Advanced Deep Learning models
* Threat visualization & analytics dashboard

---

## 👨‍💻 Author

**Syed Azmath**
BCA (Data Science) | Final Year Project
