[![Back to Portfolio](https://img.shields.io/badge/←_Back_to_Portfolio-0A66C2?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aestevaomoraes)

# 📊 Telecom Operations Analytics (AI + Automation)

## 🎯 Business Problem

In telecom operations, generating daily reports for SLA monitoring and operational performance is often manual, time-consuming, and inconsistent.

This project was developed to solve this problem by:

👉 Automating operational analysis using Python  
👉 Leveraging AI (Prompt Engineering) to structure insights  
👉 Reducing manual workload in reporting processes  

---

## 🤖 Solution Overview

This project combines:

- 📊 Data processing (Python & Pandas)  
- 🤖 AI-driven insights (Prompt Engineering - Antigravity)  
- ⚙️ Automation of daily reporting workflows  

👉 Result: a fully automated pipeline for generating business-ready reports.

---

## 📦 Dataset

Operational dataset containing:

- Service requests  
- SLA deadlines  
- Resolution times  
- Operational backlog  

---

## 🧠 Approach

The workflow follows a modern data + AI approach:

🔹 Data ingestion and cleaning  
🔹 KPI calculation (SLA, backlog, resolution time)  
🔹 AI-assisted interpretation (prompt engineering)  
🔹 Automated report generation (Markdown output)  

---

## 🧹 Data Processing

- Cleaning and structuring operational data  
- Standardizing time-based metrics  
- Preparing data for automated reporting  

---

## 📊 Key Metrics

- ⏱️ SLA compliance  
- 📉 Backlog volume  
- 📈 Average resolution time  
- 🚨 Delayed requests  

---

## ⚙️ Automation Workflow

Daily process:

1. Extract latest dataset (`bd_Online.csv`)  
2. Replace file in `data/raw/`  
3. Run automated script  

```bash
python src/data/generate_report.py
