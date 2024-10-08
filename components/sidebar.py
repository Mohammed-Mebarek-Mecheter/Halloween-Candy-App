# components/sidebar.py
import streamlit as st

def render_sidebar():
    """
    Renders the sidebar with filters for candy attributes such as chocolate, fruity, caramel,
    and sliders for sugarpercent, pricepercent, and winpercent.

    Returns:
        Tuple: chocolate, fruity, caramel, peanutalmondy, nougat, crispedricewafer, hard, bar, pluribus, sugar_range, price_range, win_range (filter inputs from the user)
    """
    st.sidebar.image("assets/halloween-owl.png", width=100)
    st.sidebar.header("Filter Your Candy")

    # Default values
    default_chocolate = 'All'
    default_fruity = 'All'
    default_caramel = 'All'
    default_peanutalmondy = 'All'  # Corrected from 'peanutalmondy'
    default_nougat = 'All'
    default_crispedricewafer = 'All'
    default_hard = 'All'
    default_bar = 'All'
    default_pluribus = 'All'
    default_sugar_range = 100
    default_price_range = 100
    default_win_range = 100  # Corrected to 100

    # Initialize session state if not already set
    if 'chocolate' not in st.session_state:
        st.session_state['chocolate'] = default_chocolate
    if 'fruity' not in st.session_state:
        st.session_state['fruity'] = default_fruity
    if 'caramel' not in st.session_state:
        st.session_state['caramel'] = default_caramel
    if 'peanutalmondy' not in st.session_state:  # Corrected key
        st.session_state['peanutalmondy'] = default_peanutalmondy
    if 'nougat' not in st.session_state:
        st.session_state['nougat'] = default_nougat
    if 'crispedricewafer' not in st.session_state:
        st.session_state['crispedricewafer'] = default_crispedricewafer
    if 'hard' not in st.session_state:
        st.session_state['hard'] = default_hard
    if 'bar' not in st.session_state:
        st.session_state['bar'] = default_bar
    if 'pluribus' not in st.session_state:
        st.session_state['pluribus'] = default_pluribus
    if 'sugar_range' not in st.session_state:
        st.session_state['sugar_range'] = default_sugar_range
    if 'price_range' not in st.session_state:
        st.session_state['price_range'] = default_price_range
    if 'win_range' not in st.session_state:
        st.session_state['win_range'] = default_win_range

    # Select key attributes
    chocolate = st.sidebar.selectbox('Contains Chocolate?', ['All', 'Yes', 'No'], index=0, key='chocolate')
    fruity = st.sidebar.selectbox('Is Fruity?', ['All', 'Yes', 'No'], index=0, key='fruity')
    caramel = st.sidebar.selectbox('Contains Caramel?', ['All', 'Yes', 'No'], index=0, key='caramel')
    peanutalmondy = st.sidebar.selectbox('Contains Peanuts?', ['All', 'Yes', 'No'], index=0, key='peanutalmondy')  # Corrected spelling
    nougat = st.sidebar.selectbox('Contains Nougat?', ['All', 'Yes', 'No'], index=0, key='nougat')
    crispedricewafer = st.sidebar.selectbox('Contains Crisped Rice Wafer?', ['All', 'Yes', 'No'], index=0, key='crispedricewafer')
    hard = st.sidebar.selectbox('Is Hard Candy?', ['All', 'Yes', 'No'], index=0, key='hard')
    bar = st.sidebar.selectbox('Is Bar?', ['All', 'Yes', 'No'], index=0, key='bar')
    pluribus = st.sidebar.selectbox('Is Pluribus?', ['All', 'Yes', 'No'], index=0, key='pluribus')

    # Sliders for win, sugar, and price percentages (now as percentages)
    sugar_range = st.sidebar.slider(
        'Max Sugar Percentage',
        0, 100,
        st.session_state['sugar_range'],
        step=1,
        key='sugar_range',
        help="Limit the sugar level of candies."
    )

    price_range = st.sidebar.slider(
        'Max Price Percentage',
        0, 100,
        st.session_state['price_range'],
        step=1,
        key='price_range',
        help="Set a price range for candies."
    )

    win_range = st.sidebar.slider(
        'Max Win Percentage',
        0, 100,
        st.session_state['win_range'],  # Corrected initial value from 0 to session state
        step=1,
        key='win_range',
        help="Set a win range for candies."
    )

    # Check if reset button is clicked
    if st.sidebar.button('Reset Filters'):
        st.session_state['chocolate'] = default_chocolate
        st.session_state['fruity'] = default_fruity
        st.session_state['caramel'] = default_caramel
        st.session_state['peanutalmondy'] = default_peanutalmondy  # Corrected key
        st.session_state['nougat'] = default_nougat
        st.session_state['crispedricewafer'] = default_crispedricewafer
        st.session_state['hard'] = default_hard
        st.session_state['bar'] = default_bar
        st.session_state['pluribus'] = default_pluribus
        st.session_state['sugar_range'] = default_sugar_range
        st.session_state['price_range'] = default_price_range
        st.session_state['win_range'] = default_win_range
        st.rerun()

    return chocolate, fruity, caramel, peanutalmondy, nougat, crispedricewafer, hard, bar, pluribus, sugar_range, price_range, win_range
