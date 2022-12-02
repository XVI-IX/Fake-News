import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from Home import df, generate_cloud

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

if (st.checkbox("Display Word Clouds")):

  fake_news = " ".join(df['text'][df['label'] == "FAKE"].str.lower())
  real_news = " ".join(df['text'][df['label'] == "REAL"].str.lower())


  st.write("### Frequency of words in news that turned out fake")
  fig, ax = plt.subplots(figsize=(12, 8))
  ax.imshow(generate_cloud(fake_news), interpolation='bilinear')
  plt.axis("off")

  st.pyplot(fig)

  st.write("### Frequency of words in news that turned out real")
  fig, ax = plt.subplots(figsize=(12, 8))
  ax.imshow(generate_cloud(real_news), interpolation='bilinear')
  plt.axis("off")

  st.pyplot(fig)

st.write("## Modelling")
st.write("Using a PassiveAgressiveClassifier resulted in a model with 93.4% accuracy")
st.code(
  """PassiveAggressiveClassifier(
    C=0.5, early_stopping=True,
    max_iter=3000, random_state=42
)"""
  )

st.write("This resulted in an accuracy of `0.9337016574585635`, and a confusion matrix of")
st.code(
  """array([[588,  40],
      [ 44, 595]])""")

