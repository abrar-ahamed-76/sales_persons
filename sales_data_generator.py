import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os


def generate_sales_data(num_records=1000, output_path='sales_data.csv'):
    """Generate a synthetic sales dataset and save it to a CSV file."""
    np.random.seed(42)

    salespeople = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    regions = ['North', 'South', 'East', 'West']
    products = ['Widget', 'Gadget', 'Thingama', 'Doohickey']

    # Generate random dates within the last year
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    random_dates = [
        start_date + timedelta(days=int(np.random.randint(0, 366)))
        for _ in range(num_records)
    ]

    data = {
        'Date': random_dates,
        'Salesperson': np.random.choice(salespeople, num_records),
        'Region': np.random.choice(regions, num_records),
        'Product': np.random.choice(products, num_records),
        'Units_Sold': np.random.randint(1, 50, num_records),
        'Unit_Price': np.round(np.random.uniform(10, 500, num_records), 2)
    }

    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').reset_index(drop=True)
    df.to_csv(output_path, index=False)

    print(f"Sales data generated successfully: {output_path} ({num_records} records)")
    return df


if __name__ == "__main__":
    generate_sales_data()

