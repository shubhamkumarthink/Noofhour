import streamlit as st
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from datetime import time
from datetime import datetime, timedelta


st.title("Total no. of hour ")
st.header("This website give total no. of hour of weather condition for selected range of hour")
st.subheader("Upload CSV file ")

uploaded_file = st.file_uploader("Choose a csv file", type='csv')
#data = pd.read_csv(uploaded_file, skiprows = 11)
data2 = pd.read_csv(uploaded_file)
data1 = data2.dropna().reset_index(drop=True)
data0 = data1.rename(columns=data1.iloc[0]).drop(data1.index[0]).reset_index(drop=True)
data = data0.apply(lambda x: pd.to_numeric(x, errors='coerce'))
st.dataframe(data)

# minhour = st.number_input("Enter min value of hour of range (from 0 to 23): ", value=None, min_value=0, max_value=23, placeholder="Type a number...")
# maxhour = st.number_input("Enter max value of hour of range (upto 23): ", value=None, min_value=0, max_value=23, placeholder="Type a number...")

appointment = st.slider(
    "Select the range of hour:",
    value=(time(9), time(18)), step=timedelta(hours=1))
start_time, end_time = appointment

minhour = start_time.hour
maxhour = end_time.hour

x = st.number_input("Enter min value of temperature of range: ", value=None, min_value= -100, max_value= 100, placeholder="Type a number...")
y1 = st.number_input("Enter max value of temperature of range in integer: ", value=None, min_value= x, max_value= 100, placeholder="Type a number...")


button0 = st.button("Visualize")
if button0:
    results = {'Temperature': [], 'Count': []}
    y = 1 + y1
    for i in range(x, y):
        mintemp = (i - 0.5)
        maxtemp = (i + 0.5)
        df1 = data.loc[(data['HR'] >= minhour) & (data['HR'] <= maxhour) & (data['T2M'] > mintemp) & (data['T2M'] <= maxtemp)]
        results['Temperature'].append(i)
        results['Count'].append(len(df1))

    result_df = pd.DataFrame(results)
    st.dataframe(result_df)
    t = result_df['Temperature']
    v = result_df['Count']



    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(t, v, lw=4)
    ax.set_xlabel('Temperature in °C', fontsize=14)
    ax.set_ylabel('No. of hour in HR range', fontsize=14)
    ax.set_title('Temperature Vs No. of Hour', fontsize=20)
    st.pyplot(fig)

