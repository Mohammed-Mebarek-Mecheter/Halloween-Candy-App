# components/candy_comparison.py
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import polars as pl
import pandas as pd

from components.visualizations import COLORS

def render_candy_comparison(data: pl.DataFrame):
    """
    Renders a candy comparison tool in the Streamlit app with donut charts for Win%, Sugar%, and Price%.

    Args:
        data (pl.DataFrame): The candy dataset.
    """
    st.write("Select candies to compare their attributes side by side.")

    # Get list of all candy names
    candy_names = data['competitorname'].to_list()

    # Allow user to select multiple candies for comparison
    selected_candies = st.multiselect("Choose candies to compare:", candy_names)

    if len(selected_candies) > 1:
        # Filter data for selected candies
        comparison_data = data.filter(pl.col('competitorname').is_in(selected_candies))

        # Create a comparison table with all relevant information
        comparison_table = create_comparison_table(comparison_data)

        st.dataframe(comparison_table)

        # Plot donut charts for Win%, Sugar%, and Price%
        plot_bar_charts(comparison_data)

    else:
        st.write("Please select at least two candies for comparison.")


def create_comparison_table(data: pl.DataFrame) -> pd.DataFrame:
    """
    Creates a comprehensive comparison table for selected candies.

    Args:
        data (pl.DataFrame): Filtered data for selected candies.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the comparison table.
    """
    # List of all attributes to include in the comparison
    attributes = [
        'competitorname', 'winpercent', 'sugarpercent', 'pricepercent',
        'chocolate', 'fruity', 'caramel', 'peanutyalmondy', 'nougat',
        'crispedricewafer', 'hard', 'bar', 'pluribus'
    ]

    # Select only the relevant columns and convert to pandas DataFrame
    comparison_df = data.select(attributes).to_pandas()

    # Format the percentage columns
    for col in ['winpercent', 'sugarpercent', 'pricepercent']:
        comparison_df[col] = comparison_df[col].apply(lambda x: f"{x:.2f}%")

    # Replace boolean values with Yes/No
    bool_columns = ['chocolate', 'fruity', 'caramel', 'peanutyalmondy', 'nougat',
                    'crispedricewafer', 'hard', 'bar', 'pluribus']
    for col in bool_columns:
        comparison_df[col] = comparison_df[col].map({1: 'Yes', 0: 'No'})

    # Rename columns for better readability
    comparison_df = comparison_df.rename(columns={
        'competitorname': 'Candy Name',
        'winpercent': 'Win %',
        'sugarpercent': 'Sugar %',
        'pricepercent': 'Price %',
        'peanutyalmondy': 'Peanut/Almond',
        'crispedricewafer': 'Crisp/Wafer'
    })

    return comparison_df


def plot_bar_charts(data: pl.DataFrame):
    """
    Plots three horizontal bar charts side by side for Win%, Sugar%, and Price% for selected candies.

    Args:
        data (pl.DataFrame): Filtered data for selected candies.
    """
    # Convert the filtered Polars DataFrame to Pandas for easier manipulation with Plotly
    comparison_df = data.select(['competitorname', 'winpercent', 'sugarpercent', 'pricepercent']).to_pandas()

    # Create columns in Streamlit to display the charts side by side
    col1, col2, col3 = st.columns(3)

    with col1:
        fig1 = create_bar_chart(comparison_df, 'competitorname', 'winpercent', 'Win %')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = create_bar_chart(comparison_df, 'competitorname', 'sugarpercent', 'Sugar %')
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        fig3 = create_bar_chart(comparison_df, 'competitorname', 'pricepercent', 'Price %')
        st.plotly_chart(fig3, use_container_width=True)


def create_bar_chart(df: pd.DataFrame, label_col: str, value_col: str, title: str):
    """
    Creates a Plotly horizontal bar chart.

    Args:
        df (pd.DataFrame): DataFrame containing the data for the chart.
        label_col (str): Column to use for labels.
        value_col (str): Column to use for values.
        title (str): Title of the chart.

    Returns:
        plotly.graph_objects.Figure: The bar chart figure.
    """
    # Generate a color palette based on the number of unique candies
    unique_candies = df['competitorname'].unique()
    colors = px.colors.qualitative.Plotly[:len(unique_candies)]

    # Create a dictionary to map candy names to colors
    color_mapping = {candy: color for candy, color in zip(unique_candies, colors)}

    # Apply the color mapping to the dataframe
    df['color'] = df['competitorname'].map(color_mapping)

    fig = go.Figure(go.Bar(
        x=df[value_col],
        y=df[label_col],
        marker=dict(
            color=df['color'],
            showscale=False,
        ),
        orientation='h',  # Horizontal bars
        text=df[value_col].apply(lambda x: f"{x:.2f}"),  # Rounds the values to two decimal points
        textposition='auto'
    ))

    fig.update_layout(
        title=title,
        showlegend=False,
        xaxis_title=value_col,
        yaxis_title=label_col,
        paper_bgcolor=COLORS['background'],
        plot_bgcolor=COLORS['background'],
        font_color=COLORS['text'],
        height=300
    )

    return fig
