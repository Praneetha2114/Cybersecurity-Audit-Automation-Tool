Cybersecurity Audit Automation Tool

A Python project that helps automate cybersecurity audits by generating audit checklists, calculating compliance, and visualizing results through a dashboard.

Key Features
Control Library

Stored in questions.xlsx

Contains cybersecurity audit controls

Each control includes:

Domain

Question

Framework

Control ID

Example:

Domain	Question	Framework	Control ID
Access Control	Role-based access control implemented	ISO 27001	A.9.1
Authentication	Multi-factor authentication enabled	CIS	CIS 6
Audit Checklist Generator

Script: export_to_excel.py

What it does:

Reads controls from questions.xlsx

Generates audit_checklist.xlsx

Adds audit tracking columns

Checklist columns:

S.No

Domain

Question

Framework

Control ID

Status

Evidence

Comments

Status Tracking

Dropdown options:

Pass

Fail

Not Tested

Color indicators:

Status	Color
Pass	Green
Fail	Red
Not Tested	Yellow
Compliance Scoring

Script: audit_score.py

Calculates:

Total controls

Passed controls

Failed controls

Compliance percentage

Example output:

Total Controls: 45
Passed Controls: 30
Failed Controls: 10
Compliance Score: 66.7%

Generated file:

audit_report.xlsx
Interactive Dashboard

Script: audit_dashboard.py

Run using:

streamlit run audit_dashboard.py

Dashboard features:

Compliance metrics

Domain compliance analysis

Framework coverage

Failed control risk analysis

Domain filtering

Export audit data

Technologies Used

Python

Pandas

OpenPyXL

Streamlit

Excel

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
Clone repository
git clone https://github.com/Praneetha2114/Cybersecurity-Audit-Automation-Tool.git
Navigate to project folder
cd Cybersecurity-Audit-Automation-Tool
Install dependencies
pip install pandas openpyxl streamlit
How to Use
Step 1 — Define Controls

Edit:

questions.xlsx

Required columns:

Domain | Question | Framework | Control ID
Step 2 — Generate Checklist

Run:

python export_to_excel.py

Creates:

audit_checklist.xlsx
Step 3 — Conduct Audit

Update the Status column in the checklist:

Pass

Fail

Not Tested

Optional fields:

Evidence

Comments

Step 4 — Generate Compliance Report

Run:

python audit_score.py

Creates:

audit_report.xlsx
Step 5 — Launch Dashboard

Run:

streamlit run audit_dashboard.py

Upload audit_checklist.xlsx to visualize results.

Use Cases

This project demonstrates:

Cybersecurity audit automation

Compliance monitoring

Security control management

Audit data visualization

Author

Praneetha

GitHub:
https://github.com/Praneetha2114

License

Educational / portfolio project.
