# app.py
import streamlit as st
import polars as pl
from components.sidebar import render_sidebar
from components.data_processing import load_data, filter_candies, get_best_value_candies
from components.visualizations import (
    plot_candy_distribution,
    plot_sugar_vs_price,
    plot_top_10_candies,
    plot_candy_attribute_distribution,
    plot_best_value_candies,
    plot_sugar_vs_popularity,
)
from components.candy_comparison import render_candy_comparison

# Set page config for wide layout
st.set_page_config(page_title="Maven Halloween Candy Challenge", page_icon="🍬", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load data (cached for performance)
@st.cache_data
def get_data():
    return load_data()

data = get_data()

# Main Header
st.markdown("""
    <div class="main-header">
        🎃 Maven Halloween Candy Challenge 🍬
    </div>
    """, unsafe_allow_html=True)

st.write("Welcome to the Maven Halloween Candy Challenge! Use this app to explore, analyze, and find the best Halloween candies to become the most popular house on the block.")

# Render KPIs (Total candies, average win percentage, top candy)

col1, col2, col3 = st.columns(3)
total_candies = len(data)
avg_win_percent = data['winpercent'].mean()
top_candy = data.sort('winpercent', descending=True).head(1)['competitorname'][0]

with col1:
    st.markdown(f"<div class='kpi-card'>Total Candies Analyzed<br>{total_candies}</div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='kpi-card'>Average Win Percentage<br>{avg_win_percent:.2f}%</div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='kpi-card'>Top Candy<br>{top_candy}</div>", unsafe_allow_html=True)

# Render the sidebar and get user input
chocolate, fruity, caramel, peanutyalmondy, nougat, crispedricewafer, hard, bar, pluribus, sugar_range, price_range = render_sidebar()

# Filter the data based on user input
filtered_candies = filter_candies(data, chocolate, fruity, caramel, peanutyalmondy, nougat, crispedricewafer, hard, bar, pluribus, sugar_range, price_range)

# Main content area
col1, col2 = st.columns(2)

with col1:
    st.markdown("---")
    st.markdown(f"<p class='summary-text'>Showing {len(filtered_candies)} candies based on your filters.</p>", unsafe_allow_html=True)
    st.dataframe(filtered_candies.to_pandas(), height=400)

    st.markdown("---")
    fig_top_10 = plot_top_10_candies(data)
    st.plotly_chart(fig_top_10, use_container_width=True)
    st.markdown(
        "<p class='summary-text'>"
        "Behold the champions of Halloween! These candies have proven their worth in countless battles "
        "for trick-or-treater affection. Pay close attention to the top contenders; they're your secret "
        "weapons for becoming the most popular house on the block."
        "</p>",
        unsafe_allow_html=True
    )

with col2:
    st.markdown("---")
    fig_distribution = plot_candy_distribution(filtered_candies)
    st.plotly_chart(fig_distribution, use_container_width=True)
    st.markdown("<p class='summary-text'>This chart displays the win percentage distribution for the filtered candies. It helps identify which candies are more popular within your selected criteria.</p>", unsafe_allow_html=True)

    st.markdown("---")
    fig_attribute = plot_candy_attribute_distribution(data, 'chocolate', 'Chocolate vs. Non-Chocolate Candies')
    st.plotly_chart(fig_attribute, use_container_width=True)
    st.markdown("<p class='summary-text'>This pie chart shows the distribution of chocolate vs. non-chocolate candies. It helps understand the overall composition of candy types in the dataset.</p>", unsafe_allow_html=True)

st.markdown("---")
fig_sugar_price = plot_sugar_vs_price(filtered_candies)
st.plotly_chart(fig_sugar_price, use_container_width=True)
st.markdown("<p class='summary-text'>This scatter plot compares the sugar content and price of candies. The size of each point represents its popularity. Look for candies in the bottom-right quadrant for high sugar content at lower prices.</p>", unsafe_allow_html=True)

st.markdown("---")
all_candies_data = get_best_value_candies(data)
fig_value_analysis = plot_best_value_candies(all_candies_data)
st.plotly_chart(fig_value_analysis, use_container_width=True)
st.markdown("""
<p class='summary-text'>
In the world of Halloween treats, not all candies are created equal. This chart maps out the delicate 
        balance between sugar content, price, and popularity. Look for candies in the 'sweet spot' – high in popularity 
        but lower in price – to maximize your Halloween impact without breaking the bank.
The plot is divided into four quadrants:
<ul>
    <li><strong>High Value (top-left):</strong> Popular candies with lower prices - these offer the best value.</li>
    <li><strong>Popular but Expensive (top-right):</strong> Well-liked candies that come at a higher price point.</li>
    <li><strong>Low Value (bottom-left):</strong> Less popular candies with lower prices.</li>
    <li><strong>Overpriced (bottom-right):</strong> Less popular candies with higher prices - these offer the least value.</li>
</ul>
The color of each point represents its win percentage, with darker colors indicating higher popularity. 
Hover over each point to see detailed information about each candy.
</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("---")
    # Add a section to display top value candies
    st.dataframe(all_candies_data.to_pandas(), height=400)
    st.markdown(
        "<p class='summary-text'>"
        "These candies offer the best combination of high popularity and lower price"
        "</p>",
        unsafe_allow_html=True
    )

with col2:
    st.markdown("---")
    fig_sugar_popularity = plot_sugar_vs_popularity(data)
    st.plotly_chart(fig_sugar_popularity, use_container_width=True)
    st.markdown(
            "<p class='summary-text'>"
            "Does sugar content directly correlate with a candy's popularity? This intriguing chart explores the "
            "relationship between sweetness and desirability. Understanding this connection can help you balance "
            "your offerings between crowd-pleasing sugary favorites and potentially healthier alternatives."
            "</p>",
            unsafe_allow_html=True
        )

# Candy Comparison Tool
st.markdown("<h2 class='sub-header'>🔍 Compare Candies</h2>", unsafe_allow_html=True)
render_candy_comparison(data)

# Conclusions and recommendations
st.markdown("<h2 class='sub-header'>🎃 Recommendations for Halloween</h2>", unsafe_allow_html=True)
st.write("""
    Based on our comprehensive candy analysis, here are the top recommendations to make your house the highlight of Halloween:

    1. **Reese's Miniatures**: The ultimate crowd-pleaser, offering the perfect blend of chocolate and peanut butter in a convenient, bite-sized format.
    2. **Twix**: A beloved candy bar that combines chocolate, caramel, and cookie for a satisfying mix of flavors and textures.
    3. **Starburst**: A top-performing fruity option to cater to those who prefer non-chocolate candies.

    By offering this mix of candies, you'll cater to a variety of preferences while ensuring high satisfaction among trick-or-treaters. This selection provides:
    - Both chocolate and non-chocolate options
    - Different textures (creamy, crunchy, chewy)
    - Variety of flavors (chocolate-peanut butter, chocolate-caramel-cookie, fruit)
    - All individually wrapped for convenience
    - High popularity and good value

    Remember, the key to Halloween success lies in offering popular, value-driven choices that balance taste, cost, and broad appeal.
    """)

st.markdown("<p class='summary-text'>Happy Halloween! 🎃👻🍬</p>", unsafe_allow_html=True)