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

The model was trained on a fake job postings dataset using TF-IDF text features and Logistic Regression.

Model evaluation should consider:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

These metrics help evaluate how well the classifier distinguishes fraudulent postings from legitimate ones. Accuracy alone may not reflect performance on an imbalanced dataset.

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
