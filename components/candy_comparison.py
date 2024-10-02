# components/candy_comparison.py
import streamlit as st
import plotly.graph_objects as go
import polars as pl


def render_candy_comparison(data):
    st.write("Select candies and metrics to compare their attributes side by side.")

    # Convert data to Polars DataFrame if it's not already
    if not isinstance(data, pl.DataFrame):
        data = pl.DataFrame(data)

    # Allow selection of up to 5 candies
    selected_candies = st.multiselect(
        "Select candies to compare (max 5):",
        data['competitorname'].unique().to_list(),
        max_selections=5
    )

    # Handle empty candy selection
    if len(selected_candies) == 0:
        st.write("Please select at least one candy to compare.")
        return

    # Define metrics for comparison
    all_metrics = ['winpercent', 'sugarpercent', 'pricepercent', 'chocolate', 'fruity',
                   'caramel', 'peanutyalmondy', 'nougat', 'crispedricewafer', 'hard', 'bar']

    # Allow user to select metrics
    selected_metrics = st.multiselect(
        "Select metrics to compare:",
        all_metrics,
        default=['winpercent', 'sugarpercent', 'pricepercent']
    )

    if len(selected_metrics) == 0:
        st.write("Please select at least one metric to compare.")
        return

    # Filter the data to include only the selected candies
    comparison_data = data.filter(pl.col('competitorname').is_in(selected_candies))

    # Create a radar chart for selected candies and metrics
    fig = go.Figure()

    # Normalize binary metrics to avoid scaling issues in the radar chart
    binary_metrics = ['chocolate', 'fruity', 'caramel', 'peanutyalmondy', 'nougat', 'crispedricewafer', 'hard', 'bar']

    for candy in selected_candies:
        candy_data = comparison_data.filter(pl.col('competitorname') == candy)
        values = []
        for metric in selected_metrics:
            if metric in ['winpercent', 'sugarpercent', 'pricepercent']:
                values.append(candy_data[metric][0] * 100)  # Scale percentages to 100
            else:
                values.append(candy_data[metric][0] * 100)  # Scale binary metrics to 100 for radar chart visibility

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=selected_metrics,
            fill='toself',
            name=candy
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]  # Ensure all metrics are scaled between 0-100
            )
        ),
        showlegend=True,
        title="Candy Attribute Comparison",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

    # Display a table with detailed comparison
    st.subheader("Detailed Comparison")
    comparison_table = comparison_data.select(['competitorname'] + selected_metrics)
    st.dataframe(comparison_table.to_pandas().set_index('competitorname').T.style.format("{:.2f}"))

    # Provide insights based on the comparison
    st.subheader("Comparison Insights")
    for candy in selected_candies:
        candy_data = comparison_data.filter(pl.col('competitorname') == candy)
        st.write(f"**{candy}**:")
        for metric in selected_metrics:
            value = candy_data[metric][0]
            if metric in ['winpercent', 'sugarpercent', 'pricepercent']:
                st.write(f"- {metric.capitalize()}: {value * 100:.2f}%")
            else:
                st.write(f"- {metric.capitalize()}: {'Yes' if value else 'No'}")
        st.write("")

    # Add a bar chart for easier comparison of numerical metrics
    numerical_metrics = [m for m in selected_metrics if m in ['winpercent', 'sugarpercent', 'pricepercent']]
    if numerical_metrics:
        st.subheader("Numerical Metrics Comparison")
        bar_fig = go.Figure()
        for metric in numerical_metrics:
            bar_fig.add_trace(go.Bar(
                x=selected_candies,
                y=comparison_data[metric] * 100,
                name=metric.capitalize()
            ))

        bar_fig.update_layout(
            title="Comparison of Numerical Metrics",
            xaxis_title="Candy",
            yaxis_title="Percentage",
            barmode='group'
        )
        st.plotly_chart(bar_fig, use_container_width=True)
