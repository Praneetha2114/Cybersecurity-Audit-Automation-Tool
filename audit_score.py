import pandas as pd

# Load audit checklist
df = pd.read_excel("audit_checklist.xlsx")

# Clean status column
df["Status"] = df["Status"].fillna("").astype(str)

# Overall metrics
total = len(df)
passed = len(df[df["Status"].str.lower() == "pass"])
failed = len(df[df["Status"].str.lower() == "fail"])
score = (passed / total) * 100 if total > 0 else 0

print("\nOverall Audit Compliance Report\n")
print(f"Total Controls: {total}")
print(f"Passed Controls: {passed}")
print(f"Failed Controls: {failed}")
print(f"Compliance Score: {score:.2f}%")

# Domain-wise report
domain_report = []

for domain, group in df.groupby("Domain"):
    
    total_controls = len(group)
    pass_controls = len(group[group["Status"].str.lower() == "pass"])
    fail_controls = len(group[group["Status"].str.lower() == "fail"])
    
    domain_score = (pass_controls / total_controls) * 100 if total_controls > 0 else 0
    
    domain_report.append({
        "Domain": domain,
        "Total Controls": total_controls,
        "Passed": pass_controls,
        "Failed": fail_controls,
        "Compliance %": f"{domain_score:.2f}%"
    })

domain_df = pd.DataFrame(domain_report)

# Save report
with pd.ExcelWriter("audit_report.xlsx") as writer:
    domain_df.to_excel(writer, sheet_name="Domain Summary", index=False)

print("\nDomain-wise report saved as audit_report.xlsx")