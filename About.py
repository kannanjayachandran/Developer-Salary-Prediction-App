import streamlit as st

def show_about_page():


    st.title("About")
    st.header("""This is a simple app to predict the salary of a software engineer based on the following parameters""")
    st.subheader("""Country""")
    st.subheader("""Years of Experience""")
    st.subheader("""Education Level""")

    
    
    st.write("""### The data used for this project is from the Stack Overflow Developer Survey 2020. The data can be found [here](https://survey.stackoverflow.co/2022/ )""")
    
    st.write(
        """
        This app is created by [Kannan J](https://github.com/kannanjayachandran)
        """
    )