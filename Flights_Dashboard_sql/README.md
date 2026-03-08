# ✈️ Flight Analytics Dashboard

An interactive **Flight Analytics Dashboard** built using **Streamlit, MySQL, and Plotly** to explore flight routes, analyze airline distribution, and visualize airport activity.  
This project demonstrates how **SQL-backed data retrieval can be combined with Python-based visualization tools to build an interactive data application.**

---

# 🚀 Project Overview

The **Flight Analytics Dashboard** allows users to:

- 🔎 Search for available flights between selected **source and destination cities**
- 📊 Analyze **airline market share** using interactive pie charts
- 🏙 Identify the **busiest airports** based on flight frequency
- 📈 Explore **daily flight trends** through time-series visualizations

The application connects to a **MySQL database**, retrieves flight data dynamically, and displays insights through **interactive visualizations powered by Plotly**.

---

# 🛠 Tech Stack

| Technology | Purpose |
|-----------|--------|
| **Python** | Core programming language |
| **Streamlit** | Building the interactive web dashboard |
| **MySQL** | Storing and querying flight data |
| **Plotly** | Interactive data visualization |
| **Pandas** | Data manipulation and handling |
| **SQLAlchemy / MySQL Connector** | Database connectivity |

---

# 📊 Dashboard Features

## 1️⃣ Flight Search
Users can search for flights between two cities.

Features:
- Select **Source City**
- Select **Destination City**
- View available flights with details including:
  - Airline
  - Route
  - Departure Time
  - Duration
  - Price

---

## 2️⃣ Airline Distribution
A **Pie Chart visualization** shows the distribution of flights by airline, helping identify which airlines dominate the market.

---

## 3️⃣ Busiest Airports
A **Bar Chart** highlights the airports with the highest number of flights, allowing users to understand airport traffic patterns.

---

## 4️⃣ Daily Flight Trends
A **Line Chart** visualizes how flight frequency changes over time, helping reveal temporal patterns in flight activity.

---

# 📂 Project Structure
```markdown
Flights_Dashboard_sql/
│
├── dashboard.py # Main Streamlit dashboard
├── dbhelper.py # Database connection and query functions
├── .gitignore # files need to be ignored
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```


---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Flights_Dashboard_sql.git
cd Flights_Dashboard_sql
```
---
##  ️2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
---
## 3️⃣ Setup MySQL Database
Create a MySQL database and import the dataset.
Example:
```
CREATE DATABASE flights_db;
USE flights_db;
```
---
## 4️⃣ Configure Database Connection
Update database credentials inside dbhelper.py:
```
mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="flights_db"
)
```
---
## ▶️ Run the Dashboard
Start the Streamlit application:
```
Start the Streamlit application:
```
## 📈 Example Use Cases

This dashboard can be used to:

- Analyze flight route availability
- Understand airline market distribution
- Identify high-traffic airports
- Explore temporal flight patterns

## 🔮 Future Improvements

Possible enhancements for the project:

- Add flight price trend analysis
- Implement date-based filtering
- Add map visualizations for flight routes
- Include machine learning models for price prediction
- Deploy the dashboard using Streamlit Cloud / Docker