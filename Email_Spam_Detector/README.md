# Email / SMS Spam Classifier

## Overview
This project is an **Email/SMS Spam Classification system** built using **Natural Language Processing (NLP)** and **Machine Learning**.

The project takes raw text messages as input, preprocesses them using NLP techniques, converts them into numerical features using **TF-IDF Vectorization**, and predicts whether the message is **Spam** or **Not Spam**.

A simple **Streamlit web app** is also included to make the model interactive and easy to test.

---

## Problem Statement
Spam messages are a common issue in email and SMS communication. Manually filtering them is inefficient and unreliable.

The goal of this project is to build a machine learning model that can automatically classify incoming messages as:

- **Spam**
- **Not Spam (Ham)**

---

## Project Workflow

### 1. Data Cleaning
- Loaded the dataset
- Removed unnecessary columns
- Renamed columns for clarity
- Encoded target labels
- Checked and removed duplicate records
- Verified missing values

### 2. Exploratory Data Analysis (EDA)
- Class distribution analysis
- Message length analysis
- Number of words and sentences
- Correlation analysis
- Pairplots and visual comparisons
- WordCloud generation for spam and ham messages
- Most common words analysis

### 3. Text Preprocessing
Text preprocessing was performed before model training using the following steps:

- Convert text to lowercase
- Tokenization
- Remove special characters
- Remove stopwords
- Remove punctuation
- Apply stemming using **Porter Stemmer**

### 4. Feature Engineering
- Converted cleaned text into numerical features using **TF-IDF Vectorizer**

### 5. Model Building
Multiple classification algorithms were tested and compared, including:

- Gaussian Naive Bayes
- Multinomial Naive Bayes
- Bernoulli Naive Bayes
- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- Extra Trees
- AdaBoost
- Bagging
- Gradient Boosting
- XGBoost
- Voting Classifier
- Stacking Classifier

### 6. Model Evaluation
Models were evaluated using:
- Accuracy Score
- Precision Score

The final deployed model uses:
- **TF-IDF Vectorizer**
- **Multinomial Naive Bayes** 

---

## Streamlit App
The project includes a **Streamlit-based web application** where users can enter an email or SMS message and instantly get a prediction.

### App Features
- User-friendly text input
- Real-time prediction
- NLP preprocessing pipeline
- Spam / Not Spam output

---

## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- Scikit-learn
- Streamlit
- Pickle

---

## Project Structure

```markdown
Email_Spam_Detector/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── spam_detector.ipynb
├── spam.csv
├── spam_utf8.csv
├── README.md
│     
└── .gitignore    
```
---
## How It Works
### Text Preprocessing Function

The input message is transformed through:

- lowercase conversion
- tokenization
- alphanumeric filtering
- stopword removal
- punctuation removal
- stemming

### Prediction Pipeline

- User enters message in Streamlit app
- Message is preprocessed
- TF-IDF vectorizer transforms text into features
- Trained model predicts class
- App displays:
- Spam
- Not Spam

--- 
## Installation and Setup
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/email-spam-detector.git
cd email-spam-detector
```

--- 

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

---

### 3. Activate Virtual Environment
```bash
.venv\Scripts\activate
```

--- 

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 5. Download NLTK Resources
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

### 6. Run the Streamlit App
```bash
streamlit run app.py
```

--- 

## Example Usage
Enter a message such as:
```
Congratulations! You have won a free prize. Call now to claim.
```
Output:
```
spam
```

--- 

## Key Learning Outcomes

Through this project, I learned:

- How to clean and preprocess text data
- How TF-IDF works in text classification
- How to build and compare multiple classification models
- How to evaluate NLP models using accuracy and precision
- How to save trained ML models using pickle
- How to deploy a machine learning model with Streamlit

--- 

## Future Improvements

- Add recall, F1-score, and ROC-AUC for deeper evaluation
- Improve preprocessing pipeline
- Use cross-validation for more robust model comparison
- Add confusion matrix visualization in the app
- Deploy the application online
- Replace pickle with joblib for model persistence
- Add better UI styling and input examples in Streamlit

