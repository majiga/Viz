import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# Test app using Streamlit
This is **too easy** and easy is the best :)
""")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.write("""
## Random spots in Perth
""")

df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [-31.95, 115.85], columns=['lat', 'lon'])
st.map(df)

number = st.slider("Pick a number", 0, 100)

file = st.file_ uploader("Pick a file")

color = st.color_picker()
