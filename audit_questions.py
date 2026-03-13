import pandas as pd

def load_questions():
    df = pd.read_excel("questions.xlsx", sheet_name="Questions")
    return df

def display_questions():
    questions = load_questions()

    print("\nCybersecurity Audit Questionnaire\n")

    for index, row in questions.iterrows():
        print(f"{row['S.No']}. {row['Question']}")

if __name__ == "__main__":
    display_questions()