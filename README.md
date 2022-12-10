# [Fake-News](https://xvi-ix-fake-news-home-mskr9n.streamlit.app/)

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

The aim of this project is to build a model to accurately
  **classify** a piece of news as **REAL** or **FAKE**.

## Data Description

This dataset has a shape of 7796 × 4.
The first column identifies the news,
the second and third are the title and text,
and the fourth column has labels denoting whether the news is REAL or FAKE.

## Install Dependencies

1. Python 3.7 - Follow instructions to install latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. Virtual Environment - It is recommeneded that you work within a virtual environment whenever using Python for projects. This keeps your dependecies for each project seperate and organized. Instructions for setting up a virtual environment for your platform can be found [here](https://docs.python.org/3/library/venv.html)

3. PIP Dependencies - Once the virtual environment is setup and running, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Key PIP Dependencies

* Scikit-Learn is a library with simple and efficient tools for predictive data analysis. check [here](https://scikit-learn.org/stable/) for more info.

* Numpy is a fundamental package for scientific computing with Python. It has powerful N-Dimensional Arrays, numerical computing tools and is open source. check [here](https://numpy.org/) for more info.

* Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of Python. Check [here](https://pandas.pydata.org/) for more info.

* Plotly is a Python graphing library that makes interactive, publication-quality graphs. check [here](https://plotly.com/python/) for more info.

* Wordcloud is a Python module that creates wordclouds. check [here](https://amueller.github.io/word_cloud/index.html)for more info.

* Streamlit is an open-source Python library that makes it easy to create and share custom web apps for machine learning and data science. check [here](https://docs.streamlit.io/) for more info.

## Set up the app

from within the directory, ensure the virtual environment is running.
To run the app, execute:

```bash
streamlit run Home.py
```

## Files

This project consists of some major files:

1. `Home.py` - This is the main page for the app

2. `pages/1_🔍️_Analysis.py` - Contains the logic for the project's data analysis.

3. `pages/2_👨‍💻_Classify.py` - Contains the logic responsible for news text classification.
