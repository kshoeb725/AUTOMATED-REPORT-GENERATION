import csv
from fpdf import FPDF

# Function to read data from CSV file
def read_data_from_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append({'Name': row['Name'], 'Value': float(row['Value'])})
    return data

# Function to analyze data
def analyze_data(data):
    values = [item['Value'] for item in data]
    average = sum(values) / len(values)
    maximum = max(values)
    minimum = min(values)
    return average, maximum, minimum

# Function to generate PDF report
def generate_pdf_report(data, average, maximum, minimum, output_file):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, 'Data Analysis Report', ln=True, align='C')
    
    # Add a line break
    pdf.ln(10)
    
    # Add analysis results
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f'Average Value: {average:.2f}', ln=True)
    pdf.cell(0, 10, f'Maximum Value: {maximum}', ln=True)
    pdf.cell(0, 10, f'Minimum Value: {minimum}', ln=True)
    
    # Add a line break
    pdf.ln(10)
    
    # Add data table
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, 'Name', 1)
    pdf.cell(40, 10, 'Value', 1)
    pdf.ln()
    
    pdf.set_font("Arial", size=12)
    for item in data:
        pdf.cell(40, 10, item['Name'], 1)
        pdf.cell(40, 10, str(item['Value']), 1)
        pdf.ln()
    
    # Save the PDF to a file
    pdf.output(output_file)

# Main function
def main():
    input_file = 'data.csv'
    output_file = 'report.pdf'
    
    # Read data from CSV
    data = read_data_from_csv(input_file)
    
    # Analyze data
    average, maximum, minimum = analyze_data(data)
    
    # Generate PDF report
    generate_pdf_report(data, average, maximum, minimum, output_file)
    print(f'Report generated: {output_file}')

if __name__ == '__main__':
    main()