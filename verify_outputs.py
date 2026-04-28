import os

expected = [
    'output_plots/revenue_by_salesperson.png', 'output_plots/sales_by_region.png',
    'output_plots/monthly_trend.png', 'output_plots/transaction_distribution.png',
    'output_plots/matplotlib_scatter.png', 'output_plots/matplotlib_bubble.png',
    'output_plots/matplotlib_stacked_bar.png', 'output_plots/matplotlib_grouped_bar.png',
    'output_plots/matplotlib_area.png', 'output_plots/matplotlib_boxplot.png',
    'output_plots/matplotlib_violin.png', 'output_plots/matplotlib_heatmap.png',
    'output_plots/matplotlib_donut.png', 'output_plots/matplotlib_radar.png',
    'output_plots/matplotlib_waterfall.png', 'output_plots/matplotlib_lollipop.png',
    'output_plots/matplotlib_hexbin.png', 'output_plots/seaborn_pairplot.png',
    'output_plots/seaborn_jointplot.png', 'output_plots/seaborn_regression.png',
    'output_plots/seaborn_countplot.png', 'output_plots/seaborn_swarmplot.png',
    'output_plots/seaborn_kde.png', 'output_plots/seaborn_clustermap.png',
    'output_plots/plotly_interactive_line.html', 'output_plots/plotly_interactive_line.png',
    'output_plots/plotly_interactive_bar.html', 'output_plots/plotly_interactive_bar.png',
    'output_plots/plotly_interactive_pie.html', 'output_plots/plotly_interactive_pie.png',
    'output_plots/plotly_interactive_scatter.html', 'output_plots/plotly_interactive_scatter.png',
    'output_plots/plotly_3d_scatter.html', 'output_plots/plotly_3d_scatter.png',
    'output_plots/plotly_sunburst.html', 'output_plots/plotly_sunburst.png',
    'output_plots/plotly_treemap.html', 'output_plots/plotly_treemap.png',
    'output_plots/pandas_parallel_coordinates.png', 'output_plots/pandas_andrews_curves.png',
    'output_plots/pandas_hexbin.png', 'output_plots/pandas_scatter_matrix.png',
]

missing = [f for f in expected if not os.path.exists(f)]
print(f'Total expected: {len(expected)}')
print(f'Found: {len(expected) - len(missing)}')
if missing:
    print(f'Missing ({len(missing)}):')
    for m in missing:
        print('  -', m)
else:
    print('All expected outputs are present!')

