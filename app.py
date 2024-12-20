import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World")

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

"""
# Dataframe
"""
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
# st.table(dataframe)

"""
# Line Chart
"""
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


"""
# Map
"""

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


"""
# Checkbox
"""

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

"""
# Selectbox
"""

option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

st.write('You selected:', option)