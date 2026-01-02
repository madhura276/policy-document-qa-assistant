from transformers import pipeline

# Load LLM once
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def classify_coverage_llm(text):
    labels = ["liability", "collision", "comprehensive"]
    result = classifier(text, labels)
    return result["labels"][0]

def summarize_text_llm(text):
    summary = summarizer(text, max_length=60, min_length=25, do_sample=False)
    return summary[0]["summary_text"]
