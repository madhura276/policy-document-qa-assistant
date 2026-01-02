"""
Assisto Technologies - LLM Assignment
Task: Policy Document Q&A Assistant (Dataset-based)
"""

from transformers import pipeline
from dataset_loader import load_policy_dataset

# -------------------------------
# Load LLM for Question Answering
# -------------------------------
qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad",
    framework="pt"
)

def displayInformation(question, answer):
    """
    Step 5: Display final answer
    """
    print("\nQuestion:")
    print(question)
    print("\nAnswer:")
    print(answer)

if __name__ == "__main__":

    # Step 1: Parse dataset
    context = load_policy_dataset("policy_qa_dataset_100_records.csv")

    # Step 2: User asks a question
    question = input("Ask a question about the insurance policy: ")

    # Steps 3 & 4 handled by LLM
    result = qa_pipeline(
        question=question,
        context=context
    )

    # Step 5: Display answer
    displayInformation(question, result["answer"])
