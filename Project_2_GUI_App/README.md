# NLP Desktop App (GUI Project)

A simple NLP Desktop Application built using **Python + Tkinter + NLPCloud API**.  
The app performs:

- **Language Detection**
- **Named Entity Recognition (NER)**
- **Sentiment Analysis**

This is an early-stage version of the project (MVP).  
More improvements will be added later (better UI, robust API parsing, improved error-handling, rate-limit handling, etc).

---

## Features

### 1. Language Detection
Uses the NLPCloud `python-langdetect` model to detect the primary language of user-entered text.

### 2. Named Entity Recognition (NER)
Extracts entities from a sentence such as:
- Person  
- Location  
- Organization  
- Dates  
- Numeric values  
and more.

### 3. Sentiment Analysis
Identifies the emotional tone of the text:
- Positive  
- Negative  
- Neutral  
(Also, Emotion labels like Joy, Anger, Fear depending on the model)

---

## 📂Project Structure

```markdown
Project_2_GUI/
│
├── apps/
│   └── (modules for GUI screens — optional placeholder)
│
├── models/
│   └── (future ML/NLP model modules)
│
├── notebooks/
│   └── (Jupyter notebooks used during testing)
│
├── resources/
│   └── (images, icons, assets)
│
├── src/
│   └── (core functions / utilities if needed)
│
├── app.py              # Main GUI application
├── mydatabase.py       # Database handling
├── db.json             # Saved user history
├── README.md
└── .gitignore

```
## Setup & Installation
### Install Dependencies
```bash
pip install nlpcloud tkinter
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
## Tech Stack

- Python 3.9+

- Tkinter

- NLPCloud Python Client

- JSON-based local storage (db.json)

- Custom modules under /apps, /models, /resources