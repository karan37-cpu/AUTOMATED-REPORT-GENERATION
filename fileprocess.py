import pandas as pd
from fpdf import FPDF
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 16)
        self.cell(0, 10, "CSV Data Analysis Report", ln=True, align="C")
        self.ln(10)

    def add_section_title(self, title):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def add_text(self, text):
        self.set_font("Arial", '', 12)
        self.multi_cell(0, 8, text)
        self.ln()

def analyze_data(df):
    summary = df.describe(include='all')  # Basic statistics
    return summary

def generate_pdf(data_summary, output_file):
    pdf = PDFReport()
    pdf.add_page()

    pdf.add_section_title("Summary Statistics")

    for column in data_summary.columns:
        pdf.add_section_title(f"Column: {column}")
        for stat in data_summary.index:
            value = data_summary.loc[stat, column]
            pdf.add_text(f"{stat}: {value}")
    
    pdf.output(output_file)
    print(f"✅ PDF report saved as '{output_file}'")

def main():
    csv_path = input("Enter path to CSV file: ").strip()
    
    if not os.path.exists(csv_path):
        print("❌ File not found.")
        return

    df = pd.read_csv(csv_path)
    summary = analyze_data(df)

    generate_pdf(summary, "CSV_Report.pdf")

if __name__ == "__main__":
    main()
