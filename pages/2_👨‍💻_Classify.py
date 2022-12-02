import streamlit as st
from news import predict_news
from Home import generate_cloud
import matplotlib.pyplot as plt

st.set_page_config(
  page_icon="👨‍💻",
  page_title="Classify"
)


st.write(
  """
  # Classifier
  **Disclaimer**: This app does not assure 100% accuracy and due
  to this news might be misclassified.

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

if (st.checkbox(
  "Show Word Cloud",
  help="Show the most occuring words in news text.")):

  st.write("### Frequency of words in news.")

  fig, ax = plt.subplots(figsize=(12, 8))
  ax.imshow(generate_cloud(text), interpolation='bilinear')
  plt.axis("off")

  st.pyplot(fig)