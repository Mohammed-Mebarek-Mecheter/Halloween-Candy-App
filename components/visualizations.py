# components/visualizations.py
import plotly.express as px
import plotly.graph_objects as go
import polars as pl
from altair.examples.pyramid import color

COLORS = {
    'primary': '#FF6B35',  # Orange
    'secondary': '#7209B7',  # Purple
    'accent': '#3A86FF',  # Blue
    'background': '#1A1A1A',  # Dark gray
    'text': '#F8F9FA',  # Light gray
}

def plot_candy_distribution(candies):
    """
    Plots a bar chart showing the winpercent distribution for the filtered candies.

    Args:
        candies (Polars DataFrame): Filtered candy data.

    Returns:
        Plotly Figure: Bar chart of candy winpercent distribution.
    """
    fig = px.bar(candies.to_pandas(),
                 x='competitorname',
                 y='winpercent',
                 text='winpercent',
                 labels={'competitorname': 'Candy', 'winpercent': 'Win Percent'},
                 title="Candy Popularity by Win Percent")

    fig.update_traces(marker_color='orange', marker_line_color='black', marker_line_width=1.5, opacity=0.8)
    fig.update_layout(paper_bgcolor=COLORS['background'], plot_bgcolor=COLORS['background'], font_color=COLORS['text'], xaxis_tickangle=-45, yaxis_title="Win Percent", xaxis_title="Candy", height=500)

    return fig


def plot_sugar_vs_price(candies):
    """
    Plots a scatter plot comparing sugarpercent and pricepercent for the filtered candies.

    Args:
        candies (Polars DataFrame): Filtered candy data.

    Returns:
        Plotly Figure: Scatter plot comparing sugar and price percent.
    """
    fig = px.scatter(candies.to_pandas(),
                     x='sugarpercent',
                     y='pricepercent',
                     size='winpercent',
                     hover_name='competitorname',
                     title="Sugar vs Price Comparison",
                     labels={'sugarpercent': 'Sugar Percent', 'pricepercent': 'Price Percent'})

    fig.update_traces(marker=dict(opacity=0.6, line=dict(width=1, color='black')))
    fig.update_layout(paper_bgcolor=COLORS['background'], plot_bgcolor=COLORS['background'], font_color=COLORS['text'], xaxis_title="Sugar Percent", yaxis_title="Price Percent", height=500)

    return fig

def plot_top_10_candies(candies):
    """
    Plots a bar chart showing the winpercent distribution for the top 10 candies.

    Args:
        candies (Polars DataFrame): Candy dataset sorted by winpercent.

    Returns:
        Plotly Figure: Bar chart of top 10 candy winpercent distribution.
    """
    top_10 = candies.sort('winpercent', descending=True).head(10)
    fig = px.bar(top_10.to_pandas(),
                 x='competitorname',
                 y='winpercent',
                 text='winpercent',
                 labels={'competitorname': 'Candy', 'winpercent': 'Win Percent'},
                 title="Top 10 Most Popular Candies")

    fig.update_traces(marker_color='orange', marker_line_color='black', marker_line_width=1.5, opacity=0.8)
    fig.update_layout(paper_bgcolor=COLORS['background'], plot_bgcolor=COLORS['background'], font_color=COLORS['text'], xaxis_tickangle=-45, height=500)
    return fig


def plot_candy_attribute_distribution(candies, attribute, title):
    attribute_distribution = candies.to_pandas()[attribute].value_counts().reset_index()
    attribute_distribution.columns = [attribute, 'count']

    fig = px.pie(attribute_distribution,
                 names=attribute,
                 values='count',
                 hole=0.4,  # Create a donut chart
                 title=f"{title} Distribution")

    fig.update_traces(textposition='inside', textinfo='percent+label', marker=dict(colors=['#FF6B35', '#7209B7']))
    fig.update_layout(paper_bgcolor=COLORS['background'], plot_bgcolor=COLORS['background'], font_color=COLORS['text'], height=500)
    return fig


def get_best_value_candies(data):
    """
    Prepares all candies data for the value analysis visualization.

    Args:
        data (Polars DataFrame): The full candy dataset.

    Returns:
        Polars DataFrame: All candies with winpercent and pricepercent data.
    """
    return data.select(['competitorname', 'winpercent', 'pricepercent'])


# Update the plot_best_value_candies function
def plot_best_value_candies(data):
    df = data.to_pandas()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['pricepercent'],
        y=df['winpercent'],
        mode='markers+text',
        marker=dict(
            size=10,
            color=df['winpercent'],
            colorscale='oranges',
            showscale=True,
            colorbar=dict(title='Win %')
        ),
        text=df['competitorname'],
        hovertext=[f"{name}<br>Win: {win:.2f}%<br>Price: {price:.2f}" for name, win, price in zip(df['competitorname'], df['winpercent'], df['pricepercent'])]
    ))

    # Quadrant lines
    median_price = df['pricepercent'].median()
    median_win = df['winpercent'].median()
    fig.add_hline(y=median_win, line_dash="dash", line_color="white", annotation_text="Median Win %", annotation_position="top right")
    fig.add_vline(x=median_price, line_dash="dash", line_color="white", annotation_text="Median Price", annotation_position="top right")

    fig.update_layout(
        title="Candy Value Analysis: Win Percent vs Price Percent",
        xaxis_title="Price Percent",
        yaxis_title="Win Percent",
        paper_bgcolor=COLORS['background'],
        plot_bgcolor=COLORS['background'],
        font_color=COLORS['text'],
        height=600
    ).update_layout(annotations = [
        dict(x=0.25, y=0.95, xref="paper", yref="paper", text="High Value", showarrow=False, font=dict(size=14)),
        dict(x=0.75, y=0.95, xref="paper", yref="paper", text="Popular but Expensive", showarrow=False,
             font=dict(size=14)),
        dict(x=0.25, y=0.05, xref="paper", yref="paper", text="Low Value", showarrow=False, font=dict(size=14)),
        dict(x=0.75, y=0.05, xref="paper", yref="paper", text="Overpriced", showarrow=False, font=dict(size=14))
    ]
    )
    return fig

def plot_sugar_vs_popularity(candies):
    """
    Plots a scatter plot showing the relationship between sugarpercent and winpercent.

    Args:
        candies (Polars DataFrame): Filtered candy dataset.

    Returns:
        Plotly Figure: Scatter plot comparing sugarpercent and winpercent.
    """
    fig = px.scatter(candies.to_pandas(),
                     x='sugarpercent',
                     y='winpercent',
                     title="Sugar Content vs Candy Popularity",
                     labels={'sugarpercent': 'Sugar Percent', 'winpercent': 'Win Percent'},
                     trendline='ols', trendline_scope='overall')

    fig.update_traces(marker=dict(opacity=0.6, line=dict(width=1, color='black')))
    fig.update_layout(paper_bgcolor=COLORS['background'], plot_bgcolor=COLORS['background'], font_color=COLORS['text'], showlegend=False)
    return fig

def plot_fruity_vs_chocolate(candies):
    """
    Plots a comparison of winpercent between fruity and chocolate candies.
    """
    # Create a grouped summary for average winpercent
    candy_summary = candies.groupby(['chocolate', 'fruity']).agg(pl.col('winpercent').mean().alias('avg_winpercent')).to_pandas()

    fig = px.bar(candy_summary,
                 x='chocolate',
                 y='avg_winpercent',
                 color='fruity',
                 barmode='group',
                 labels={'avg_winpercent': 'Average Win Percent'},
                 title="Fruity vs. Chocolate Candy Popularity")
    return fig
