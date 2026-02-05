import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
from pathlib import Path

#CONFIGURATION
DATA_PATH = "data/expenses.csv"
VIZ_DIR = Path("visualizations")
REPORT_DIR = Path("report")

VIZ_DIR.mkdir(exist_ok = True)
REPORT_DIR.mkdir(exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

#FUNCTIONS
def load_data(path):
    logging.info(f"Loading dataset...")
    df = pd.read_csv(path)
    logging.info(f"Loaded {len(df)} records.")
    return df

def validate_data(df):
    required_cols  = ["date", "category", "amount"]
    
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"Missing required columns. Required: {required_cols}")
    
    if df.isnull().sum().any():
        logging.warning("Missing values detected - filling with median/mode.")
        
    return df

def clean_data(df):
    df["date"] = pd.to_datetime(df["date"], errors = "coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors = "coerce")
    
    df["amount"] = df["amount"].fillna(df["amount"].median())
    df["category"] = df["category"].fillna(df["category"].mode()[0])
    
    df = df.dropna(subset = ["date"])
    
    if df["date"].dt.tz is not None:
        df["date"] = df["date"].dt.tz_convert(None)
    
    df["month"] = df["date"].dt.to_period("M")
    
    return df

def analyze_data(df):
    summary = {
        "total_spent": df.amount.sum(),
        "avg_spend": df.amount.mean(),
        "max_spend": df.amount.max(),
        "min_spend": df.amount.min()
    }
    
    category_summary = df.groupby("category")["amount"].sum().sort_values(ascending = False)
    monthly_summary = df.groupby("month")["amount"].sum()
    
    return summary, category_summary, monthly_summary

def visualize_data(category_summary, monthly_summary):
    
    #Bar chart for category spending
    category_summary.plot(kind = "bar", figsize = (10, 5))
    plt.title("Expense by Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig(VIZ_DIR /"category_bar.png")
    plt.clf()
    
    #Pie chart for expense distribution
    category_summary.plot(kind = "pie", autopct = "%1.1f%%", figsize = (6, 6))
    plt.title("Expense Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(VIZ_DIR / "expense_pie.png")
    plt.clf()
    
    #Line chart for monthly spending
    monthly_summary.sort_index().plot(kind = "line", marker = "o", figsize = (10, 5))
    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig(VIZ_DIR / "monthly_trend.png")
    plt.clf()

def generate_report(summary, category, monthly):
    with open(REPORT_DIR/ "report.md", "w") as f:
        f.write("# Personal Expense Analysis Report\n\n")
        
        f.write("## Summary Statistics\n")
        for k,v in summary.items():
            f.write(f"{k}: {round(v, 2)}\n")
            
        f.write("\n## Category Spending\n")
        f.write(category.to_string())
        
        f.write("\n\n## Monthly Spending\n")
        f.write(monthly.to_string())
        
        f.write("\n\n## Insights\n")
        f.write("- The highest spending category is **{}** with a total of ${:.2f}.\n".format(category.idxmax(), category.max()))
    
#MAIN EXECUTION
def main():
    try:
        df = load_data(DATA_PATH)
        df = validate_data(df)
        df = clean_data(df)
    
        summary, category_summary, monthly_summary = analyze_data(df)
    
        visualize_data(category_summary, monthly_summary)
    
        generate_report(summary, category_summary, monthly_summary)
    
        logging.info("Analysis complete. Report and visualizations saved.")
    
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
    
if __name__ == "__main__":
    main()