# 📘 Assisto Technologies – LLM Assignment
Task Selected: Policy Document Q&A Assistant

## 📌 Problem Statement

Insurance policy documents are often lengthy and difficult to understand.
Customers usually want quick answers to specific questions instead of reading
the entire document.

This project implements a Policy Document Q&A Assistant that allows users to
ask questions about insurance policies and receive clear, simplified answers
using a semantic Large Language Model (LLM).

## 📂 Dataset Used

A small CSV dataset is used as the knowledge base for this system.

Dataset file: policy_qa_dataset_5_records.csv

Each record represents a key insurance policy section such as:

1. Liability Coverage
2. Collision Coverage
3. Comprehensive Coverage
4. Personal Injury Protection
5. Uninsured Motorist Coverage

The policy text from the dataset is combined and provided as context to the LLM
for question answering.

## 🧠 Approach (Step-by-Step)

The system follows the logical steps outlined in the assignment:

**1. Parse Policy Data**
The policy dataset is loaded from a CSV file.
All policy sections are combined into a single context.

**2. Semantic Search**
When a user asks a question, the LLM semantically searches the policy text
to find the most relevant information.
This is not keyword matching; meaning and intent are understood.

**3. Coverage Understanding & Classification**
The LLM understands which type of coverage the question refers to
(e.g., liability, collision, comprehensive).

**4. Summarization**
The LLM generates a short, user-friendly explanation instead of returning
raw policy text.

**5. Display Answer**
The final answer is displayed to the user in simple language.

## 🤖 LLM Usage (IMPORTANT)

A transformer-based Large Language Model is used for:

1. Semantic understanding of user questions
2. Searching relevant policy sections
3. Interpreting coverage context
4. Generating simplified answers

**LLM is used here:**

- Question Answering pipeline (transformers)
- Semantic reasoning instead of rule-based logic
- This allows the system to answer questions even when wording differs from the
dataset text.

## ❓ Types of Questions Users Can Ask

The system supports natural language questions such as:

**Example Questions**

- What does liability coverage cover?
- What happens if my vehicle is damaged in an accident?
- Does this policy cover theft or fire damage?
- Does the policy cover medical expenses after an accident?
- What if I am hit by an uninsured driver?

These questions are answered using semantic LLM reasoning, not exact keyword
matching.

## 🛠 Technologies Used

- Python 3.10
- HuggingFace Transformers
- PyTorch
- Pandas
- Semantic Question Answering (LLM-based NLP)

## 📁 Project Structure
policy_document_qa_dataset/
├── app.py
├── dataset_loader.py
├── policy_qa_dataset_5_records.csv
├── requirements.txt
└── README.md

## ▶️ How to Run

**1. Install dependencies:**

pip install -r requirements.txt

**2. Run the application:**

python app.py
3. Enter a question when prompted.

## ✅ Summary

This project demonstrates how Large Language Models can be used to build a
semantic Question & Answer system for insurance policy documents. By leveraging
LLM-based understanding and summarization, users can quickly understand policy
coverage without reading complex documents.