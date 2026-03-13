import pandas as pd

def load_questions():
    df = pd.read_excel("questions.xlsx")
    return df

def generate_audit(domain=None):

    df = load_questions()

    if domain:
        df = df[df["Domain"].str.lower() == domain.lower()]

    if "S.No" in df.columns:
        df = df.drop(columns=["S.No"])

    df = df.sort_values(by="Domain")
    df.reset_index(drop=True, inplace=True)

    df.insert(0, "S.No", range(1, len(df) + 1))

    df["Status"] = ""
    df["Evidence"] = ""
    df["Comments"] = ""

    df.to_excel("audit_checklist.xlsx", index=False)

    print("Audit checklist created successfully!")

def main():

    print("\nCybersecurity Audit Tool\n")
    print("1 Generate full audit checklist")
    print("2 Generate domain-specific checklist")

    choice = input("\nSelect option: ")

    if choice == "1":
        generate_audit()

    elif choice == "2":
        domain = input("Enter domain name: ")
        generate_audit(domain)

    else:
        print("Invalid option")

if __name__ == "__main__":
    main()