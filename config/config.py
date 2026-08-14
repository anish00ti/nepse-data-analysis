from pathlib import Path
from dotenv import load_dotenv
import os

ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USER = os.getenv("EMAIL_USER", "")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")
REPORT_RECIPIENT = os.getenv("REPORT_RECIPIENT", "")
DATABASE_PATH = ROOT_DIR / "data" / "nepse.db"
REPORT_DIR = ROOT_DIR / "reports" / "daily"
CHART_DIR = ROOT_DIR / "reports" / "charts"
