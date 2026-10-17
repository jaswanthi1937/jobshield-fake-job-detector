
import os
import re
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
)

DATA_PATH = "data/fake_job_postings.csv"
MODEL_PATH = "models/fraud_detector.joblib"

print("Loading dataset...")
df = pd.read_csv(DATA_PATH)

# Combine useful text fields into one input.
text_columns = [
    "title",
    "company_profile",
    "description",
    "requirements",
    "benefits",
]

for col in text_columns:
    if col not in df.columns:
        df[col] = ""

df[text_columns] = df[text_columns].fillna("")

df["job_text"] = df[text_columns].agg(" ".join, axis=1)
df["job_text"] = df["job_text"].str.replace(r"\s+", " ", regex=True).str.strip()

# Remove rows without useful text and validate labels.
df = df[df["job_text"].str.len() > 0].copy()
df = df[df["fraudulent"].isin([0, 1])].copy()
df["fraudulent"] = df["fraudulent"].astype(int)

X = df["job_text"]
y = df["fraudulent"]

print("Usable postings:", len(df))
print("Class counts:")
print(y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

# TF-IDF converts text into numerical features.
# Logistic Regression learns to classify the postings.
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            stop_words="english",
            max_features=50000,
            ngram_range=(1, 2),
            min_df=2,
            sublinear_tf=True,
        ),
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42,
        ),
    ),
])

print("\nTraining model...")
model.fit(X_train, y_train)

print("\nEvaluating on held-out test data...")
predictions = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, predictions):.4f}")
print("\nClassification report:")
print(classification_report(
    y_test,
    predictions,
    target_names=["Real", "Fraudulent"],
    zero_division=0,
))

print("Confusion matrix (rows=actual, columns=predicted):")
print(confusion_matrix(y_test, predictions))

os.makedirs("models", exist_ok=True)
joblib.dump(model, MODEL_PATH)

print(f"\nModel saved to: {MODEL_PATH}")
print("Training complete!")
