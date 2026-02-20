import pandas as pd
import streamlit as st
from visualizations.theme import set_seaborn_theme
from visualizations import seaborn_plots as sp
from visualizations import plotly_plots as pp

#Page Configuration
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📉",
    layout="wide"
)
st.title("Interactive Sales Dashboard")

#Data Loading
@st.cache_data
def load_data(filepath: str):
    df = pd.read_csv(filepath)

    #Robust date parsing
    df["Date"] = pd.to_datetime(
        df["Date"],
        dayfirst=True,
        errors="coerce",
        format="mixed"
    )

    # Drop rows where date could not be parsed
    df = df.dropna(subset=["Date"])

    return df

df = load_data("data/sales_data.csv")

#Sidebar Filters
st.sidebar.header("Filters")

#region filter
selected_region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

#product filter
selected_product = st.sidebar.multiselect(
    "Select Product",
    options=df["Product"].unique(),
    default=df["Product"].unique()
)

#apply filter to dataframe
filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Product"].isin(selected_product))
]

#stop execution if filters produce empty dataset
if filtered_df.empty:
    st.warning("⚠️ No data available for selected filters. Please adjust your selections.")
    st.stop()

#KPI Section (Business Metrics)
#Key performance indicators provide quick executive-level insight.
total_revenue = filtered_df["Total_Sales"].sum()
total_orders = len(filtered_df)

#identify highest revenue-generating product
top_product = (
    filtered_df.groupby("Product")["Total_Sales"]
    .sum()
    .idxmax()
)

#display KPIs in horizontal layout
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Top Product", top_product)

#Interactive Visualizations (Plotly)
#These charts support hover interactions and dynamic filtering.
st.subheader("Sales Trend")
st.plotly_chart(pp.sales_trend(filtered_df), use_container_width=True)

st.subheader("Product Performance")
st.plotly_chart(pp.product_performance(filtered_df), use_container_width=True)

st.subheader("Customer Segmentation")
st.plotly_chart(pp.customer_segmentation(filtered_df), use_container_width=True)

#Static Statistical Visualizations
st.subheader("Statistical Analysis")

set_seaborn_theme()   #apply consistent styling

#generate and save plots
box_path = sp.box_price_distribution(filtered_df)
violin_path = sp.violin_quantity_distribution(filtered_df)
heatmap_path = sp.correlation_heatmap(filtered_df)
region_path = sp.sales_by_region(filtered_df)

#display plots in grid layout
col1, col2 = st.columns(2)
col1.image(box_path)
col2.image(violin_path)

col3, col4 = st.columns(2)

#handles scenarios where heatmap cannot be generated due to insufficient numeric data
if heatmap_path:
    col3.image(heatmap_path)
else:
    col3.info("Not enough data to generate heatmap.")

col4.image(region_path)
#Completion message
st.success("Analysis Done Successfully")