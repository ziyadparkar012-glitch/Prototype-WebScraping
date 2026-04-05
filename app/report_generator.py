from xhtml2pdf import pisa
from datetime import datetime


def fmt(value):
    if value is None:
        return "N/A"
    if isinstance(value, (int, float)):
        return f"{value:,}"
    return value


def fmt_money(value):
    if value is None:
        return "N/A"
    return f"${value:,}"


def clean_property_report(data: dict):
    return {
        "address": data.get("address"),
        "city": data.get("city"),
        "state": data.get("state"),
        "zip_code": data.get("zip_code"),
        "county": data.get("county"),
        "apn": data.get("apn"),
        "owner": data.get("owner"),
        "owner_type": data.get("owner_type"),
        "property_type": data.get("property_type"),
        "use_desc": data.get("use_desc"),
        "square_feet": data.get("square_feet"),
        "lot_size_acres": data.get("lot_size"),
        "year_built": data.get("year_built"),
        "stories": data.get("stories"),
        "bedrooms": data.get("bedrooms"),
        "bathrooms": data.get("bathrooms"),
        "zoning": data.get("zoning"),
        "market_estimate": data.get("market_estimate"),
        "annual_tax": data.get("annual_tax"),
        "last_sale_date": data.get("last_sale_date"),
        "last_sale_price": data.get("last_sale_price"),
        "flood_zone": data.get("flood_zone"),
        "flood_zone_community_name": data.get("flood_zone_community_name"),
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "google_map_url": data.get("google_map_url"),
    }


def render_html_report(data: dict):
    generated_on = datetime.now().strftime("%Y-%m-%d %H:%M")

    return f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 40px;
                line-height: 1.6;
                color: #333;
            }}
            h1 {{
                text-align: center;
                margin-bottom: 0;
            }}
            h2 {{
                margin-top: 30px;
                border-left: 5px solid #4CAF50;
                padding-left: 10px;
            }}
            .subtitle {{
                text-align: center;
                color: gray;
                margin-top: 5px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
            }}
            td {{
                padding: 10px;
                border-bottom: 1px solid #eee;
                vertical-align: top;
            }}
            td.label {{
                font-weight: bold;
                width: 35%;
                background-color: #f9f9f9;
            }}
        </style>
    </head>
    <body>
        <h1>Property Intelligence Report</h1>
        <p class="subtitle">Generated on: {generated_on}</p>

        <h2>Location</h2>
        <table>
            <tr><td class="label">Address</td><td>{fmt(data["address"])}</td></tr>
            <tr><td class="label">City</td><td>{fmt(data["city"])}</td></tr>
            <tr><td class="label">State</td><td>{fmt(data["state"])}</td></tr>
            <tr><td class="label">ZIP Code</td><td>{fmt(data["zip_code"])}</td></tr>
            <tr><td class="label">County</td><td>{fmt(data["county"])}</td></tr>
            <tr><td class="label">Latitude</td><td>{fmt(data["latitude"])}</td></tr>
            <tr><td class="label">Longitude</td><td>{fmt(data["longitude"])}</td></tr>
            <tr><td class="label">Map</td><td><a href="{fmt(data["google_map_url"])}">View on Google Maps</a></td></tr>
        </table>

        <h2>Ownership</h2>
        <table>
            <tr><td class="label">Owner</td><td>{fmt(data["owner"])}</td></tr>
            <tr><td class="label">Owner Type</td><td>{fmt(data["owner_type"])}</td></tr>
            <tr><td class="label">APN</td><td>{fmt(data["apn"])}</td></tr>
        </table>

        <h2>Property Details</h2>
        <table>
            <tr><td class="label">Property Type</td><td>{fmt(data["property_type"])}</td></tr>
            <tr><td class="label">Use Description</td><td>{fmt(data["use_desc"])}</td></tr>
            <tr><td class="label">Square Feet</td><td>{fmt(data["square_feet"])}</td></tr>
            <tr><td class="label">Lot Size (Acres)</td><td>{fmt(data["lot_size_acres"])}</td></tr>
            <tr><td class="label">Year Built</td><td>{fmt(data["year_built"])}</td></tr>
            <tr><td class="label">Stories</td><td>{fmt(data["stories"])}</td></tr>
            <tr><td class="label">Bedrooms</td><td>{fmt(data["bedrooms"])}</td></tr>
            <tr><td class="label">Bathrooms</td><td>{fmt(data["bathrooms"])}</td></tr>
            <tr><td class="label">Zoning</td><td>{fmt(data["zoning"])}</td></tr>
        </table>

        <h2>Valuation</h2>
        <table>
            <tr><td class="label">Market Estimate</td><td>{fmt_money(data["market_estimate"])}</td></tr>
            <tr><td class="label">Annual Tax</td><td>{fmt_money(data["annual_tax"])}</td></tr>
            <tr><td class="label">Last Sale Date</td><td>{fmt(data["last_sale_date"])}</td></tr>
            <tr><td class="label">Last Sale Price</td><td>{fmt_money(data["last_sale_price"])}</td></tr>
        </table>

        <h2>Risk / Flood</h2>
        <table>
            <tr><td class="label">Flood Zone</td><td>{fmt(data["flood_zone"])}</td></tr>
            <tr><td class="label">Flood Zone Community</td><td>{fmt(data["flood_zone_community_name"])}</td></tr>
        </table>
    </body>
    </html>
    """


def generate_pdf_report(report_data: dict, output_path: str):
    html = render_html_report(report_data)

    with open(output_path, "wb") as pdf_file:
        pisa.CreatePDF(html, dest=pdf_file)