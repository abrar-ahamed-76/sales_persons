# Salesman Project

A complete data analysis pipeline demonstrating the use of **NumPy**, **Pandas**, **Matplotlib**, **Seaborn**, **Plotly**, and **Pandas plotting** to generate, analyze, and visualize sales performance data.

## Features

- **Data Generation** (`sales_data_generator.py`)
  - Uses **NumPy** to create random sales records (salespeople, regions, products, units, prices).
  - Uses **Pandas** to structure and persist the data as `sales_data.csv`.

- **Sales Analytics** (`sales_analytics.py`)
  - Loads data with **Pandas**.
  - Computes total revenue, top-performing salesperson, regional breakdown, and monthly trends.

- **Basic Visualizations** (`visualizations.py`)
  - Uses **Matplotlib** to generate publication-ready charts:
    - Bar chart: Revenue by salesperson
    - Pie chart: Sales share by region
    - Line chart: Monthly revenue trend
    - Histogram: Distribution of transaction amounts

- **Comprehensive Chart Gallery** (`chart_gallery.py`)
  - **31 chart types** across 4 major Python visualization libraries:
    - **Matplotlib (13)**: scatter, bubble, stacked bar, grouped bar, area, boxplot, violin, heatmap, donut, radar, waterfall, lollipop, hexbin
    - **Seaborn (7)**: pairplot, jointplot, regression, countplot, swarmplot, KDE, clustermap
    - **Plotly (7)**: interactive line, interactive bar, interactive pie/donut, interactive scatter, 3D scatter, sunburst, treemap
    - **Pandas (4)**: parallel coordinates, Andrews curves, hexbin, scatter matrix

- **Orchestration** (`main.py`)
  - Single entry point that runs the entire pipeline end-to-end.
  - Optional `--gallery` flag to generate all 31 chart types.

## Project Structure

```
.
├── main.py                   # Entry-point script
├── sales_data_generator.py   # NumPy + Pandas data generation
├── sales_analytics.py        # Pandas analytics engine
├── visualizations.py         # Matplotlib basic plotting (4 charts)
├── chart_gallery.py          # Comprehensive gallery (31 charts)
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── sales_data.csv            # Generated dataset (after first run)
└── output_plots/             # Generated charts (after first run)
```

## Installation

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

### Run the basic pipeline (4 charts):
```bash
python main.py
```

### Run the full pipeline with comprehensive chart gallery (31 charts):
```bash
python main.py --gallery
```

### Run only the chart gallery:
```bash
python chart_gallery.py
```

On the first run, the script will:
1. Generate 1,000 synthetic sales records.
2. Print a detailed analytics report to the console.
3. Save visualization images to the `output_plots/` folder.

## Sample Output

### Console Report
```
==================================================
SALES ANALYTICS REPORT
==================================================

Total Revenue:       $6,245,123.45
Total Transactions:  1000
Average Order Value: $6,245.12

Top Salesperson:     Alice ($1,432,567.89)

Revenue by Region:
   North: $1,890,123.45
    West: $1,654,321.09
  ...
```

### Generated Plots (Basic - 4 charts)
- `output_plots/revenue_by_salesperson.png`
- `output_plots/sales_by_region.png`
- `output_plots/monthly_trend.png`
- `output_plots/transaction_distribution.png`

### Generated Plots (Gallery - 31 charts)
**Matplotlib:**
- `output_plots/matplotlib_scatter.png`
- `output_plots/matplotlib_bubble.png`
- `output_plots/matplotlib_stacked_bar.png`
- `output_plots/matplotlib_grouped_bar.png`
- `output_plots/matplotlib_area.png`
- `output_plots/matplotlib_boxplot.png`
- `output_plots/matplotlib_violin.png`
- `output_plots/matplotlib_heatmap.png`
- `output_plots/matplotlib_donut.png`
- `output_plots/matplotlib_radar.png`
- `output_plots/matplotlib_waterfall.png`
- `output_plots/matplotlib_lollipop.png`
- `output_plots/matplotlib_hexbin.png`

**Seaborn:**
- `output_plots/seaborn_pairplot.png`
- `output_plots/seaborn_jointplot.png`
- `output_plots/seaborn_regression.png`
- `output_plots/seaborn_countplot.png`
- `output_plots/seaborn_swarmplot.png`
- `output_plots/seaborn_kde.png`
- `output_plots/seaborn_clustermap.png`

**Plotly (HTML + PNG):**
- `output_plots/plotly_interactive_line.html` / `.png`
- `output_plots/plotly_interactive_bar.html` / `.png`
- `output_plots/plotly_interactive_pie.html` / `.png`
- `output_plots/plotly_interactive_scatter.html` / `.png`
- `output_plots/plotly_3d_scatter.html` / `.png`
- `output_plots/plotly_sunburst.html` / `.png`
- `output_plots/plotly_treemap.html` / `.png`

**Pandas:**
- `output_plots/pandas_parallel_coordinates.png`
- `output_plots/pandas_andrews_curves.png`
- `output_plots/pandas_hexbin.png`
- `output_plots/pandas_scatter_matrix.png`

## Dependencies

- numpy
- pandas
- matplotlib
- seaborn
- plotly
- openpyxl

## License

This project is provided for educational and demonstration purposes.
