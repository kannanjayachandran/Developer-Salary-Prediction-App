import streamlit as st

def show_about_page():


    st.title("About")
    st.write("""### This is a simple app to predict the salary of a software engineer based on the following parameters:
    - Country
    - Education Level
    - Years of Experience
    """)
    st.write("""### The data used for this project is from the Stack Overflow Developer Survey 2020. The data can be found [here](https://insights.stackoverflow.com/survey/2020)""")
    
    st.write(
        """
        This app is created by [Kannan J](https://github.com/kannanjayachandran)
        """
    )