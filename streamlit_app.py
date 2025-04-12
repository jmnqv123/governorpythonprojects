import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Visualizer", layout="wide")

st.title("📊 Data Visualization Web App")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data")
    st.write(df)

    # Select columns for plotting
    st.subheader("Select columns to plot")
    columns = df.columns.tolist()
    
    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)

    chart_type = st.radio("Chart Type", ["Bar", "Line"])

    if st.button("Generate Chart"):
        fig, ax = plt.subplots()
        if chart_type == "Bar":
            ax.bar(df[x_axis], df[y_axis], color='skyblue')
        else:
            ax.plot(df[x_axis], df[y_axis], marker='o', color='orange')

        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"{chart_type} Chart: {y_axis} vs {x_axis}")
        plt.xticks(rotation=45)
        st.pyplot(fig)
else:
    st.info("Please upload a CSV file to begin.")
