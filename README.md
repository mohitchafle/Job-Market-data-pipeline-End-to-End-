# End-to-End Job Market Data Pipeline

## Overview
The **End-to-End Job Market Data Pipeline** is a data engineering project that extracts real-time job listings from a public API, processes and transforms the data, stores it in a relational database, and generates actionable insights through dashboards.

This project demonstrates core data engineering concepts such as **ETL (Extract, Transform, Load)**, workflow automation, and data visualization.
---

## Objectives
- Build a scalable ETL pipeline using real-world data  
- Automate data workflows using scheduling tools  
- Store structured data in a relational database  
- Generate insights for decision-making using dashboards  
---


## Architecture
API (Adzuna)
    ↓
Extract (Python - Requests)
    ↓
Transform (Pandas)
    ↓
Load (MySQL)
    ↓
Automation (Airflow DAG)
    ↓
Visualization (Power BI Dashboard)
---


## Tech Stack -

| Category            | Tools Used     |
|---------------------|----------------|
| Programming         | Python         |
| Data Processing     | Pandas         |
| API Integration     | Requests       |
| Database            | MySQL          |
| Workflow Automation | Apache Airflow |
| Visualization       | Power BI       |

---

## 🔄 Project Workflow
### 1️⃣ Data Extraction
- Fetches real-time job data from the Adzuna API  
- Retrieves job details such as title, company, salary, and location  
- Stores raw data in JSON format  

### 2️⃣ Data Transformation
- Cleans and processes semi-structured JSON data  
- Handles missing/null values  
- Converts data into structured tabular format (CSV)  

### 3️⃣ Data Loading
- Creates a MySQL database and table schema  
- Inserts transformed data into database  
- Ensures data consistency and integrity  

### 4️⃣ Workflow Automation
- Uses Apache Airflow DAGs to automate ETL pipeline  
- Schedules daily execution of tasks  
- Maintains pipeline reliability  

### 5️⃣ Data Visualization
- Connects MySQL database to Power BI  
- Builds dashboards to analyze:
  - Hiring trends  
  - Salary distribution  
  - Job demand by location  
  - In-demand roles  

        ---

