# Startup Funding Analysis (Streamlit)
A Streamlit dashboard to explore startup funding data by overall trends,startup, and investor. The app loads a cleaned dataset, parses dates, and provides interactive views including month-by-month funding, top investments, and category breakdowns.

## Features
### **Overall Analysis**
- Total amount invested (sum of Amount in USD)
- Maximum funding by startup
- Average investment amount
- Total funded startups (unique startups)
- Month-by-month trends:
  - Number of startups funded
  - Total amount funded
### Startup View
- Select a startup to see:
  - Industries associated with the startup
  - Sub-vertical categories
  - Locations (cities)
- Investor contribution split (pie chart)
### Investor View
- Select an investor to see:
  - Latest investments (last 5 by date)
  - Biggest investments (top 5)
  - Sector distribution (pie chart)
  - Investment type distribution (pie chart)

## Tech Stack
- Python
- Pandas
- NumPy
- Streamlit
- CSV based Startup Funding Dataset

## Project Structure
```markdown
Project_6_Startup_dashboard/
├── app.py
├── data/
│ └── startup_cleaned.csv
| └── startup_funding.csv
├── model/
├── resources/
├── src/
├── README.md
└── .gitignore
```

## Dataset
### Required Columns
- `Date`
- `startup`
- `Industry`
- `SubVertical`
- `city`
- `Investors`
- `Investment Type`
- `Amount in USD`

## Install dependencies
```
pip install streamlit pandas numpy matplotlib
```
## Run the application
```
streamlit run app.py
```

## Future Improvements

- Add year-wise and quarter-wise funding filters
- Introduce investor-wise comparison dashboards
- Add funding trend forecasting using time-series models
- Enable interactive visualizations using Plotly
- Add geographic analysis with city/state-level maps
- Deploy the application on cloud platforms (Render / AWS / Docker)
