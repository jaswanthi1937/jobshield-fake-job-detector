
import pandas as pd

df = pd.read_csv("data/fake_job_postings.csv")

print("Dataset shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst five rows:")
print(df.head())

print("\nFraudulent label counts:")
print(df["fraudulent"].value_counts())
