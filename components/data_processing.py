# components/data_processing.py
import streamlit as st
import polars as pl


@st.cache_data(hash_funcs={pl.DataFrame: id})
def load_data():
    return pl.read_csv("data/candy-data.csv")


def filter_candies(data, chocolate, fruity, caramel, peanutalmondy, nougat, crispedricewafer, hard, bar, pluribus,
                   sugar_range, price_range, win_range):
    # Start with a copy of the original data
    filtered_data = data.clone()

    # Handling filters for categorical attributes
    if chocolate != 'All':
        filtered_data = filtered_data.filter(pl.col('chocolate') == (chocolate == 'Yes'))
    if fruity != 'All':
        filtered_data = filtered_data.filter(pl.col('fruity') == (fruity == 'Yes'))
    if caramel != 'All':
        filtered_data = filtered_data.filter(pl.col('caramel') == (caramel == 'Yes'))
    if peanutalmondy != 'All':
        filtered_data = filtered_data.filter(pl.col('peanutalmondy') == (peanutalmondy == 'Yes'))
    if nougat != 'All':
        filtered_data = filtered_data.filter(pl.col('nougat') == (nougat == 'Yes'))
    if crispedricewafer != 'All':
        filtered_data = filtered_data.filter(pl.col('crispedricewafer') == (crispedricewafer == 'Yes'))
    if hard != 'All':
        filtered_data = filtered_data.filter(pl.col('hard') == (hard == 'Yes'))
    if bar != 'All':
        filtered_data = filtered_data.filter(pl.col('bar') == (bar == 'Yes'))
    if pluribus != 'All':
        filtered_data = filtered_data.filter(pl.col('pluribus') == (pluribus == 'Yes'))

    # Filter by sugar, price, and win percentage ranges (0 to 100 scale)
    filtered_data = filtered_data.filter(
        (pl.col('sugarpercent') <= sugar_range) &
        (pl.col('pricepercent') <= price_range) &
        (pl.col('winpercent') <= win_range)
    )

    # If the filtered data is empty, return the original data with a warning
    if filtered_data.is_empty():
        st.warning("No candies match the selected filters. Showing all candies instead.")
        return data

    return filtered_data


def get_best_value_candies(data):
    # Finding candies with high win percent, low price, and high sugar content
    return data.filter((pl.col('winpercent') >= 50) &
                       (pl.col('pricepercent') <= 50)).sort('winpercent', descending=True)