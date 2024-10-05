# 🎃 Maven Halloween Candy Challenge Dashboard 🍬

Welcome to the **Maven Halloween Candy Challenge Dashboard**! This interactive app allows you to explore and analyze the most popular Halloween candies using data-driven insights. The dashboard helps you choose the best candies to give out on Halloween to become the most popular house on the block!

## 🚀 Getting Started

### Prerequisites

Before running the dashboard, make sure you have the following installed:
- Python 3.12+
- Streamlit
- Polars (for fast data processing)
- Plotly (for visualizations)
- Pandas (for data processing)

### Installation

1. **Clone this repository**:
    ```bash
    git clone https://github.com/Mohammed-Mebarek-Mecheter/Halloween-Candy-App.git
    cd Halloween-Candy-App
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:
    ```bash
    streamlit run app.py
    ```

The dashboard will launch in your browser at `http://localhost:8501`.

## 🏗️ Project Structure

Here's a breakdown of the project's structure:

```
/candy_analysis_app/
│
├── /assets/                    # Static assets (logos, images)
│   
├── /data/                      # Data files
│   ├── candy-data.csv           # Halloween candy dataset
│
├── /components/                # Modular Streamlit components
│   ├── sidebar.py              # Sidebar with filters for candy attributes
│   ├── visualizations.py       # Plotly visualizations (charts)
│   ├── candy_comparison.py     # Tool for comparing selected candies
│   ├── data_processing.py      # Data processing using Polars
│   
├── app.py                      # Main Streamlit app entry point
├── requirements.txt            # List of all dependencies
└── README.md                   # Project description and setup guide
```

## 📊 Dashboard Features

### 1. **Candy Popularity Overview**
- **Filtered Candy Popularity**: A bar chart displaying the win percentage of candies based on user-selected filters (chocolate, fruity, caramel, sugar content, and price range).
- **Top 10 Candies**: A bar chart showcasing the top 10 candies with the highest win percentage.

### 2. **Attribute Analysis**
- **Chocolate vs. Non-Chocolate Candies**: A donut chart showing the distribution of candies based on whether they contain chocolate or not.

### 3. **Price vs. Value Examination**
- **Sugar vs. Price Comparison**: A scatter plot comparing the sugar content and price percentile of candies, with point size representing candy popularity (win percentage).
- **Candy Value Analysis**: A scatter plot with quadrant analysis, showing the relationship between candy price and popularity. It highlights candies that offer the best value (high win percentage, low price).

### 4. **Candy Comparison Tool**
- Select multiple candies to compare side by side based on their attributes (win percentage, sugar content, price).

### 5. **Sugar Content vs. Popularity**
- A scatter plot that illustrates the correlation between a candy's sugar content and its win percentage. A trendline helps identify whether higher sugar content leads to increased popularity.

### 6. **Recommendations for Halloween**
- Based on the analysis, we provide recommendations for the top candies to offer on Halloween to ensure you're the most popular house on the block!

## 🔍 Key Findings

Here are some of the key insights derived from our candy analysis:

### 1. **Top 10 Most Popular Candies**
- **Reese's Peanut Butter Cups** consistently rank as the most popular candy with the highest win percentage.
- Other popular candies include **Twix**, **Kit Kat**, and **Snickers**, all offering a combination of chocolate, caramel, and crisp textures.

### 2. **Chocolate Dominates**
- Candies containing **chocolate** tend to outperform non-chocolate candies by a significant margin.
- **Chocolate + Peanut Butter** combinations are especially popular, as seen with Reese's varieties.

### 3. **Fruity Candies**
- Fruity candies like **Starburst** and **Skittles** still maintain popularity but generally fall behind chocolate-based candies in overall win percentage.

### 4. **Candy Value Analysis**
- Candies that balance both **high win percentage** and **low price** offer the best value. For example:
  - **Reese's Miniatures** and **Twix** provide excellent value with high popularity at relatively lower price percentiles.
  
### 5. **Sugar Content vs. Popularity**
- There is a slight positive correlation between sugar content and popularity, but **price** has a stronger impact. More expensive candies tend to be more popular, but there are exceptions where cheaper candies perform well.

### 6. **Recommendations for Halloween**
Based on our findings, here are the **top 3 candy recommendations** to maximize your Halloween success:
1. **Reese's Peanut Butter Cups** – the all-time favorite.
2. **Twix** – a perfect mix of chocolate, caramel, and cookie.
3. **Kit Kat** – offering a unique texture that is widely enjoyed.

These candies will likely appeal to a wide variety of trick-or-treaters and ensure you are the most popular house on the block!

## 🎨 Design and Customization

- The app uses a **Halloween-themed color palette** featuring orange, purple, and dark gray.
- Charts are created with **Plotly** for interactive and responsive visualizations, ensuring a smooth user experience across devices.
- The sidebar allows for **real-time filtering** of candy data based on attributes such as chocolate content, fruity flavors, sugar content, and price percentile.

---

## 📧 Contact

For any inquiries or suggestions, feel free to contact us via [email](mailto:mohammedmecheter@gmail.com).

Enjoy exploring and analyzing the world of Halloween candy! 🍫🍬 Happy Halloween! 🎃👻

---

