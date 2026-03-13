import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cybersecurity Audit Dashboard", layout="wide")

st.title("Cybersecurity Audit Dashboard")

uploaded_file = st.file_uploader("Upload Audit Checklist", type=["xlsx"])

risk_levels = {
    "Authentication": "High",
    "Access Control": "High",
    "Data Protection": "High",
    "Monitoring": "Medium",
    "Backup & Recovery": "Medium",
    "Vulnerability Management": "High",
    "Incident Response": "Medium",
    "Governance": "Low",
    "Business Continuity": "Medium"
}

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    df["Status"] = df["Status"].fillna("Not Tested").astype(str)

    # DOMAIN FILTER
    domains = ["All"] + sorted(df["Domain"].unique().tolist())
    selected_domain = st.sidebar.selectbox("Filter by Domain", domains)

    if selected_domain != "All":
        df = df[df["Domain"] == selected_domain]

    # METRICS
    total = len(df)
    passed = len(df[df["Status"].str.lower() == "pass"])
    failed = len(df[df["Status"].str.lower() == "fail"])
    not_tested = len(df[df["Status"].str.lower() == "not tested"])

    compliance = (passed / total) * 100 if total > 0 else 0

    st.subheader("Overall Compliance")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Controls", total)
    col2.metric("Passed", passed)
    col3.metric("Failed", failed)
    col4.metric("Compliance %", f"{compliance:.2f}%")

    st.write("Not Tested:", not_tested)

    # STATUS DISTRIBUTION PIE
    st.subheader("Control Status Distribution")

    status_counts = df["Status"].value_counts()

    st.bar_chart(status_counts)

    # DOMAIN ANALYSIS
    st.subheader("Domain Compliance")

    domain_summary = []

    for domain, group in df.groupby("Domain"):

        total_controls = len(group)
        pass_controls = len(group[group["Status"].str.lower() == "pass"])
        fail_controls = len(group[group["Status"].str.lower() == "fail"])

        score = (pass_controls / total_controls) * 100 if total_controls > 0 else 0

        domain_summary.append({
            "Domain": domain,
            "Passed": pass_controls,
            "Failed": fail_controls,
            "Compliance %": score
        })

    domain_df = pd.DataFrame(domain_summary)

    st.dataframe(domain_df)

    st.bar_chart(domain_df.set_index("Domain")[["Compliance %"]])

    # FRAMEWORK COVERAGE
    if "Framework" in df.columns:

        st.subheader("Framework Coverage")

        framework_summary = df.groupby("Framework").size().reset_index(name="Controls")

        st.dataframe(framework_summary)

        st.bar_chart(framework_summary.set_index("Framework"))

    # FAILED CONTROLS
    st.subheader("Failed Controls")

    failed_controls = df[df["Status"].str.lower() == "fail"].copy()

    failed_controls["Risk Level"] = failed_controls["Domain"].map(risk_levels)

    st.dataframe(failed_controls[["Domain", "Question", "Risk Level"]])

    # DOWNLOAD REPORT
    st.subheader("Download Filtered Data")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Audit Data",
        csv,
        "audit_results.csv",
        "text/csv"
    )