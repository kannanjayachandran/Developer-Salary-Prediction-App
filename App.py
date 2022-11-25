import streamlit as st
from Prediction import show_predict_page
from Explore import show_explore_page
from About import show_about_page


page = st.sidebar.selectbox("Insights ~ Prediction ~ About", ("Predictions", "Insights", "About"))

if page == "Predictions":
    show_predict_page()
elif page == "Insights":
        show_explore_page()
else:
    show_about_page()