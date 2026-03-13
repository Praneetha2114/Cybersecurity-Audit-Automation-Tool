Cybersecurity Audit Automation Tool

A Python-based cybersecurity project designed to automate parts of the security audit process.

This tool helps with:

Generating audit checklists

Tracking security control compliance

Calculating audit scores

Visualizing results through an interactive dashboard

Project Features
1. Control Library

The project uses a centralized control repository stored in questions.xlsx.

Each security control includes the following fields:

Domain

Control Question

Security Framework

Control ID

Example Control Mapping

Domain	Question	Framework	Control ID
Access Control	Is role-based access control implemented?	ISO 27001	A.9.1
Authentication	Is multi-factor authentication enabled?	CIS	CIS 6
Monitoring	Are logs monitored using a SIEM tool?	NIST	DE.AE
2. Automated Audit Checklist Generator

Script used:

export_to_excel.py

This script performs the following steps:

Reads controls from questions.xlsx

Generates a structured checklist

Adds audit tracking columns automatically

Generated file:

audit_checklist.xlsx

Checklist Structure

S.No	Domain	Question	Framework	Control ID	Status	Evidence	Comments
1	Governance	Information Security Policy defined	ISO 27001	A.5.1	Not Tested		
2	Access Control	Role-based access implemented	ISO 27001	A.9.1	Not Tested		
3. Status Tracking

The Status column includes a dropdown menu with the following options:

Pass

Fail

Not Tested

Each status is automatically color-coded.

Status	Color Indicator
Pass	Green
Fail	Red
Not Tested	Yellow

This helps auditors quickly identify control results.

4. Compliance Scoring

Script used:

audit_score.py

This script calculates audit metrics including:

Total Controls

Passed Controls

Failed Controls

Compliance Percentage

Example Output

Total Controls: 45
Passed Controls: 30
Failed Controls: 10
Compliance Score: 66.7%

Generated report file:

audit_report.xlsx
5. Interactive Audit Dashboard

Script used:

audit_dashboard.py

The dashboard is built using Streamlit.

Run the dashboard using:

streamlit run audit_dashboard.py
Dashboard Capabilities

The dashboard provides:

• Overall compliance metrics

Total Controls

Passed Controls

Failed Controls

Compliance Percentage

• Control Status Distribution

Visualization showing:

Pass

Fail

Not Tested

• Domain Compliance Analysis

Example:

Domain	Passed	Failed	Compliance %
Access Control	8	2	80%
Authentication	6	4	60%

• Framework Coverage

Shows number of controls mapped to frameworks.

Framework	Controls
ISO 27001	20
NIST	15
CIS	10

• Failed Control Risk Analysis

Failed controls are categorized by risk.

Domain	Question	Risk Level
Authentication	MFA not enabled	High
Backup & Recovery	Backup not tested	Medium

• Domain Filtering

Users can filter the dashboard by security domain.

Example filters:

Governance

Access Control

Authentication

Monitoring

Incident Response

• Export Results

Users can export filtered results as:

audit_results.csv
Technologies Used

This project uses the following technologies:

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
1. Clone the Repository
git clone https://github.com/Praneetha2114/Cybersecurity-Audit-Automation-Tool.git
2. Navigate to the Project Folder
cd Cybersecurity-Audit-Automation-Tool
3. Install Dependencies
pip install pandas openpyxl streamlit
How to Use the Tool
Step 1 — Define Security Controls

Edit the control library:

questions.xlsx

Required columns:

Domain | Question | Framework | Control ID
Step 2 — Generate the Audit Checklist

Run:

python export_to_excel.py

Generated file:

audit_checklist.xlsx
Step 3 — Conduct the Audit

Open the checklist and update the Status column:

Pass

Fail

Not Tested

Optional fields:

Evidence

Comments

Step 4 — Generate Compliance Report

Run:

python audit_score.py

Output:

audit_report.xlsx
Step 5 — Launch the Dashboard

Run:

streamlit run audit_dashboard.py

Upload the checklist file to visualize results.

Example Use Cases

This project demonstrates:

Cybersecurity audit automation

Security compliance tracking

Security control monitoring

Risk analysis and reporting

Security dashboard visualization

Author

Praneetha

GitHub Profile
https://github.com/Praneetha2114

License

This project is created for educational and portfolio purposes.
