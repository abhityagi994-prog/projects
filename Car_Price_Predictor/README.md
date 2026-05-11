# Car Price Prediction System

## Overview
This project is a **Car Price Prediction System** built using **Supervised Machine Learning (Regression)** and deployed using a **Flask web application**.

The system predicts the **estimated selling price of a car** based on user inputs such as company, model, year, fuel type, and kilometers driven.

---

## Problem Statement
Used car pricing is often inconsistent and subjective.  

The goal of this project is to build a machine learning model that:
- Learns patterns from historical car data
- Predicts car prices based on features
- Provides a quick and reliable estimate

---

## Type of Learning
This is a **Supervised Learning (Regression)** problem.

- Input → Car features  
- Output → Predicted price (continuous value)

---

## Features Used

- **Car Name**
- **Company**
- **Year**
- **Kilometers Driven**
- **Fuel Type**

---

## Project Workflow

### 1. Data Collection
- Dataset containing used car listings

---

### 2. Data Cleaning
- Removed missing values
- Cleaned inconsistent entries
- Converted data types
- Filtered unrealistic values

---

### 3. Feature Engineering
- Selected relevant features
- Handled categorical variables
- Prepared dataset for modeling

---

### 4. Model Training
- Used **Linear Regression**
- Built pipeline for preprocessing + modeling
- Trained model on cleaned dataset

---

### 5. Model Evaluation

The model was evaluated using **R² Score**.

- Achieved approximately **0.76 R² score** on test data  
- Performance varied across different train-test splits (up to ~0.92), indicating sensitivity to data splitting  

> Note: The reliable performance is considered around **0.76**, while higher scores were observed under specific random splits.

---

### 6. Model Saving
- Saved trained model using **pickle**
- Used for real-time predictions in the Flask app

---

### 7. Deployment (Flask App)
- Built a web interface for user input
- Takes car details from form
- Predicts price dynamically

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML / CSS
- Pickle

---

## Repository Structure

```markdown
Car_Price_Predictor/
│
├── application.py
├── LinearRegressionModel.pkl
├── Cleaned_Car_data.csv
├── quikr_car.csv
│
├── Quikr Analysis.ipynb
│
├── demo.png
├── predict.png
│
├── requirements.txt
├── README.md
```

---

## How It Works

- User enters car details in the web form
- Input is converted into model-compatible format
- Trained model predicts price
- Result is displayed instantly

--- 

## Running the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
```

---

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

--- 

### 3️⃣ Run the Flask App
```bash
python application.py
```

--- 

## Key Learning Outcomes

- Built a regression model using Linear Regression
- Learned data cleaning and preprocessing techniques
- Implemented feature engineering for structured data
- Developed an end-to-end ML pipeline 
- Deployed ML model using Flask

--- 

## Limitations

- Linear model may not capture complex relationships
- Model performance depends on data quality
- Limited feature set
- No real-time data updates

---

## Future Improvements

- Use advanced models (Random Forest, XGBoost)
- Apply cross-validation for better evaluation
- Improve feature engineering
- Add input validation in UI
- Deploy application online
