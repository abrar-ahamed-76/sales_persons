"""
Salesman Project - Main Entry Point

Orchestrates the full pipeline:
  1. Generate synthetic sales data (if missing)
  2. Run analytics and print summary report
  3. Generate Matplotlib visualizations (original 4 charts)
  4. Generate comprehensive chart gallery (31 chart types)
"""

import os
import sys
from sales_data_generator import generate_sales_data
from sales_analytics import analyze_sales
from visualizations import generate_all_plots


def main(run_gallery=False):
    csv_path = 'sales_data.csv'

    # Step 1: Generate data if it doesn't already exist
    if not os.path.exists(csv_path):
        print("Step 1: Generating sales data...")
        generate_sales_data(output_path=csv_path)
    else:
        print("Step 1: Sales data already exists. Skipping generation.")

    # Step 2: Run analytics
    print("\nStep 2: Running sales analytics...")
    analyze_sales(filepath=csv_path)

    # Step 3: Generate original visualizations
    print("\nStep 3: Generating basic visualizations...")
    generate_all_plots(filepath=csv_path)

    # Step 4: Generate comprehensive chart gallery (optional)
    if run_gallery:
        print("\nStep 4: Generating comprehensive chart gallery...")
        from chart_gallery import run_gallery
        run_gallery(filepath=csv_path)

    print("\n" + "=" * 50)
    print("Salesman Project Execution Complete!")
    print("=" * 50)
    print("\nOutputs:")
    print(f"  - Raw data:       {csv_path}")
    print(f"  - Plots folder:   output_plots/")
    if run_gallery:
        print("\nChart Gallery: 31 chart types generated!")
        print("  Includes: Matplotlib (13), Seaborn (7), Plotly (7), Pandas (4)")


if __name__ == "__main__":
    # Allow: python main.py --gallery
    run_gallery_flag = '--gallery' in sys.argv
    main(run_gallery=run_gallery_flag)
