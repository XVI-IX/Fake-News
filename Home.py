import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="Home",
  page_icon="🏠️"
)

st.markdown(
  """
  # Fake News Classifier

  ## Introduction
  A type of yellow journalism, fake news encapsulates pieces of news
  that may be hoaxes and is generally spread through social media and
  other online media.
  This is often done to further or impose certain ideas 
  and is often achieved with political agendas.
  Such news items may contain false and/or exaggerated claims,
  and may end up being viralized by algorithms,
  and users may end up in a filter bubble.

  ## Objective
  The aim of this project is to build a model to accurately classify a piece of news as REAL or FAKE.

  ## Data Description
  This dataset has a shape of 7796 × 4. 
  The first column identifies the news, 
  the second and third are the title and text, 
  and the fourth column has labels denoting whether the news is REAL or FAKE.
  """
)

df = pd.read_csv("./Model/news.csv")
st.dataframe(df.head())

st.markdown(
  """
  - title:    Represents the title of the news article.
  - text:     The text containing the news in details
  - label:    Classification
  """
)
