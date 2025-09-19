import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Interactive Data Visualizer",
                   page_icon="📊",
                   layout="wide")

# App header
st.title("📊 Interactive Data Visualization Tool")
st.markdown("Upload your dataset and explore interactive visualizations with ease!")

# Sidebar for file upload
st.sidebar.header("Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Read data
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("✅ Data uploaded successfully!")
    
    # Show preview
    with st.expander("🔎 Preview Data"):
        st.dataframe(df.head(20), use_container_width=True)

    # Sidebar controls
    st.sidebar.header("Visualization Settings")
    chart_type = st.sidebar.selectbox(
        "Choose a visualization type:",
        ["Scatter Plot", "Line Chart", "Bar Chart", "Histogram", "Box Plot", "Pie Chart"]
    )

    numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns
    all_columns = df.columns

    # Define x and y axis
    x_axis = st.sidebar.selectbox("Select X-axis", options=all_columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", options=all_columns)

    color_option = st.sidebar.selectbox("Color by (Optional)", options=[None] + list(all_columns))

    # Create chart
    fig = None
    if chart_type == "Scatter Plot":
        fig = px.scatter(df, x=x_axis, y=y_axis, color=color_option,
                         title=f"Scatter Plot of {y_axis} vs {x_axis}")
    elif chart_type == "Line Chart":
        fig = px.line(df, x=x_axis, y=y_axis, color=color_option,
                      title=f"Line Chart of {y_axis} vs {x_axis}")
    elif chart_type == "Bar Chart":
        fig = px.bar(df, x=x_axis, y=y_axis, color=color_option,
                     title=f"Bar Chart of {y_axis} by {x_axis}")
    elif chart_type == "Histogram":
        fig = px.histogram(df, x=x_axis, color=color_option,
                           title=f"Histogram of {x_axis}")
    elif chart_type == "Box Plot":
        fig = px.box(df, x=x_axis, y=y_axis, color=color_option,
                     title=f"Box Plot of {y_axis} by {x_axis}")
    elif chart_type == "Pie Chart":
        fig = px.pie(df, names=x_axis, values=y_axis, color=color_option,
                     title=f"Pie Chart of {y_axis} by {x_axis}")

    # Show visualization
    if fig:
        st.plotly_chart(fig, use_container_width=True)

    # Allow multiple visualizations
    st.subheader("➕ Add Another Visualization")
    if st.checkbox("Add second visualization"):
        chart_type2 = st.selectbox(
            "Choose another chart type:",
            ["Scatter Plot", "Line Chart", "Bar Chart", "Histogram", "Box Plot", "Pie Chart"],
            key="chart2"
        )
        x_axis2 = st.selectbox("Select X-axis for second chart", options=all_columns, key="x2")
        y_axis2 = st.selectbox("Select Y-axis for second chart", options=all_columns, key="y2")
        color_option2 = st.selectbox("Color by (Optional)", options=[None] + list(all_columns), key="c2")

        fig2 = None
        if chart_type2 == "Scatter Plot":
            fig2 = px.scatter(df, x=x_axis2, y=y_axis2, color=color_option2)
        elif chart_type2 == "Line Chart":
            fig2 = px.line(df, x=x_axis2, y=y_axis2, color=color_option2)
        elif chart_type2 == "Bar Chart":
            fig2 = px.bar(df, x=x_axis2, y=y_axis2, color=color_option2)
        elif chart_type2 == "Histogram":
            fig2 = px.histogram(df, x=x_axis2, color=color_option2)
        elif chart_type2 == "Box Plot":
            fig2 = px.box(df, x=x_axis2, y=y_axis2, color=color_option2)
        elif chart_type2 == "Pie Chart":
            fig2 = px.pie(df, names=x_axis2, values=y_axis2, color=color_option2)

        if fig2:
            st.plotly_chart(fig2, use_container_width=True)

else:
    st.info("👆 Please upload a CSV or Excel file to begin.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/python/)")
