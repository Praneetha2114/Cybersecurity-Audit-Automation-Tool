Cybersecurity Audit Automation Tool

A Python-based tool that helps automate cybersecurity audit processes by generating audit checklists, tracking control compliance, and visualizing results through an interactive dashboard.

The project demonstrates how security audits can be automated using Python, Excel, and data visualization.

Project Features
Control Library

Centralized list of cybersecurity controls stored in questions.xlsx.

Each control includes:

Domain

Control Question

Security Framework

Control ID

Example:

Domain	Question	Framework	Control ID
Access Control	Role-based access control implemented	ISO 27001	A.9.1
Authentication	Multi-factor authentication enabled	CIS	CIS 6
Automated Audit Checklist

The script export_to_excel.py generates a structured audit checklist.

Generated file:

audit_checklist.xlsx

Checklist format:

S.No	Domain	Question	Framework	Control ID	Status	Evidence	Comments

Status dropdown options

Pass

Fail

Not Tested

Automatic color indicators

Status	Color
Pass	Green
Fail	Red
Not Tested	Yellow
Compliance Analysis

The script audit_score.py calculates audit results.

Metrics generated:

Total controls

Passed controls

Failed controls

Compliance percentage

Example output:

Total Controls: 45
Passed Controls: 30
Failed Controls: 10
Compliance Score: 66.7%

Results exported to:

audit_report.xlsx
Interactive Dashboard

The project includes a Streamlit dashboard to visualize audit results.

Run:

streamlit run audit_dashboard.py

Dashboard capabilities:

Overall compliance metrics

Control status distribution

Domain-wise compliance analysis

Framework coverage

Failed control risk analysis

Domain filtering

Export filtered audit data

Technologies Used

Python

Pandas

OpenPyXL

Streamlit

Microsoft Excel

Project Structure
cybersecurity-audit-tool
│
├── questions.xlsx
├── export_to_excel.py
├── audit_score.py
├── audit_dashboard.py
├── audit_checklist.xlsx
├── audit_report.xlsx
└── README.md
Installation

Clone the repository:

git clone https://github.com/Praneetha2114/cybersecurity-audit-tool.git

Navigate to the project folder:

cd cybersecurity-audit-tool

Install required libraries:

pip install pandas openpyxl streamlit
How to Use
1. Define Controls

Edit questions.xlsx and add audit controls.

Required columns:

Domain | Question | Framework | Control ID
2. Generate Audit Checklist

Run:

python export_to_excel.py

This creates:

audit_checklist.xlsx
3. Perform Audit

Open audit_checklist.xlsx and update the Status column.

Options:

Pass

Fail

Not Tested

Add evidence and comments if needed.

4. Generate Compliance Report

Run:

python audit_score.py

This produces:

audit_report.xlsx
5. Launch Dashboard

Run:

streamlit run audit_dashboard.py

Upload the generated checklist to visualize results.

Example Use Cases

This project demonstrates:

Cybersecurity audit automation

Compliance monitoring

Risk analysis

Security dashboard visualization

Future Improvements

Potential enhancements:

PDF audit report generation

Multi-organization audit support

Control maturity scoring

Cloud security control analysis

Integration with vulnerability scanning tools

Author

Praneetha

GitHub:
https://github.com/Praneetha2114

License

This project is intended for educational and portfolio purposes.
