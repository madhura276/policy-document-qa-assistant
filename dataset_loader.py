import pandas as pd

def load_policy_dataset(csv_path):

    df = pd.read_csv("policy_qa_dataset.csv")

    # Combine all policy text into a single context
    context = " ".join(df["policy_text"].tolist())

    return context
