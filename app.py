import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello First App")

st.subheader("Sub title")

st.write("""# Hello 
## Subheading""")

fileinput = st.file_uploader("Enter CSV file:", type="csv")

if fileinput is not None:
    df = pd.read_csv(fileinput)   
    st.dataframe(df)              # Display dataframe
    st.dataframe(df["target"] > 1)

    st.area_chart(df)
else:
    st.write("Please upload a CSV file.")

