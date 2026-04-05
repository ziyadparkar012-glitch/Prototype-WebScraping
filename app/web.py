import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from app.property_api import get_property_data
from app.report_generator import clean_property_report, generate_pdf_report

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/generate-report")
def generate_report(address: str = Form(...)):
    api_key = os.getenv("PROPERTY_API_KEY")
    if not api_key:
        return HTMLResponse("Missing PROPERTY_API_KEY in .env", status_code=500)

    property_data = get_property_data(address, api_key)
    report_data = clean_property_report(property_data)

    os.makedirs("output", exist_ok=True)
    output_path = os.path.join("output", "property_report.pdf")

    generate_pdf_report(report_data, output_path)

    return FileResponse(
        path=output_path,
        media_type="application/pdf",
        filename="property_report.pdf",
    )