# NEPSE Market Report

Automated NEPSE data pipeline:
1. Scrape market data
2. Clean with Pandas
3. Store historical data
4. Analyze market
5. Generate daily report
6. Email the report
7. Schedule automatically

## Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and configure email settings.

## Run

```bash
python scripts/run_daily_report.py
```

> The scraper is intentionally a starter module. Verify NEPSE's current data access method and applicable website terms before implementing production scraping.
