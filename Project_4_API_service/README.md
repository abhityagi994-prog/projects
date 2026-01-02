# IPL Analytics REST API (Flask)

A RESTful API built using **Flask** that provides analytical insights from the **Indian Premier League (IPL)** dataset.  
This project exposes multiple endpoints to fetch team-level and player-level statistics such as head-to-head records, team performance, batting records, and bowling records.

The project focuses on **backend API design**, **data analysis using Pandas**, and **clean separation of concerns**.

---

## Features

- List all IPL teams
- Team vs Team (Head-to-Head) statistics
- Team performance summary
- Batsman career statistics
- Bowler career statistics
- JSON-based REST API responses

---

## Tech Stack

- **Python**
- **Flask**
- **Pandas**
- **NumPy**
- CSV-based IPL dataset

---

## Project Structure
```markdown
Project_4_API_service/
│
├── .idea/ # PyCharm project settings
├── .venv/ # Virtual environment (ignored in Git)
├── pycache/ # Python cache files
├── apps/ # (future extension)
├── model/ # (future extension)
├── resources/ # Dataset / static resources
├── src/ # Source-level logic (if extended)
│
├── app.py # Main Flask application
├── ipl.py # IPL dataset loading & core analytics
├── api_functions.py # Team, batsman & bowler API logic
└── README.md
```
### Install dependencies
```
pip install flask pandas numpy
```

### Run the Flask server
```
python app.py
```

## API Endpoints
### Home

```
GET/
```
### Response
```
Welcome to IPL World
```

## Design Notes

- All API responses are JSON-serializable

- Pandas & NumPy objects are converted to native Python types before returning

- Modular structure:

    - app.py → routing & API endpoints

    - ipl.py → dataset handling & team analytics

    - api_functions.py → player-level analytics

## Future Improvements

- Add season-wise filters

- Add IPL points table endpoint

- Add caching for faster API responses

- Deploy on cloud (Render / AWS / Docker)