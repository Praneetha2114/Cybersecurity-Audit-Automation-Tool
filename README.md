# Cybersecurity Audit Automation Tool

A Python-based tool that automates parts of the cybersecurity audit workflow.

It helps security teams:

- Generate audit checklists
- Track control compliance
- Calculate compliance scores
- Visualize audit results in a dashboard

---

## Project Overview

This project demonstrates how cybersecurity audits can be automated using:

- Python
- Excel
- Data analytics
- Dashboard visualization

The tool converts a security control library into an interactive audit system.

---

## Key Features

### Control Library

Security controls are stored in:

questions.xlsx

Each control includes:

- Domain
- Question
- Framework
- Control ID

Example:

| Domain | Question | Framework | Control ID |
|------|------|------|------|
| Access Control | Role-based access control implemented | ISO 27001 | A.9.1 |
| Authentication | Multi-factor authentication enabled | CIS | CIS 6 |

---

### Automated Audit Checklist

Script used:

export_to_excel.py

This script:

- Reads controls from the control library
- Generates a structured audit checklist
- Adds tracking columns automatically

Generated file:

audit_checklist.xlsx

Checklist structure:

| S.No | Domain | Question | Framework | Control ID | Status | Evidence | Comments |

---

### Status Tracking

The Status column supports three options:

Pass  
Fail  
Not Tested  

Status colors:

| Status | Indicator |
|------|------|
| Pass | Green |
| Fail | Red |
| Not Tested | Yellow |

---

### Compliance Scoring

Script used:

audit_score.py

Metrics calculated:

- Total Controls
- Passed Controls
- Failed Controls
- Compliance Percentage

Example:

Total Controls: 45  
Passed Controls: 30  
Failed Controls: 10  
Compliance Score: 66.7%

Generated report:

audit_report.xlsx

---

### Interactive Dashboard

Dashboard built using Streamlit.

Run:

streamlit run audit_dashboard.py

Dashboard features:

- Compliance metrics
- Domain analysis
- Framework coverage
- Failed control analysis
- Domain filtering
- Export results

---

## Technologies Used

| Technology | Purpose |
|------|------|
| Python | Automation |
| Pandas | Data processing |
| OpenPyXL | Excel automation |
| Streamlit | Dashboard |
| Excel | Control library |

---

## Project Structure

Cybersecurity-Audit-Automation-Tool

questions.xlsx  
export_to_excel.py  
audit_score.py  
audit_dashboard.py  
audit_checklist.xlsx  
audit_report.xlsx  
README.md

---

## Installation

Clone the repository:

git clone https://github.com/Praneetha2114/Cybersecurity-Audit-Automation-Tool.git

Navigate to the project folder:

cd Cybersecurity-Audit-Automation-Tool

Install dependencies:

pip install pandas openpyxl streamlit

---

## Usage

Step 1 — Define Controls  
Edit the control library:

questions.xlsx

Required columns:

Domain | Question | Framework | Control ID

---

Step 2 — Generate Audit Checklist

python export_to_excel.py

---

Step 3 — Conduct Audit

Update the Status column:

Pass  
Fail  
Not Tested

Optional fields:

Evidence  
Comments

---

Step 4 — Generate Compliance Report

python audit_score.py

---

Step 5 — Launch Dashboard

streamlit run audit_dashboard.py

Upload the checklist to visualize results.

---

## Use Cases

This project demonstrates:

- Cybersecurity audit automation
- Security compliance monitoring
- Security control tracking
- Risk analysis and reporting
- Security dashboard visualization

---

## Author

Praneetha

GitHub  
https://github.com/Praneetha2114

---

## License

Educational / portfolio project.
