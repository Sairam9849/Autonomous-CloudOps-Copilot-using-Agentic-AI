# 🚀 Autonomous CloudOps Copilot using Agentic AI

## 📌 Overview
Autonomous CloudOps Copilot is an AI-powered incident analysis dashboard built using Python, Streamlit, Kubernetes, and AWS. The system automates cloud incident investigation using multiple agents and provides root cause analysis with remediation suggestions.

---

## ✨ Features

- ✅ AWS Health Monitoring
- ✅ Kubernetes Pod Monitoring
- ✅ Jenkins Build Status Analysis
- ✅ Severity Detection
- ✅ Root Cause Analysis
- ✅ Automated Remediation Suggestions
- ✅ Incident Dashboard using Streamlit
- ✅ Multi-Agent Architecture

---

## 🛠 Tech Stack

- Python
- Streamlit
- Kubernetes
- AWS
- Git & GitHub
- Agentic AI

---

## 🏗 Architecture

Incident → Planner Agent → AWS Agent → Kubernetes Agent → Jenkins Agent → Severity Agent → Root Cause Agent → Remediation Agent → Dashboard

---

## 📊 Sample Incident

**Input:**

```text
Deployment Failed
```

**Output:**

```text
AWS Status: EC2 Healthy
Kubernetes Status: Healthy
Jenkins Status: Build Success
Severity: High
Root Cause: Docker image missing
Recommended Fix: Push image and restart deployment
```

---

## 🚀 Run Locally

```bash
git clone <repo-url>
cd autonomous-cloudops

python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
streamlit run ui/app.py
```

---

## 👨‍💻 Author

**Muchintala Sai Ram**

GitHub: https://github.com/Sairam9849