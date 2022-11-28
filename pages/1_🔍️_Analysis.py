import streamlit as st
import pandas as pd
import plotly.express as px
from Home import df

st.set_page_config(
  page_icon="🔍️",
  page_title="Analysis"
)

st.write("# **Dataframe**")
x = st.slider("Rows", 0, 100, 10)
st.write(df.head(x))

values = [
  df['label'][df['label'] == 'FAKE'].count(),
  df['label'][df['label'] == 'REAL'].count()]
labels = ['FAKE', 'REAL']


fig = px.pie(
  df, values = values,
  color=labels,
  names=labels, title="Percentage of News Classes",
  hole = .5, color_discrete_map={
    'REAL':"#0984e3",
    'FAKE': "#d63031"
  },
  hover_data=None
)
fig.update_traces(textposition='inside')

st.plotly_chart(fig)

st.write(
  "Since this appears to be a balanced dataset, it can be worked on without worrying about balancing it up.")