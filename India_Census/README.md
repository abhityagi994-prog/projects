# India Census Data Visualization (Streamlit + Plotly)

## Overview
A lightweight interactive web application built with **Streamlit** to visualize **India Census 2011** indicators on a geographic map. Users can select a **state** (or view **Overall India**) and choose two parameters to explore:

- **Primary parameter** → encoded as **bubble size**
- **Secondary parameter** → encoded as **bubble color**

The app renders an interactive **Plotly Scatter Mapbox** plot, allowing users to inspect districts via hover tooltips.

---

## Features
- State-level filtering (Overall India + individual states)
- Selectable primary and secondary parameters
- Interactive map with zoom/pan and hover details (State + District)
- Visual encoding:
  - **Size** = primary metric
  - **Color** = secondary metric

---

## Parameters Available
The app supports the following indicators:
- `Population`
- `Households_with_Internet`
- `Households_with_Electric_Lighting`
- `Sex Ratio`
- `Literacy Rate`

> Note: Sex Ratio is treated as **females per 1000 males**.

---

## Tech Stack
- **Python**
- **Streamlit** (web UI)
- **Plotly Express** (`scatter_mapbox`)
- **Pandas / NumPy** (data handling)

---

## Project Structure
```
India_Census/
│
├── app.py
├── data/
│ └── india_census_2011.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup & Run Locally

### 1) Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```
### 2) Create and activate a virtual environment
```bash
python -m venv .venv
```
**Windows**
```bash
.venv\Scripts\activate
```
**macOS/Linux**
```bash
source .venv/bin/activate
```
### 3) Install dependencies
```bash
pip install -r requirements.txt
```
### 4) Run the Streamlit app
```bash
streamlit run app.py
```
## Data Source
The application uses a dataset file: `data/india_census_2011.csv`
The dataset is expected to include at minimum:

- State name, District name

- Latitude, Longitude

All selected parameter columns listed above

## How It Works (High Level)

1) Load census dataset from CSV

2) User selects:
   - State (Overall India or a specific state)
   - Primary parameter (bubble size)
   - Secondary parameter (bubble color)

3) App filters data if a specific state is selected

4) Plotly renders a `scatter_mapbox` visualization with hover tooltips

## Future Improvements

- Add a district search
- Add summary KPIs (min/max/avg of selected metrics)
- Add a toggle for log scaling for Population (otherwise size can dominate)
- Improve zoom behavior for state-level view
- Add data validation / missing value handling

