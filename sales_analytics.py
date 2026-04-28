import pandas as pd
import numpy as np


def load_data(filepath='sales_data.csv'):
    """Load sales data and compute total revenue per transaction."""
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Total_Revenue'] = df['Units_Sold'] * df['Unit_Price']
    return df


def analyze_sales(filepath='sales_data.csv'):
    """Compute and print key sales metrics."""
    df = load_data(filepath)

    print("=" * 50)
    print("SALES ANALYTICS REPORT")
    print("=" * 50)

    # Overall metrics
    total_revenue = df['Total_Revenue'].sum()
    total_transactions = len(df)
    avg_order_value = df['Total_Revenue'].mean()

    print(f"\nTotal Revenue:       ${total_revenue:,.2f}")
    print(f"Total Transactions:  {total_transactions}")
    print(f"Average Order Value: ${avg_order_value:,.2f}")

    # Top salesperson
    sales_by_person = df.groupby('Salesperson')['Total_Revenue'].sum().sort_values(ascending=False)
    print(f"\nTop Salesperson:     {sales_by_person.index[0]} (${sales_by_person.iloc[0]:,.2f})")

    # Sales by region
    sales_by_region = df.groupby('Region')['Total_Revenue'].sum().sort_values(ascending=False)
    print("\nRevenue by Region:")
    for region, revenue in sales_by_region.items():
        print(f"  {region:>6}: ${revenue:>12,.2f}")

    # Monthly trends
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Total_Revenue'].sum()
    print("\nMonthly Revenue Trend (last 6 months):")
    for month, revenue in monthly_sales.tail(6).items():
        print(f"  {month}: ${revenue:,.2f}")

    return {
        'total_revenue': total_revenue,
        'total_transactions': total_transactions,
        'avg_order_value': avg_order_value,
        'sales_by_person': sales_by_person,
        'sales_by_region': sales_by_region,
        'monthly_sales': monthly_sales
    }


if __name__ == "__main__":
    analyze_sales()

