from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf(df, anomalies, forecast):

    os.makedirs("outputs", exist_ok=True)

    file_path = "outputs/climate_report.pdf"
    c = canvas.Canvas(file_path, pagesize=letter)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "🌍 Climate Analysis Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 720, f"Total Records: {len(df)}")
    c.drawString(50, 700, f"Anomalies: {len(anomalies)}")

    # Forecast
    y = 660
    c.drawString(50, y, "📊 Forecast (Next 12 months):")
    y -= 20

    for i, val in enumerate(forecast[:10]):
        c.drawString(60, y, f"{i+1}. {val}")
        y -= 15

    # Images
    c.drawString(50, y-20, "📈 Charts Generated:")
    c.drawImage("outputs/raw_trend.png", 50, 300, width=500, height=200)

    c.showPage()

    c.save()

    return file_path