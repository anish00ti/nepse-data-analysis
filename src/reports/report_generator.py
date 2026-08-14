from pathlib import Path
from datetime import date
from jinja2 import Environment, FileSystemLoader
from config.config import REPORT_DIR

def generate_html_report(summary: dict):
    template_dir = Path(__file__).parent / "templates"
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("daily_report.html")

    html = template.render(report_date=date.today(), summary=summary)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    output = REPORT_DIR / f"nepse_report_{date.today()}.html"
    output.write_text(html, encoding="utf-8")
    return output
