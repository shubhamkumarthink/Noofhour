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

x = st.number_input("Enter min value of temperature of range & Press Enter: ", value=None, min_value= -100, max_value= 100, placeholder="Type a number... & press enter.")
y1 = st.number_input("Enter max value of temperature of range & Press Enter: ", value=None, min_value= x, max_value= 100, placeholder="Type a number... & press enter.")


button0 = st.button("Visualize")
if button0:
    results = {'Temperature': [], 'Total no of hour': [],
               'No of hr in Humidity range (0-10)': [],
               'No of hr in Humidity range (10-20)': [],
               'No of hr in Humidity range (20-30)': [],
               'No of hr in Humidity range (30-40)': [],
               'No of hr in Humidity range (40-50)': [],
               'No of hr in Humidity range (50-60)': [],
               'No of hr in Humidity range (60-70)': [],
               'No of hr in Humidity range (70-80)': [],
               'No of hr in Humidity range (80-90)': [],
               'No of hr in Humidity range (90-100)': []}
    y = 1 + y1
    for i in range(x, y):
        mintemp = (i - 0.5)
        maxtemp = (i + 0.5)
        df1 = data.loc[(data['HR'] >= minhour) & (data['HR'] <= maxhour) & (data['T2M'] > mintemp) & (data['T2M'] <= maxtemp)]
        results['Temperature'].append(i)
        results['Total no of hour'].append(len(df1))
        df2 = df1.loc[(df1['RH2M'] > 0) & (df1['RH2M'] <= 10)]
        df3 = df1.loc[(df1['RH2M'] > 10) & (df1['RH2M'] <= 20)]
        df4 = df1.loc[(df1['RH2M'] > 20) & (df1['RH2M'] <= 30)]
        df5 = df1.loc[(df1['RH2M'] > 30) & (df1['RH2M'] <= 40)]
        df6 = df1.loc[(df1['RH2M'] > 40) & (df1['RH2M'] <= 50)]
        df7 = df1.loc[(df1['RH2M'] > 50) & (df1['RH2M'] <= 60)]
        df8 = df1.loc[(df1['RH2M'] > 60) & (df1['RH2M'] <= 70)]
        df9 = df1.loc[(df1['RH2M'] > 70) & (df1['RH2M'] <= 80)]
        df10 = df1.loc[(df1['RH2M'] > 80) & (df1['RH2M'] <= 90)]
        df11 = df1.loc[(df1['RH2M'] > 90) & (df1['RH2M'] <= 100)]
        results['No of hr in Humidity range (0-10)'].append(len(df2))
        results['No of hr in Humidity range (10-20)'].append(len(df3))
        results['No of hr in Humidity range (20-30)'].append(len(df4))
        results['No of hr in Humidity range (30-40)'].append(len(df5))
        results['No of hr in Humidity range (40-50)'].append(len(df6))
        results['No of hr in Humidity range (50-60)'].append(len(df7))
        results['No of hr in Humidity range (60-70)'].append(len(df8))
        results['No of hr in Humidity range (70-80)'].append(len(df9))
        results['No of hr in Humidity range (80-90)'].append(len(df10))
        results['No of hr in Humidity range (90-100)'].append(len(df11))

    result_df = pd.DataFrame(results)
    st.dataframe(result_df)
    t = result_df['Temperature']
    v = result_df['Total no of hour']



    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(t, v, lw=4)
    ax.set_xlabel('Temperature in °C', fontsize=14)
    ax.set_ylabel('No. of hour in HR range', fontsize=14)
    ax.set_title('Temperature Vs No. of Hour', fontsize=20)
    st.pyplot(fig)

