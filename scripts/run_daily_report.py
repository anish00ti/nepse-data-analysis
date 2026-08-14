from src.analysis.market_analysis import market_summary
from src.reports.report_generator import generate_html_report

def main():
    # Replace this section with the verified NEPSE extraction pipeline.
    summary = {"status": "Project initialized"}
    report = generate_html_report(summary)
    print(f"Report generated: {report}")

if __name__ == "__main__":
    main()
