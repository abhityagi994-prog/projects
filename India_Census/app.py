import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title='India Census',layout='wide')
df=pd.read_csv('data/india_census_2011.csv')
print(df.head())

temp=['Population','Households_with_Internet', 'Housholds_with_Electric_Lighting','Sex Ratio', 'Literacy Rate']

st.header('India Census')
st.sidebar.header('India Data Viz')
list_of_states=list(df['State name'].unique())
list_of_states.insert(0,'Overall India')

sel1=st.sidebar.selectbox('Select a State',list_of_states)
primary=st.sidebar.selectbox('Select Primary Parameter',temp)
secondary=st.sidebar.selectbox('Select Secondary Parameter',temp)

btn1=st.sidebar.button('Plot Graph')

if btn1:
    if sel1=='Overall India':
        st.subheader('Size represents primary parameter')
        st.subheader('Colour represents secondary parameter')
        fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',color=secondary,hover_data=['State name','District name'],zoom=3,
                           size=primary,mapbox_style='carto-positron')
        st.plotly_chart(fig)
    else:
        st.subheader('Size represents primary parameter')
        st.subheader('Colour represents secondary parameter')
        df_1=df[df['State name']==sel1]
        fig1=px.scatter_mapbox(df_1,lat='Latitude',lon='Longitude',size=primary,color=secondary,hover_data=['State name','District name'],zoom=3,
                            mapbox_style='carto-positron')
        st.plotly_chart(fig1)

