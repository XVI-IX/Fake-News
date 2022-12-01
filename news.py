import pandas as pd
import numpy as np
import pickle

from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import train_test_split, HalvingGridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

def predict_news(text):
  """
  predict_news - predicts the authenticity of news given in text.

  @text: text representing news to classify as real or fake
  
  Return: Real if news is real and fake otherwise
  """
  text = np.array([text])

  # loading label encoder
  with open("./Model/encoder.pkl", "rb") as handle:
    encoder = pickle.load(handle)

  # loading vectorizer
  with open('./Model/vectorizer.pkl', 'rb') as handle:
    vectorizer = pickle.load(handle)

  # loading model
  with open('./Model/model.pkl', 'rb') as handle:
    model = pickle.load(handle)

  enc_text = vectorizer.transform(text)

  pred = model.predict(enc_text)

  return (encoder.inverse_transform(pred)[0])


