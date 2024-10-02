# components/candy_comparison.py
import streamlit as st
import plotly.graph_objects as go

COLORS = {
    'primary': '#FF6B35',  # Orange
    'secondary': '#7209B7',  # Purple
    'accent': '#3A86FF',  # Blue
    'background': '#1A1A1A',  # Dark gray
    'text': '#F8F9FA',  # Light gray
}

def render_candy_comparison(data):
    st.subheader("Candy Comparison Tool")

    selected_candies = st.multiselect("Select candies to compare:", data['competitorname'].unique())

    if len(selected_candies) > 0:
        comparison_data = data[data['competitorname'].isin(selected_candies)]

        fig = go.Figure()

        for candy in selected_candies:
            candy_data = comparison_data[comparison_data['competitorname'] == candy]
            fig.add_trace(go.Bar(
                x=['Win %', 'Sugar %', 'Price %'],
                y=[candy_data['winpercent'].values[0],
                   candy_data['sugarpercent'].values[0],
                   candy_data['pricepercent'].values[0]],
                name=candy,
                marker_color=COLORS['primary']  # Assign dynamic colors
            ))

        fig.update_layout(
            barmode='group',
            title="Candy Comparison",
            xaxis_title="Attributes",
            yaxis_title="Percentage",
            plot_bgcolor=COLORS['background'],
            paper_bgcolor=COLORS['background'],
            font_color=COLORS['text']
        )

        st.plotly_chart(fig)
    else:
        st.write("Please select at least one candy to compare.")
