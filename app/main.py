import os
from app.property_api import get_property_data
from app.report_generator import clean_property_report, generate_pdf_report
from dotenv import load_dotenv
load_dotenv()

def main():
    api_key = os.getenv("PROPERTY_API_KEY")
    if not api_key:
        raise ValueError("PROPERTY_API_KEY not found in environment variables.")

    address = "1600 Amphitheatre Parkway, Mountain View, CA"

    property_data = get_property_data(address, api_key)
    report_data = clean_property_report(property_data)

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "property_report.pdf")
    generate_pdf_report(report_data, output_path)

    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    main()