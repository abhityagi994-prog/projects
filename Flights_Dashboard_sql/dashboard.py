import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db=DB()
st.sidebar.title('Flights Analytics')
user_opt=st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_opt=='Check Flights':
    st.title('Check Flights')
    col1,col2=st.columns(2)

    with col1:
        city=db.fetch_city()
        source=st.selectbox('Source',city)
    with col2:
        destination=st.selectbox('Destination',city)
    btn1=st.button('Search')
    if btn1:
        results=db.fetch_all_flights(source,destination)
        st.dataframe(results)
elif user_opt=='Analytics':
    st.text('Analytics')
    airlines,frequency=db.fetch_airlines()
    fig=go.Figure(
        go.Pie(
            labels=airlines,
            values=frequency,
            hoverinfo='label+percent',
            textinfo='value'
        ))
    st.header('Pie Chart')
    st.plotly_chart(fig)

    city, frequency = db.busy_airport()
    fig = px.bar(
        x=city,y=frequency
    )
    st.header('Bar Chart')
    st.plotly_chart(fig,theme='streamlit',use_container_width=True)

    data, frequency = db.daily_frequency()
    fig = px.line(
        x=data, y=frequency
    )
    st.header('Line Chart')
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

else:
    st.title('About the Dashboard')
    st.markdown("""
    This interactive **Flight Analytics Dashboard** is built using **Streamlit, MySQL, and Plotly** to explore and visualize flight data.

    The dashboard allows users to:
    - Search for available flights between selected source and destination cities.
    - Analyze airline distribution using interactive visualizations.
    - Identify the busiest airports based on flight frequency.
    - Observe daily flight trends through time-series analysis.

    The goal of this dashboard is to demonstrate how **SQL-backed data pipelines can be integrated with Python-based visualization tools to build interactive data applications**.
    """)

