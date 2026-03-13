Cybersecurity Audit Automation Tool

Overview-
The Cybersecurity Audit Automation Tool is a Python-based project designed to simplify and automate cybersecurity audit processes. It generates audit checklists, tracks compliance, analyzes security controls, and provides an interactive dashboard for visualizing audit results.

This project demonstrates how cybersecurity audits can be automated using Python, Excel, and a web-based dashboard. It supports security frameworks such as ISO 27001, NIST, and CIS Controls.

The tool is intended as a learning project and portfolio project for cybersecurity and data analysis roles.

Key Features-
Control Library
The project uses a centralized control library stored in questions.xlsx which contains cybersecurity audit controls categorized by domain.
Each control includes:
-Domain
-Control Question
-Security Framework
-Control ID


Example:
Domain	Question	Framework	Control ID
Access Control	Is role-based access control implemented?	ISO 27001	A.9.1
Authentication	Is multi-factor authentication enabled?	CIS	CIS 6
Automated Audit Checklist Generation

The script export_to_excel.py automatically generates a structured audit checklist from the control library.
Generated file:
-audit_checklist.xlsx

Checklist columns:
S.No	Domain	Question	Framework	Control ID	Status	Evidence	Comments
Status Options

A dropdown is automatically added with:
-Pass
-Fail
-Not Tested

Color Indicators
Status	Color
Pass	Green
Fail	Red
Not Tested	Yellow
Compliance Scoring

The script audit_score.py calculates audit results based on the status of controls.

It calculates:
Total Controls
Passed Controls
Failed Controls
Compliance Percentage

Example output:
Audit Compliance Report
Total Controls: 45
Passed Controls: 30
Failed Controls: 10
Compliance Score: 66.7%

Results are exported to:
audit_report.xlsx

Interactive Audit Dashboard
The project includes a Streamlit-based dashboard for visualizing audit results.
File:
audit_dashboard.py

The dashboard allows users to upload the audit checklist and view analytics.

Dashboard Features
Overall Compliance Metrics
Total Controls
Passed Controls
Failed Controls
Compliance Percentage
Status Distribution

Visual distribution of:
Pass
Fail
Not Tested

Domain Compliance Analysis
Shows compliance percentage for each security domain.


Example:
Domain	Passed	Failed	Compliance %
Access Control	8	2	80%
Authentication	6	4	60%

Framework Coverage
Displays number of controls mapped to frameworks such as:
ISO 27001
NIST
CIS Controls
Failed Control Risk Analysis
Failed controls are categorized by risk level.

Example:
Domain	Question	Risk Level
Authentication	MFA not implemented	High
Backup	Backup restoration not tested	Medium

Domain Filtering
Users can filter controls by domain using a sidebar.
Export Data
Filtered audit results can be downloaded as CSV.

Technologies Used
Python
Pandas
OpenPyXL
Streamlit
Excel

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
Clone the repository
git clone https://github.com/Praneetha2114/cybersecurity-audit-tool.git

Navigate to the project folder:

cd cybersecurity-audit-tool
Install required packages
pip install pandas openpyxl streamlit
How to Use
Step 1: Prepare the Control Library
Edit questions.xlsx to define cybersecurity controls.

Columns required:
Domain | Question | Framework | Control ID

Step 2: Generate Audit Checklist
Run:
python export_to_excel.py

This creates:
audit_checklist.xlsx

Step 3: Conduct the Audit
Open audit_checklist.xlsx and update the Status column.
Options:
Pass
Fail
Not Tested

You can also record:
Evidence
Comments

Step 4: Calculate Compliance
Run:
python audit_score.py
This generates:
audit_report.xlsx

Step 5: Launch Dashboard
Run:
streamlit run audit_dashboard.py
The dashboard will open in your browser.
Upload:
audit_checklist.xlsx
to view audit analytics.

Example Use Cases
This tool can help demonstrate:
Cybersecurity audit automation
Compliance tracking
Risk analysis
Security control monitoring
Security dashboard visualization
Future Improvements
Possible future enhancements:
PDF audit report generation
User authentication for auditors
Cloud security control analysis
Audit maturity scoring
Integration with vulnerability scanners
Multi-company audit tracking


Author
Praneetha

GitHub Profile:
https://github.com/Praneetha2114

License
This project is for educational and portfolio purposes.
