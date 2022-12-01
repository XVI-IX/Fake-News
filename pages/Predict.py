import streamlit as st
from news import predict_news


st.write(
  """
  # Classifier
  Paste news text to be classified in textbox below
  """
)

text = st.text_area(
  "News", placeholder="Paste news here", height=500
)

if (st.button(
  label="Classify", help="Click to classify news",
)):
  if (predict_news(text) == "REAL"):
    st.success("This news is **Real**", icon="✅")
  else:
    st.warning("This news is **Fake**, pay little attention to it", icon="⚠️")