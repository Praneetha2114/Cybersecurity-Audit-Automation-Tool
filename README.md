Cybersecurity Audit Automation Tool

A Python-based project that automates key steps of the cybersecurity audit process.

The tool helps generate audit checklists, calculate compliance results, and visualize audit findings using an interactive dashboard.

Project Features
Control Library

The project maintains a centralized list of security controls in:

questions.xlsx

Each control contains the following fields:

Domain

Question

Framework

Control ID

Example control mapping:

Domain	Question	Framework	Control ID
Access Control	Role-based access control implemented	ISO 27001	A.9.1
Authentication	Multi-factor authentication enabled	CIS	CIS 6
Monitoring	Logs monitored using a SIEM tool	NIST	DE.AE
Automated Audit Checklist Generation

Script used:

export_to_excel.py

Functionality:

Reads security controls from questions.xlsx

Generates a structured checklist

Adds audit tracking columns automatically

Generated file:

audit_checklist.xlsx

Checklist structure:

S.No	Domain	Question	Framework	Control ID	Status	Evidence	Comments
Status Tracking

The Status column contains a dropdown with three values:

Pass

Fail

Not Tested

Status colors are automatically applied.

Status	Color
Pass	Green
Fail	Red
Not Tested	Yellow

This allows quick identification of control results.

Compliance Scoring

Script used:

audit_score.py

The script calculates the following metrics:

Total Controls

Passed Controls

Failed Controls

Compliance Percentage

Example output:

Total Controls: 45
Passed Controls: 30
Failed Controls: 10
Compliance Score: 66.7%

Generated report file:

audit_report.xlsx
Interactive Audit Dashboard

Script used:

audit_dashboard.py

The dashboard is built using Streamlit.

Run the dashboard using:

streamlit run audit_dashboard.py
Dashboard Capabilities

The dashboard provides the following analytics:

Compliance Metrics

Total Controls

Passed Controls

Failed Controls

Compliance Percentage

Control Status Distribution

Displays the distribution of:

Pass

Fail

Not Tested

Domain Compliance Analysis

Example:

Domain	Passed	Failed	Compliance %
Access Control	8	2	80%
Authentication	6	4	60%

Framework Coverage

Displays the number of controls mapped to frameworks.

Framework	Controls
ISO 27001	20
NIST	15
CIS	10

Failed Control Risk Analysis

Failed controls are categorized by risk.

Domain	Question	Risk Level
Authentication	MFA not enabled	High
Backup & Recovery	Backup restoration not tested	Medium

Domain Filtering

Users can filter the dashboard by security domain.

Examples:

Governance

Access Control

Authentication

Monitoring

Incident Response

Export Results

Filtered results can be exported as:

audit_results.csv
Technologies Used

The project uses the following technologies:

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
How to Use the Tool
Step 1 — Define Security Controls

Edit the control library:

questions.xlsx

Required columns:

Domain | Question | Framework | Control ID
Step 2 — Generate the Audit Checklist

Run the following script:

python export_to_excel.py

Generated file:

audit_checklist.xlsx
Step 3 — Conduct the Audit

Open the checklist and update the Status column.

Options:

Pass

Fail

Not Tested

Optional fields:

Evidence

Comments

Step 4 — Generate Compliance Report

Run:

python audit_score.py

Output file:

audit_report.xlsx
Step 5 — Launch the Dashboard

Run:

streamlit run audit_dashboard.py

Upload the checklist file to visualize audit analytics.

Example Use Cases

This project demonstrates:

Cybersecurity audit automation

Security compliance monitoring

Security control tracking

Risk analysis and reporting

Security dashboard visualization


Author
Praneetha

GitHub Profile:

https://github.com/Praneetha2114

License

This project is created for educational and portfolio purposes.
