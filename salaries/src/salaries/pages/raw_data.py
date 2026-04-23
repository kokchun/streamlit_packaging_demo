import streamlit as st 
from salaries.utils.constants import DATA_PATH
import pandas as pd 

df = pd.read_csv(DATA_PATH / "salaries.csv")

st.markdown("# RAW DATA")

st.dataframe(df)