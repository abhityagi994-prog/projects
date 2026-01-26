import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

st.set_page_config(page_title='Startup Analysis')

df=pd.read_csv('data/startup_cleaned.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)

df['months'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

def load_investor_details(investor_name):
    st.header(investor_name)
    #Last 5 investors
    df_1 = df[df['Investors'].str.contains(investor_name)]
    resent_investment = df_1.sort_values(by='Date', ascending=False)[['Date','startup','Industry','city','Investors','Investment Type','Amount in USD']].head(5)
    st.subheader('Latest Investments')
    st.dataframe(resent_investment)

col1,col2=st.columns(2)


def load_biggest_investment(investor_name):
    #biggest investment
    invest=df[df['Investors'].str.contains(investor_name)]
    big = invest['Amount in USD'].max()
    biggest_investment = invest.sort_values('Amount in USD',ascending=False)[['startup','Amount in USD']].head(5)
    st.subheader('Biggest Investments in $')
    st.write(biggest_investment)
    st.write("Biggest Investment - ",big)
    column1,column2 = st.columns(2)
    with column1:
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(biggest_investment['startup'],biggest_investment['Amount in USD'])

        st.pyplot(fig)

    with column2:
        st.subheader('Sectors invested in')
        invest=df[df['Investors'].str.contains(investor_name)]
        pie_ = invest.groupby('Industry').size()
        fig1, ax1 = plt.subplots()
        ax1.pie(pie_,labels=pie_.index)

        st.pyplot(fig1)

    column3,column4=st.columns(2)
    with column3:
        st.subheader('Investment Type')
        invest = df[df['Investors'].str.contains(investor_name)]
        pie_ = invest.groupby('Investment Type').size()
        fig2, ax2 = plt.subplots()
        ax2.pie(pie_,labels=pie_.index)

        st.pyplot(fig2)

def load_amount_invested():
    st.title('Overall Analysis')
    st.subheader('Total Amount Invested')
    amount = df['Amount in USD'].sum()
    st.write('Amount in USD', amount)

def max_amount_invested():
    maximum = df.groupby('startup')['Amount in USD'].max().sort_values(ascending=False).head(1)
    st.subheader('Maximum Amount Invested by an Investor')
    st.write('Amount in USD',maximum)

def load_avg_amount_invested():
    st.subheader('Average Amount of Investment')
    avg_amount=df.groupby('startup')['Amount in USD'].sum().mean()
    st.write('Amount in USD',avg_amount)

def load_funded_startups():
    st.subheader('Total Funded Startups')
    counts=df['startup'].nunique()
    st.write('Total number of Startups',counts)

def mom_funding():
    st.header('Month by Month Data')

    choice = st.selectbox(
        'Select One',
        ['Number of Startups Funded', 'Total Amount Funded'],
        key='mom_choice'
    )
    if choice == 'Number of Startups Funded':
        temp = (df.groupby(['Year', 'months'])['startup']
                  .nunique()
                  .reset_index(name='value')
                  .sort_values(['Year', 'months']))
    else:
        temp = (df.groupby(['Year', 'months'])['Amount in USD']
                  .sum()
                  .reset_index(name='value')
                  .sort_values(['Year', 'months']))

    temp['x_axis'] = temp['Year'].astype(str) + '-' + temp['months'].astype(str).str.zfill(2)

    fig, ax = plt.subplots()
    ax.plot(temp['x_axis'], temp['value'])
    ax.set_xlabel('Year-Month')
    ax.set_ylabel('Count' if choice == 'Number of Startups Funded' else 'Amount in USD')
    plt.xticks(rotation=45, ha='right')

    st.pyplot(fig)

def load_company_details(names):
    st.header(names)
    df_1=df[df['startup'] == names]
    st.subheader('Type of Industries')
    result=df_1[['Industry']].dropna().reset_index(drop=True)
    result.index=result.index+1
    st.dataframe(result)
    st.subheader('Sub - Vertical Types')
    result_1=df_1[['SubVertical']].dropna().reset_index(drop=True)
    result_1.index=result_1.index+1
    st.dataframe(result_1)
    st.subheader('Location')
    result_2=df_1[['city']].reset_index(drop=True)
    result_2.index=result_2.index+1
    st.dataframe(result_2)

def investors_portion(names):
    st.subheader('Top Investors')
    temp_df = df[df['startup'] == names][['Investors', 'Amount in USD']]
    pie_=temp_df.groupby('Investors')['Amount in USD'].sum()
    fig2, ax2 = plt.subplots()
    ax2.pie(pie_, labels=pie_.index)

    st.pyplot(fig2)



st.sidebar.title('Startup Funding Analysis')
options=st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if options=='Overall Analysis':
    load_amount_invested()
    max_amount_invested()
    load_avg_amount_invested()
    load_funded_startups()
    mom_funding()


elif options=='Startup':
    st.title('Startup')
    company_name=st.sidebar.selectbox('Select One',sorted(pd.unique(df['startup'])))
    btn1=st.sidebar.button('Find Startup Details')
    if btn1:
        load_company_details(company_name)
        investors_portion(company_name)


else:
    st.title('Investor')
    inv = df['Investors'].str.split(',')
    name=st.sidebar.selectbox('Select One',sorted(inv.explode().unique()))
    btn2=st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(name)
        load_biggest_investment(name)



