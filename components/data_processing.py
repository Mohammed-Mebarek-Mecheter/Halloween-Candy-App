# components/data_processing.py
import streamlit as st
import polars as pl


@st.cache_data(hash_funcs={pl.DataFrame: id})
def load_data():
    return pl.read_csv("data/candy-data.csv")


def filter_candies(data, chocolate, fruity, caramel, sugar_range, price_range):

    # Handling filters for categorical attributes
    if chocolate != 'All':
        data = data.filter(pl.col('chocolate') == (chocolate == 'Yes'))
    if fruity != 'All':
        data = data.filter(pl.col('fruity') == (fruity == 'Yes'))
    if caramel != 'All':
        data = data.filter(pl.col('caramel') == (caramel == 'Yes'))

    # Filter by sugar and price range
    data = data.filter((pl.col('sugarpercent') <= sugar_range) & (pl.col('pricepercent') <= price_range))

    return data


def get_best_value_candies(data):

    return data.filter((pl.col('winpercent') > 50) & (pl.col('pricepercent') < 0.5)).sort('winpercent', descending=True)
