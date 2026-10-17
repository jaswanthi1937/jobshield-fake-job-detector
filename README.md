
# JobShield — Fake Job Posting Detector

JobShield is a machine-learning application that screens job postings for patterns associated with fraudulent listings. Users can enter job details and receive a model prediction and estimated fraud score through a Streamlit interface.

## Features

- Analyze job titles and descriptions
- Include optional company profiles, requirements, and benefits
- Display a fraud score and model classification
- Provide practical job-verification guidance
- Simple, interactive Streamlit interface

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF text vectorization
- Logistic Regression
- Streamlit
- Joblib

## Project Structure

    fake-job/
    ├── data/
    │   └── fake_job_postings.csv
    ├── models/
    │   └── fraud_detector.joblib
    ├── app.py
    ├── train_model.py
    ├── check_data.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## Getting Started

### 1. Clone the repository

    git clone YOUR_GITHUB_REPOSITORY_URL
    cd fake-job

### 2. Create a virtual environment

    python -m venv .venv

### 3. Activate the environment on Windows

    .venv\Scripts\activate

### 4. Install dependencies

    pip install -r requirements.txt

### 5. Train the model

    python train_model.py

### 6. Launch the application

    python -m streamlit run app.py

Open the local URL shown in your terminal.

## Model Evaluation

The model training script reports evaluation metrics, including accuracy, precision, recall, F1-score, and a confusion matrix.

Actual performance depends on the dataset, train/test split, and model configuration. Review the evaluation results before making performance claims.

## Limitations

- Predictions can be incorrect.
- The fraud score is a model estimate, not a verified probability that a posting is fraudulent.
- JobShield does not independently verify companies or job offers.
- Always check employers through official sources.

## Disclaimer

This project is an educational machine-learning screening tool. It should not be used as the sole basis for deciding whether a job offer is genuine.

## Author

Jaswanthi N
