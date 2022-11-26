import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time



def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'






def main_data_explore():
    df = pd.read_csv("./Data/survey_results_public.csv")

    df = df[["Country", "EdLevel", "YearsCodePro", "ConvertedCompYearly", "DevType"]]












@st.cache
def load_data():
    df = pd.read_csv("./Data/survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df[df["ConvertedComp"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["ConvertedComp"] <= 250000]
    df = df[df["ConvertedComp"] >= 100]
    df = df[df["Country"] != "Other"]

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    return df

df = load_data()

def show_explore_page():

    # surpress warnings
    st.set_option('deprecation.showPyplotGlobalUse', False)


    with st.spinner(text='Crunching the numbers...'):
        time.sleep(0.5)
        st.success('Done')
    
    st.title("Software Engineer Salary Prediction")

    data = df["Country"].value_counts()

    st.subheader("Country Wise Distribution of Software Engineers")
    st.bar_chart(data)
    
    # bar chart using seaborn
    st.subheader("Country Wise Distribution of Software Engineers")
    plt.figure(figsize=(10, 6))
    sns.countplot(x="Country", data=df, )
    st.pyplot()

    plt.figure(figsize=(10, 6))
    sns.histplot(df["Salary"], kde=True)
    st.pyplot()


    
    st.write("""#### Mean Salary Based On Country""")

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Mean Salary Based On Experience
    """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

