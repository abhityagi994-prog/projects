# Stock Market Prediction and Sentiment Analysis using Machine Learning & Deep Learning

## Overview

This repository presents my MSc Business Analytics dissertation project focused on **Stock Market Forecasting using Financial Metrics and News Sentiment Analysis** within a structured **CRISP-DM framework**.

The project combines:
- Financial market indicators
- Natural Language Processing (NLP)
- Machine Learning
- Deep Learning
- Explainable AI (XAI)

to improve stock price movement prediction using both structured financial data and unstructured news sentiment data.

The research investigates whether integrating financial news sentiment with stock market indicators improves predictive performance compared to traditional forecasting approaches.

---

# Dissertation Details

- **Title:** Integrating Financial Metrics and News Sentiment for Stock Price Forecasting: A CRISP-DM Framework
- **Framework Used:** CRISP-DM
- **Research Focus:** Stock Forecasting using AI, NLP, and Sentiment Analysis

---

# Problem Statement

Traditional stock prediction approaches using only:
- Fundamental Analysis
- Technical Analysis

struggle to capture:
- market volatility
- real-time events
- investor sentiment
- nonlinear behavior in financial markets.

This project addresses that limitation by integrating:
- historical stock price data
- technical indicators
- financial news sentiment

using Machine Learning and Deep Learning techniques.

---

# Objectives

The main objectives of this research were:

- Integrate stock market data with financial news sentiment
- Compare Machine Learning and Deep Learning models
- Apply NLP techniques for sentiment extraction
- Evaluate forecasting performance using multiple metrics
- Implement a reproducible CRISP-DM pipeline
- Analyze feature importance using Explainable AI (SHAP)

---

# Dataset Sources

## Financial Data
- Yahoo Finance API (`yfinance`)
- S&P 500
- Apple (AAPL)
- Microsoft (MSFT)

## News Dataset
- Reddit News Dataset
- 73,608 news headlines
- Financial news filtered using keyword extraction

---

# Technologies Used

## Programming & Libraries
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow / Keras
- SHAP
- NLTK
- TextBlob
- VADER Sentiment

---

# Machine Learning & Deep Learning Models

The following models were implemented and compared:

## Machine Learning
- Gradient Boosting Classifier

## Deep Learning
- LSTM (Long Short-Term Memory)
- CNN-LSTM Hybrid Architecture

The study compares these models on:
- Accuracy
- F1-Score
- ROC-AUC

---

# NLP & Sentiment Analysis

The project uses:
- **VADER Sentiment Analysis**
- **TextBlob**

to extract:
- positive sentiment
- negative sentiment
- neutral sentiment
- compound sentiment scores

from financial news headlines.

The sentiment data was then integrated with stock market time-series data for forecasting.

---

# CRISP-DM Framework

This project follows the complete CRISP-DM lifecycle:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

The framework helps create a structured and reproducible workflow for financial forecasting projects.

---

# Exploratory Data Analysis (EDA)

The project includes:
- Sentiment distribution analysis
- Word cloud visualization
- Stock trend visualization
- Correlation heatmaps
- Moving average analysis
- RSI and MACD analysis

for:
- S&P 500
- Apple
- Microsoft

---

# Explainable AI (XAI)

To improve model interpretability, the project uses:

## SHAP (SHapley Additive Explanations)

SHAP was used to:
- identify important features
- explain prediction behavior
- analyze sentiment contribution
- interpret financial indicators

This helped understand how sentiment scores and technical indicators influence stock prediction outputs.

---

# Repository Structure
```markdown
stock_prediction_sentiment_analysis/
│
├── notebooks/
│   └── stock_prediction_sentiment_analysis.ipynb
│
├── datasets/
│   └── reddit_news.csv
│
├── report/
│   └── dissertation_report.pdf
│
├── README.md
├── requirements.txt
├── .gitignore
```

---

# Key Findings

- Integrating news sentiment improves stock forecasting performance.
- Gradient Boosting performed best for S&P 500 prediction.
- CNN-LSTM showed strong performance for individual stocks.
- Sentiment-related features significantly contributed to prediction accuracy.
- Deep learning models captured sequential dependencies effectively.

---

# Evaluation Metrics

The models were evaluated using:
- Accuracy
- F1-Score
- ROC-AUC
- Confusion Matrix

to compare forecasting performance across different stock datasets.

---

# Future Improvements

Potential future enhancements include:
- Real-time dashboard deployment
- Twitter and earnings-call sentiment integration
- FinBERT and transformer-based architectures
- Multi-country stock market analysis
- Advanced explainability techniques

---

# Learning Outcomes

Through this dissertation project, I gained hands-on experience in:

- Time Series Forecasting
- Natural Language Processing
- Sentiment Analysis
- Machine Learning & Deep Learning
- Explainable AI (XAI)
- Financial Data Analytics
- CRISP-DM Methodology
- Feature Engineering
- Model Evaluation & Interpretation

---

# Conclusion

This research demonstrates that integrating financial indicators with sentiment analysis can improve stock forecasting performance compared to traditional approaches.

The project also highlights the importance of:
- structured data mining workflows
- multi-source data integration
- explainable AI techniques
- hybrid ML/DL architectures

in solving complex financial prediction problems.