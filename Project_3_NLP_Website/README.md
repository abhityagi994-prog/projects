# NLP Web Application using Flask & NLP Cloud API

A full-stack Natural Language Processing (NLP) web application built using Python, Flask, and NLP Cloud APIs. This project provides a simple web interface to perform core NLP tasks such as Named Entity Recognition, Language Detection, and Sentiment Analysis.

**This project demonstrates:**

- Backend development with Flask
- API integration with real-world NLP services
- Clean project structuring
- Deployment-ready design

## Features

- Named Entity Recognition (NER)
- Language Detection
- Sentiment Analysis
- Web Interface using Flask
- Real-time API inference using NLP Cloud
- Modular and scalable project structure

## Tech Stack

- Backend: Python, Flask
- NLP API: NLP Cloud
- Frontend: HTML, CSS (Flask Templates)
- Deployment Ready: Compatible with GitHub & cloud platforms

## 📂Project Structure
```markdown
Project_1_NLP/
│
├── apps/                 # Future app modules 
├── model/                # Saved ML/NLP models
├── resources/            # Images, assets, extra files
├── script/               # Core application logic
│   ├── app.py            # Main Flask application
│   ├── mydatabase.py    # Database handling
│   ├── db.json           # User/database storage
│
├── templates/            # HTML templates (Flask frontend)
│
├── src/                  # Utility/helper scripts
│
├── .gitignore            # Git ignore rules
├── requirements.txt     # Project dependencies
└── README.md             # Project documentation
```

## Setup & Installation
### Install Dependencies
```
pip install nlpcloud
```

## Add Your NLP Cloud API Key
Inside app.py, replace:

```markdown
client = nlpcloud.Client("model-name", "YOUR_API_KEY", gpu=False)
```
with your actual model and API key

## Run the Application
From the Project root:
```bash
python app.py
```

## NLP Functionalities
**Named Entity Recognition (NER)**
- Extracts entities from text

**Supports specific entity filtering**
- Language Detection

**Detects the language of user-entered text**
- Sentiment Analysis
- Identifies sentiment polarity (positive/negative)

### Future Enhancements

User Authentication

Database Integration

Multiple Model Support

Docker Deployment

CI/CD Pipeline

