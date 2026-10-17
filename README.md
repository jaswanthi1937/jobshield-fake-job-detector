# 🛡️ JobShield — Fake Job Posting Detector

An AI/ML-powered web application that analyzes job postings and identifies patterns associated with potentially fraudulent listings. JobShield provides a model-generated fraud score and practical safety guidance to help users evaluate job opportunities.

🌐 **Live Demo:** [Try JobShield](https://jobshield-fake-job-detector.streamlit.app/)

💻 **GitHub Repository:** [View Source Code](https://github.com/jaswanthi1937/jobshield-fake-job-detector)

## ✨ Features

- Analyze job titles and descriptions.
- Include company names and company profiles.
- Evaluate job requirements and benefits.
- Display a model-generated fraud score and classification.
- Highlight common job scam warning signs.
- Provide practical job verification guidance.
- Interactive web interface built with Streamlit.

## 🧰 Technologies Used

- **Python** — application development
- **Pandas** — data handling and preprocessing
- **Scikit-learn** — machine learning
- **TF-IDF Vectorization** — text feature extraction
- **Logistic Regression** — classification model
- **Streamlit** — interactive web application
- **Joblib** — model serialization and loading

## ⚙️ How It Works

1. **Input:** The user enters available job posting details.
2. **Preprocessing:** The text is prepared for machine learning.
3. **Feature extraction:** TF-IDF converts text into numerical features.
4. **Prediction:** A trained Logistic Regression model analyzes the features.
5. **Results:** The application displays an estimated fraud score and classification.
6. **Verification:** The user receives practical safety guidance before applying.

## 🏗️ Project Structure

```text
jobshield-fake-job-detector/
├── app.py
├── train_model.py
├── check_data.py
├── requirements.txt
├── README.md
├── data/
│   └── fake_job_postings.csv
└── models/
    └── fraud_detector.joblib
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/jaswanthi1937/jobshield-fake-job-detector.git
cd jobshield-fake-job-detector
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## 📊 Model Evaluation

JobShield uses TF-IDF text features and a Logistic Regression classifier to identify potentially fraudulent job postings.

### Performance Metrics

Evaluation on the test set produced the following results:

| Metric | Score |
|---|---:|
| Accuracy | 98.63% |
| Precision (Fraud) | 82.63% |
| Recall (Fraud) | 90.75% |
| F1-score (Fraud) | 86.50% |

### Confusion Matrix

The confusion matrix contains 3,576 test samples.

| | Predicted Legitimate | Predicted Fraud |
|---|---:|---:|
| Actual Legitimate | 3,370 | 33 |
| Actual Fraud | 16 | 157 |

- **True Negatives (TN):** 3,370
- **False Positives (FP):** 33
- **False Negatives (FN):** 16
- **True Positives (TP):** 157

### Interpretation

- **Accuracy:** 98.63% of test predictions were correct.
- **Precision:** 82.63% of postings predicted as fraudulent were actually fraudulent.
- **Recall:** 90.75% of fraudulent postings in the test set were detected.
- **F1-score:** 86.50%, balancing precision and recall.

Accuracy should be interpreted alongside precision and recall, especially when the dataset contains more legitimate postings than fraudulent postings.

*Note: These figures assume the confusion matrix uses the class order `[legitimate, fraud]` for both actual and predicted labels. Results reflect the test dataset and do not guarantee performance on new job postings.*

## 🔒 Limitations and Responsible Use

- A low fraud score does not guarantee that a job posting is genuine.
- A high score does not prove that a posting is fraudulent.
- Predictions depend on the training data and the information entered.
- Always verify employers through official websites and trusted contact details.
- Never pay upfront recruitment fees or share sensitive information with unverified recruiters.

**JobShield is an educational screening aid, not a guarantee of job legitimacy.**

## 👩‍💻 Author

**Jaswanthi N.**

B.Tech — Computer Science and Engineering (AI/ML)

Interested in Artificial Intelligence, Machine Learning, and building practical AI-powered applications.

---

⭐ If you find this project interesting, feel free to explore the repository and try the live demo.
