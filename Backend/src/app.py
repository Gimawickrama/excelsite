from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import pandas as pd
from fpdf import FPDF

app = Flask(__name__)
CORS(app)

# Sample data to be exported
data = [
    {"Invoice No": "USS-0018732", "Serial No": 3671, "Traders Name": "CASH", "Name": "KASUN", "Cash": 7500.00, "Credit": "-", "Cheque": "-", "C/Card": "-", "BANK DT": "-", "C/Note": "-", "Advance": "-" , "Total":7500.00, "GP":600.00},
    {"Invoice No": "USS-0018734", "Serial No": 3674, "Traders Name": "CASH", "Name": "Nifraz", "Cash": 5500.00, "Credit": "-", "Cheque": "-", "C/Card": "-", "BANK DT": 79000.00, "C/Note": "-", "Advance": "-" ,"Total":7500.00, "GP":600.00},
    {"Invoice No": "USS-0018735", "Serial No": 3674, "Traders Name": "CASH", "Name": "MUDITH", "Cash": 9500.00, "Credit": "-", "Cheque": 9000.00, "C/Card": "-", "BANK DT": "-", "C/Note": "-", "Advance": 8000.00 ,"Total":7500.00, "GP":600.00},
    {"Invoice No": "USS-0018736", "Serial No": 3675, "Traders Name": "CASH", "Name": "ABDUR", "Cash": 4500.00, "Credit": "-", "Cheque": "-", "C/Card": "-", "BANK DT": "-", "C/Note": "-", "Advance": "-" ,"Total":7500.00, "GP":600.00},
    {"Invoice No": "USS-0018737", "Serial No": 3676, "Traders Name": "CASH", "Name": "MUDITH", "Cash": 22500.00, "Credit": "-", "Cheque": "-", "C/Card": "-", "BANK DT": "-", "C/Note": "-", "Advance": "-" ,"Total":7500.00, "GP":600.00},
]



@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)


# API to export CSV
@app.route('/export/csv', methods=['GET'])
def export_csv():
    df = pd.DataFrame(data)
    file_path = "data.csv"
    df.to_csv(file_path, index=False)
    return send_file(file_path, as_attachment=True)

# API to export Excel
@app.route('/export/excel', methods=['GET'])
def export_excel():
    df = pd.DataFrame(data)
    file_path = "data.xlsx"
    df.to_excel(file_path, index=False)
    return send_file(file_path, as_attachment=True)

# API to export PDF
@app.route('/export/pdf', methods=['GET'])
def export_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add a title to the PDF
    pdf.cell(200, 10, txt="Table Data Export", ln=True, align='C')

    # Add table header
    headers = ["Invoice No", "Serial No", "Traders Name", "Name", "Cash", "Credit", "Cheque", "C/Card", "BANK DT", "C/Note", "Advance","Total","GP"]
    pdf.set_font("Arial", 'B', 12)
    for header in headers:
        pdf.cell(30, 10, header, 1, 0, 'C')
    pdf.ln()

    # Add table rows to the PDF
    pdf.set_font("Arial", size=12)
    for record in data:
        pdf.cell(30, 10, str(record['Invoice No']), 1)
        pdf.cell(30, 10, str(record['Serial No']), 1)
        pdf.cell(30, 10, str(record['Traders Name']), 1)
        pdf.cell(30, 10, str(record['Name']), 1)
        pdf.cell(30, 10, str(record['Cash']), 1)
        pdf.cell(30, 10, str(record['Credit']), 1)
        pdf.cell(30, 10, str(record['Cheque']), 1)
        pdf.cell(30, 10, str(record['C/Card']), 1)
        pdf.cell(30, 10, str(record['BANK DT']), 1)
        pdf.cell(30, 10, str(record['C/Note']), 1)
        pdf.cell(30, 10, str(record['Advance']), 1)
        pdf.cell(30, 10, str(record['Total']), 1)
        pdf.cell(30, 10, str(record['GP']), 1)
        pdf.ln()

    file_path = "data.pdf"
    pdf.output(file_path)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
