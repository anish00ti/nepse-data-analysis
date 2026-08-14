# NEPSE Market Data Analysis & Daily Reporting

A Python-based data pipeline for collecting Nepal Stock Exchange (NEPSE)
market data, storing the data as CSV files, analyzing it with Pandas,
loading it into a database, generating daily market reports, and
automatically sending the generated report by email.

> **Project Status:** 🚧 Work in Progress  
> **Current Completed Stage:** Data Scraping  
> **Next Stages:** Data Cleaning → Snowflake → Analysis → Report → Email → Automation

---

## 📌 Project Overview

The main goal of this project is to build an automated NEPSE market-data
pipeline that runs daily.

The planned workflow is:

```text
                    NEPSE Websites
                         │
                         ▼
                  Data Scraping
                         │
                         ▼
                   Raw CSV Data
                         │
                         ▼
                Data Cleaning
                 & Processing
                         │
                         ▼
                  Snowflake DB
                         │
                         ▼
                Python + Pandas
                    Analysis
                         │
                         ▼
                 Charts / Insights
                         │
                         ▼
                  Daily Report
                         │
                         ▼
                    Email
                         │
                         ▼
              Automatic Daily Run
