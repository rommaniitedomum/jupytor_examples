import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("train.csv")
st.line_chart(df)

# streamlit run app.py --server.port 20000