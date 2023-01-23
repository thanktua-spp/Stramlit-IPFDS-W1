import os
import shutil

import gdown
import pandas as pd
import plotly.express as px
import streamlit as st


@st.cache
def get_data():
    # Download file from Google Drive
    # This file is based on data from: http://insideairbnb.com/get-the-data/
    file_id_1 = "1rsxDntx9CRSyDMy_fLHEI5Np4lB153sa"
    downloaded_file_1 = "listings.pkl"
    gdown.download(id=file_id_1, output=downloaded_file_1)

    # Read a Python Pickle file
    return pd.read_pickle("listings.pkl")


df = get_data()


st.title("The Airbnb dataset of Amsterdam")
st.markdown(
    "The dataset contains slight modifications with regards to the original for illustrative purposes"
)
st.dataframe(df.head(100))
st.text("The dataset was retrieved using the following code:")
st.code(
    """
@st.cache
def get_data():
    # Download file from Google Drive
    # This file is based on data from: http://insideairbnb.com/get-the-data/
    file_id_1 = "1f6o9IeaieH_xXyghjnREfl2dC44pIUc4"
    downloaded_file_1 = "listings.pkl"
    gdown.download(id=file_id_1, output=downloaded_file_1)
    
    # Read a Python Pickle file
    return pd.read_pickle("listings.pkl")
""",
    language="python",
)
st.markdown(
    "*Let's take a closer look at the supposed relation between **price_in_dollar** and **review_scores_rating**.*"
)
st.plotly_chart(
    px.scatter(
        df,
        x="price_in_dollar",
        y="review_scores_rating",
        trendline="ols",
        trendline_color_override="orange",
    )
)
