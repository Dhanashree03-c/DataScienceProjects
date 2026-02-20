import pandas as pd
import streamlit as st
from visualizations.theme import set_seaborn_theme
from visualizations import seaborn_plots as sp
from visualizations import plotly_plots as pp

#Page Configuration
st.set_page_config(
    page_title = "Sales Analytics Dashboard",
    page_icon = "📉",
    layout = "wide"
)
st.title("Interactive Sales Dashboard")
st.markdown(
    "Interactive dashboard for analyzing sales trends, product performance, "
    "customer behavior, and regional revenue distribution."
)

#Data Loading
@st.cache_data(show_spinner=False)
def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)

    #Robust date parsing
    df["Date"] = pd.to_datetime(
        df["Date"],
        dayfirst = True,
        errors = "coerce",
        format = "mixed"
    )

    # Drop rows where date could not be parsed
    df = df.dropna(subset=["Date"])
    
    #Ensure numeric types
    numeric_cols = ["Quantity", "Price", "Total_Sales"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    return df

df = load_data("data/sales_data.csv")

if df.empty:
    st.error("Dataset is empty or could not be loaded.")
    st.stop()

#Sidebar Filters
st.sidebar.header("Filters")

#Date Range Filter
min_date = df["Date"].min()
max_date = df["Date"].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value = (min_date, max_date),
    min_value = min_date,
    max_value = max_date,
)

#region filter
selected_region = st.sidebar.multiselect(
    "Select Region",
    options = sorted(df["Region"].unique()),
    default = sorted(df["Region"].unique())
)

#product filter
selected_product = st.sidebar.multiselect(
    "Select Product",
    options = sorted(df["Product"].unique()),
    default = sorted(df["Product"].unique())
)

#apply filter to dataframe
filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Product"].isin(selected_product))
]

#Filter Dataset
filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Product"].isin(selected_product)) &
    (df["Date"] >= pd.to_datetime(date_range[0])) &
    (df["Date"] <= pd.to_datetime(date_range[1]))
]

#stop execution if filters produce empty dataset
if filtered_df.empty:
    st.warning("⚠️ No data available for selected filters. Please adjust filters.")
    st.stop()

#KPI Section (Business Metrics)
#Key performance indicators provide quick executive-level insight.
st.markdown("---")
st.markdown("## Executive Summary")
total_revenue = filtered_df["Total_Sales"].sum()
total_orders = filtered_df.shape[0]
avg_order_value = total_revenue / total_orders

#identify highest revenue-generating product
top_product = (
    filtered_df.groupby("Product")["Total_Sales"].sum().idxmax()
)

best_region = (
    filtered_df.groupby("Region")["Total_Sales"].sum().idxmax()
)

#display KPIs in horizontal layout
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg Order Value", f"₹{avg_order_value:,.0f}")
col4.metric("Top Product", top_product)

#Interactive Visualizations (Plotly)
#These charts support hover interactions and dynamic filtering.
st.markdown("---")
st.markdown("## Sales Trend Analysis")
st.markdown(
    "This chart illustrates daily revenue fluctuations. "
    "Peaks may indicate promotional activity or seasonal demand."
)
st.plotly_chart(pp.sales_trend(filtered_df), use_container_width=True)

st.markdown("---")
st.markdown("## Product Performance")
st.markdown(
    "Revenue contribution by product category. "
    "Helps identify high-performing products."
)
st.plotly_chart(pp.product_performance(filtered_df), use_container_width=True)

st.markdown("---")
st.markdown("## Customer Segmentation")
st.markdown(
    "Customer purchasing behavior based on total quantity and total revenue."
)
st.plotly_chart(pp.customer_segmentation(filtered_df), use_container_width=True)

#Static Statistical Visualizations
st.markdown("---")
st.markdown("## Statistical Insights")

set_seaborn_theme()   #apply consistent styling

#generate and save plots
box_path = sp.box_price_distribution(filtered_df)
violin_path = sp.violin_quantity_distribution(filtered_df)
heatmap_path = sp.correlation_heatmap(filtered_df)
region_path = sp.sales_by_region(filtered_df)

#display plots in grid layout
col1, col2 = st.columns(2)
col1.image(box_path, caption="Price Distribution by Product")
col2.image(violin_path, caption="Quantity Distribution by Product")

col3, col4 = st.columns(2)

#handles scenarios where heatmap cannot be generated due to insufficient numeric data
if heatmap_path:
    col3.image(heatmap_path, caption="Correlation Heatmap")
else:
    col3.info("Not enough numeric data to generate heatmap.")

col4.image(region_path, caption="Revenue by Region")

#Completion message
st.markdown("---")
st.success("Dashboard loaded successfully.")
st.caption("Built using Streamlit, Seaborn, Plotly, and Pandas.")