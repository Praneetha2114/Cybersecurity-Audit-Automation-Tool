Cybersecurity Audit Automation Tool

A Python-based project that automates parts of the cybersecurity audit process by generating audit checklists, calculating compliance scores, and visualizing results through an interactive dashboard.

This project demonstrates how security audits can be automated using Python, Excel, and data visualization.

Features
Control Library

Audit controls are stored in questions.xlsx and mapped to security frameworks.

Each control contains:

Domain

Question

Framework

Control ID

Example:

Domain	Question	Framework	Control ID
Access Control	Role-based access control implemented	ISO 27001	A.9.1
Authentication	Multi-factor authentication enabled	CIS	CIS 6
Automated Audit Checklist

The script export_to_excel.py automatically generates an audit checklist.

Generated file:

audit_checklist.xlsx

Checklist structure:

S.No	Domain	Question	Framework	Control ID	Status	Evidence	Comments

Status dropdown options:

Pass

Fail

Not Tested

Status colors:

Status	Color
Pass	Green
Fail	Red
Not Tested	Yellow
Compliance Scoring

The script audit_score.py calculates audit results.

Metrics generated:

Total Controls

Passed Controls

Failed Controls

Compliance Percentage

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

Compliance metrics

Domain-wise compliance analysis

Framework coverage

Failed control risk analysis

Domain filtering

Export audit data

Technologies Used

Python

Pandas

OpenPyXL

Streamlit

Microsoft Excel

Project Structure
Cybersecurity-Audit-Automation-Tool
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

git clone https://github.com/Praneetha2114/Cybersecurity-Audit-Automation-Tool.git

Navigate to the project folder:

cd Cybersecurity-Audit-Automation-Tool

Install dependencies:

pip install pandas openpyxl streamlit
How to Use
1. Define Controls

Add controls in questions.xlsx.

Required columns:

Domain | Question | Framework | Control ID
2. Generate Audit Checklist

Run:

python export_to_excel.py

This creates:

audit_checklist.xlsx
3. Perform Audit

Open the checklist and update the Status column.

Options:

Pass

Fail

Not Tested

You can also record Evidence and Comments.

4. Generate Compliance Report

Run:

python audit_score.py

This generates:

audit_report.xlsx
5. Launch Dashboard

Run:

streamlit run audit_dashboard.py

Upload the generated checklist to visualize audit analytics.

Example Use Cases

This project demonstrates:

Cybersecurity audit automation

Compliance monitoring

Security control tracking

Audit data visualization

Author

Praneetha

GitHub:
https://github.com/Praneetha2114

License

This project is intended for educational and portfolio purposes.
