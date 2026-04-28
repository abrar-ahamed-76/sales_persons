"""Comprehensive Chart Gallery for Python Visualization Libraries.

This module demonstrates 31 chart types across Matplotlib, Seaborn, Plotly,
and Pandas using the synthetic sales dataset.

Categories:
    A. Matplotlib Charts (13 types)
    B. Seaborn Charts (7 types)
    C. Plotly Interactive Charts (7 types)
    D. Pandas Native Charts (4 types)
"""

import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

warnings.filterwarnings('ignore')

# Optional imports with graceful fallback
try:
    import seaborn as sns
    HAS_SEABORN = True
except ImportError:
    HAS_SEABORN = False

try:
    import plotly.express as px
    import plotly.graph_objects as go
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False


OUTPUT_DIR = 'output_plots'
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_sales_data(filepath='sales_data.csv'):
    """Load and preprocess sales data."""
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Total_Revenue'] = df['Units_Sold'] * df['Unit_Price']
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    df['Year'] = df['Date'].dt.year
    return df


# ============================================================
# A. MATPLOTLIB CHARTS
# ============================================================

def matplotlib_scatter(df):
    """1. Scatter plot: Units Sold vs Unit Price colored by Region."""
    fig, ax = plt.subplots(figsize=(10, 6))
    regions = df['Region'].unique()
    colors = plt.cm.tab10(np.linspace(0, 1, len(regions)))
    for region, color in zip(regions, colors):
        subset = df[df['Region'] == region]
        ax.scatter(subset['Units_Sold'], subset['Unit_Price'],
                   label=region, alpha=0.6, s=50, color=color)
    ax.set_title('Scatter Plot: Units Sold vs Unit Price', fontsize=14, fontweight='bold')
    ax.set_xlabel('Units Sold')
    ax.set_ylabel('Unit Price ($)')
    ax.legend(title='Region')
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_scatter.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_scatter.png")


def matplotlib_bubble(df):
    """2. Bubble chart: Revenue by Region with size = total revenue."""
    region_revenue = df.groupby('Region')['Total_Revenue'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(8, 8))
    sizes = (region_revenue['Total_Revenue'] / region_revenue['Total_Revenue'].max()) * 1000
    colors = cm.viridis(np.linspace(0, 1, len(region_revenue)))
    ax.scatter(region_revenue['Region'], region_revenue['Total_Revenue'],
               s=sizes, c=colors, alpha=0.6, edgecolors='black', linewidth=1)
    for i, txt in enumerate(region_revenue['Region']):
        ax.annotate(txt, (region_revenue['Region'].iloc[i],
                          region_revenue['Total_Revenue'].iloc[i]),
                    ha='center', fontsize=10)
    ax.set_title('Bubble Chart: Revenue by Region', fontsize=14, fontweight='bold')
    ax.set_xlabel('Region')
    ax.set_ylabel('Total Revenue ($)')
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_bubble.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_bubble.png")


def matplotlib_stacked_bar(df):
    """3. Stacked bar chart: Monthly revenue stacked by region."""
    pivot = df.pivot_table(values='Total_Revenue', index='Month',
                           columns='Region', aggfunc='sum', fill_value=0)
    fig, ax = plt.subplots(figsize=(12, 6))
    pivot.plot(kind='bar', stacked=True, ax=ax, colormap='Set2')
    ax.set_title('Stacked Bar: Monthly Revenue by Region', fontsize=14, fontweight='bold')
    ax.set_xlabel('Month')
    ax.set_ylabel('Revenue ($)')
    ax.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_stacked_bar.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_stacked_bar.png")


def matplotlib_grouped_bar(df):
    """4. Grouped bar chart: Salesperson revenue by product."""
    pivot = df.pivot_table(values='Total_Revenue', index='Salesperson',
                           columns='Product', aggfunc='sum', fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 6))
    pivot.plot(kind='bar', ax=ax, colormap='Pastel1')
    ax.set_title('Grouped Bar: Revenue by Salesperson & Product', fontsize=14, fontweight='bold')
    ax.set_xlabel('Salesperson')
    ax.set_ylabel('Revenue ($)')
    ax.legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=0)
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_grouped_bar.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_grouped_bar.png")


def matplotlib_area(df):
    """5. Area chart: Cumulative monthly revenue."""
    monthly = df.groupby('Month')['Total_Revenue'].sum().sort_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.fill_between(range(len(monthly)), monthly.values, color='skyblue', alpha=0.4)
    ax.plot(range(len(monthly)), monthly.values, color='Slateblue', alpha=0.6, linewidth=2)
    ax.set_xticks(range(len(monthly)))
    ax.set_xticklabels(monthly.index, rotation=45)
    ax.set_title('Area Chart: Monthly Revenue Trend', fontsize=14, fontweight='bold')
    ax.set_xlabel('Month')
    ax.set_ylabel('Revenue ($)')
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_area.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_area.png")


def matplotlib_boxplot(df):
    """6. Box plot: Revenue distribution by region."""
    fig, ax = plt.subplots(figsize=(10, 6))
    data_to_plot = [df[df['Region'] == r]['Total_Revenue'].values for r in df['Region'].unique()]
    bp = ax.boxplot(data_to_plot, labels=df['Region'].unique(), patch_artist=True)
    colors = plt.cm.Set3(np.linspace(0, 1, len(bp['boxes'])))
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    ax.set_title('Box Plot: Revenue Distribution by Region', fontsize=14, fontweight='bold')
    ax.set_xlabel('Region')
    ax.set_ylabel('Revenue ($)')
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_boxplot.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_boxplot.png")


def matplotlib_violin(df):
    """7. Violin plot: Revenue distribution by salesperson."""
    fig, ax = plt.subplots(figsize=(10, 6))
    people = df['Salesperson'].unique()
    positions = np.arange(1, len(people) + 1)
    for i, person in enumerate(people):
        data = df[df['Salesperson'] == person]['Total_Revenue']
        parts = ax.violinplot([data.values], positions=[positions[i]], showmeans=True)
        for pc in parts['bodies']:
            pc.set_facecolor(plt.cm.Set2(i))
            pc.set_alpha(0.7)
    ax.set_xticks(positions)
    ax.set_xticklabels(people)
    ax.set_title('Violin Plot: Revenue Distribution by Salesperson', fontsize=14, fontweight='bold')
    ax.set_xlabel('Salesperson')
    ax.set_ylabel('Revenue ($)')
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_violin.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_violin.png")


def matplotlib_heatmap(df):
    """8. Heatmap: Salesperson vs Product revenue matrix."""
    pivot = df.pivot_table(values='Total_Revenue', index='Salesperson',
                           columns='Product', aggfunc='sum', fill_value=0)
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(pivot.values, cmap='YlOrRd', aspect='auto')
    ax.set_xticks(np.arange(len(pivot.columns)))
    ax.set_yticks(np.arange(len(pivot.index)))
    ax.set_xticklabels(pivot.columns)
    ax.set_yticklabels(pivot.index)
    for i in range(len(pivot.index)):
        for j in range(len(pivot.columns)):
            ax.text(j, i, f"${pivot.values[i, j]:,.0f}",
                    ha="center", va="center", color="black", fontsize=8)
    ax.set_title('Heatmap: Revenue by Salesperson & Product', fontsize=14, fontweight='bold')
    fig.colorbar(im, ax=ax, label='Revenue ($)')
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_heatmap.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_heatmap.png")


def matplotlib_donut(df):
    """9. Donut chart: Sales share by region."""
    revenue = df.groupby('Region')['Total_Revenue'].sum()
    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        revenue, labels=revenue.index, autopct='%1.1f%%',
        startangle=140, colors=plt.cm.Pastel1.colors,
        wedgeprops=dict(width=0.4), textprops={'fontsize': 12}
    )
    ax.set_title('Donut Chart: Sales Share by Region', fontsize=14, fontweight='bold')
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_donut.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_donut.png")


def matplotlib_radar(df):
    """10. Radar/Spider chart: Salesperson performance across metrics."""
    metrics = ['Total_Revenue', 'Units_Sold', 'Avg_Price', 'Transaction_Count']
    person_stats = df.groupby('Salesperson').agg(
        Total_Revenue=('Total_Revenue', 'sum'),
        Units_Sold=('Units_Sold', 'sum'),
        Avg_Price=('Unit_Price', 'mean'),
        Transaction_Count=('Total_Revenue', 'count')
    )
    person_norm = (person_stats - person_stats.min()) / (person_stats.max() - person_stats.min())
    
    categories = metrics
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    colors = plt.cm.tab10(np.linspace(0, 1, len(person_norm)))
    for idx, (person, row) in enumerate(person_norm.iterrows()):
        values = row.values.tolist()
        values += values[:1]
        ax.plot(angles, values, 'o-', linewidth=2, label=person, color=colors[idx])
        ax.fill(angles, values, alpha=0.15, color=colors[idx])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 1)
    ax.set_title('Radar Chart: Salesperson Performance', fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_radar.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_radar.png")


def matplotlib_waterfall(df):
    """11. Waterfall chart: Monthly revenue changes."""
    monthly = df.groupby('Month')['Total_Revenue'].sum().sort_index()
    changes = monthly.diff().fillna(monthly.iloc[0])
    
    fig, ax = plt.subplots(figsize=(12, 6))
    running_total = 0
    colors = ['green' if x >= 0 else 'red' for x in changes]
    for i, (month, change) in enumerate(changes.items()):
        ax.bar(i, change, bottom=running_total, color=colors[i], edgecolor='black', alpha=0.8)
        running_total += change
        ax.text(i, running_total - change/2, f'${change:,.0f}', ha='center', va='center', fontsize=8)
    
    ax.set_xticks(range(len(changes)))
    ax.set_xticklabels(monthly.index, rotation=45)
    ax.set_title('Waterfall Chart: Monthly Revenue Changes', fontsize=14, fontweight='bold')
    ax.set_xlabel('Month')
    ax.set_ylabel('Revenue Change ($)')
    ax.axhline(0, color='black', linewidth=0.8)
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_waterfall.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_waterfall.png")


def matplotlib_lollipop(df):
    """12. Lollipop chart: Revenue by salesperson."""
    revenue = df.groupby('Salesperson')['Total_Revenue'].sum().sort_values(ascending=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hlines(y=revenue.index, xmin=0, xmax=revenue.values, color='steelblue', alpha=0.7, linewidth=2)
    ax.scatter(revenue.values, revenue.index, color='steelblue', s=100, alpha=1, zorder=3)
    ax.set_title('Lollipop Chart: Revenue by Salesperson', fontsize=14, fontweight='bold')
    ax.set_xlabel('Revenue ($)')
    ax.set_ylabel('Salesperson')
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_lollipop.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_lollipop.png")


def matplotlib_hexbin(df):
    """13. Hexbin plot: Units Sold vs Total Revenue density."""
    fig, ax = plt.subplots(figsize=(10, 6))
    hb = ax.hexbin(df['Units_Sold'], df['Total_Revenue'], gridsize=20, cmap='inferno', mincnt=1)
    ax.set_title('Hexbin Plot: Units Sold vs Revenue Density', fontsize=14, fontweight='bold')
    ax.set_xlabel('Units Sold')
    ax.set_ylabel('Total Revenue ($)')
    cb = fig.colorbar(hb, ax=ax)
    cb.set_label('Count')
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/matplotlib_hexbin.png', dpi=300)
    plt.close(fig)
    print("Saved: matplotlib_hexbin.png")


# ============================================================
# B. SEABORN CHARTS
# ============================================================

def seaborn_pairplot(df):
    """14. Pairplot: Relationships between numerical variables."""
    if not HAS_SEABORN:
        print("Seaborn not installed. Skipping pairplot.")
        return
    numeric_df = df[['Units_Sold', 'Unit_Price', 'Total_Revenue']].sample(min(500, len(df)))
    g = sns.pairplot(numeric_df, diag_kind='kde', plot_kws={'alpha': 0.5}, corner=True)
    g.fig.suptitle('Seaborn Pairplot: Numeric Relationships', y=1.02, fontsize=14, fontweight='bold')
    g.fig.savefig(f'{OUTPUT_DIR}/seaborn_pairplot.png', dpi=300)
    plt.close(g.fig)
    print("Saved: seaborn_pairplot.png")


def seaborn_jointplot(df):
    """15. Jointplot: Units Sold vs Revenue with KDE margins."""
    if not HAS_SEABORN:
        print("Seaborn not installed. Skipping jointplot.")
        return
    sample = df.sample(min(500, len(df)))
    g = sns.jointplot(data=sample, x='Units_Sold', y='Total_Revenue',
                      kind='kde', fill=True, cmap='mako', height=8)
    g.fig.suptitle('Seaborn Jointplot: Units Sold vs Revenue', y=1.02, fontsize=14, fontweight='bold')
    g.fig.savefig(f'{OUTPUT_DIR}/seaborn_jointplot.png', dpi=300)
    plt.close(g.fig)
    print("Saved: seaborn_jointplot.png")


def seaborn_regression(df):
    """16. Regression plot with confidence interval."""
    if not HAS_SEABORN:
        print("Seaborn not installed. Skipping regression plot.")
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    sample = df.sample(min(500, len(df)))
    sns.regplot(data=sample, x='Units_Sold', y='Total_Revenue',
                scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'}, ax=ax)
    ax.set_title('Seaborn Regression: Units Sold vs Revenue', fontsize=14, fontweight='bold')
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/seaborn_regression.png', dpi=300)
    plt.close(fig)
    print("Saved: seaborn_regression.png")


def seaborn_countplot(df):
    """17. Count plot: Number of transactions by product."""
    if not HAS_SEABORN:
        print("Seaborn not installed. Skipping countplot.")
        return
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x='Product', hue='Region', palette='viridis', ax=ax)
    ax.set_title('Seaborn Count Plot: Transactions by Product & Region', fontsize=14, fontweight='bold')
    ax.set_xlabel('Product')
    ax.set_ylabel('Count')
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/seaborn_countplot.png', dpi=300)
    plt.close(fig)
    print("Saved: seaborn_countplot.png")


def seaborn_swarmplot(df):
    """18. Swarm plot: Revenue distribution by product."""
    if not HAS_SEABORN:
        print("Seaborn not installed. Skipping swarmplot.")
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    sample = df.sample(min(200, len(df)))
    sns.swarmplot(data=sample, x='Product', y='Total_Revenue', hue='Region', palette='Set2', size=4, ax=ax)
    ax.set_title('Seaborn Swarm Plot: Revenue by Product', fontsize=14, fontweight='bold')
    ax.set_xlabel('Product')
    ax.set_ylabel('Revenue ($)')
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/seaborn_swarmplot.png', dpi=300)
    plt.close(fig)
    print("Saved: seaborn_swarmplot.png")


def seaborn_kde(df):
    """19. KDE plot: Revenue distribution by region."""
    if not HAS_SEABORN:
        print("Seaborn not installed. Skipping KDE plot.")
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    for region in df['Region'].unique():
        subset = df[df['Region'] == region]
        sns.kdeplot(data=subset, x='Total_Revenue', label=region, fill=True, alpha=0.3, ax=ax)
    ax.set_title('Seaborn KDE Plot: Revenue Distribution by Region', fontsize=14, fontweight='bold')
    ax.set_xlabel('Revenue ($)')
    ax.legend(title='Region')
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/seaborn_kde.png', dpi=300)
    plt.close(fig)
    print("Saved: seaborn_kde.png")


def seaborn_clustermap(df):
    """20. Clustermap: Correlation matrix of numeric features."""
    if not HAS_SEABORN:
        print("Seaborn not installed. Skipping clustermap.")
        return
    numeric_df = df[['Units_Sold', 'Unit_Price', 'Total_Revenue']].corr()
    g = sns.clustermap(numeric_df, annot=True, cmap='coolwarm', center=0,
                       figsize=(8, 8), linewidths=0.5)
    g.fig.suptitle('Seaborn Clustermap: Feature Correlations', y=1.02, fontsize=14, fontweight='bold')
    g.savefig(f'{OUTPUT_DIR}/seaborn_clustermap.png', dpi=300)
    plt.close()
    print("Saved: seaborn_clustermap.png")


# ============================================================
# C. PLOTLY INTERACTIVE CHARTS
# ============================================================

def plotly_interactive_line(df):
    """21. Interactive line chart: Monthly revenue trend."""
    if not HAS_PLOTLY:
        print("Plotly not installed. Skipping interactive line chart.")
        return
    monthly = df.groupby('Month', as_index=False)['Total_Revenue'].sum()
    fig = px.line(monthly, x='Month', y='Total_Revenue',
                  title='Plotly Interactive Line: Monthly Revenue Trend',
                  markers=True, line_shape='spline')
    fig.update_layout(hovermode='x unified')
    fig.write_html(f'{OUTPUT_DIR}/plotly_interactive_line.html')
    fig.write_image(f'{OUTPUT_DIR}/plotly_interactive_line.png', scale=2)
    print("Saved: plotly_interactive_line.html & .png")


def plotly_interactive_bar(df):
    """22. Interactive bar chart: Revenue by salesperson."""
    if not HAS_PLOTLY:
        print("Plotly not installed. Skipping interactive bar chart.")
        return
    revenue = df.groupby('Salesperson', as_index=False)['Total_Revenue'].sum().sort_values('Total_Revenue')
    fig = px.bar(revenue, x='Salesperson', y='Total_Revenue',
                 title='Plotly Interactive Bar: Revenue by Salesperson',
                 color='Total_Revenue', color_continuous_scale='Blues')
    fig.write_html(f'{OUTPUT_DIR}/plotly_interactive_bar.html')
    fig.write_image(f'{OUTPUT_DIR}/plotly_interactive_bar.png', scale=2)
    print("Saved: plotly_interactive_bar.html & .png")


def plotly_interactive_pie(df):
    """23. Interactive pie/donut chart: Sales by region."""
    if not HAS_PLOTLY:
        print("Plotly not installed. Skipping interactive pie chart.")
        return
    region_data = df.groupby('Region', as_index=False)['Total_Revenue'].sum()
    fig = px.pie(region_data, names='Region', values='Total_Revenue',
                 title='Plotly Interactive Pie: Sales Share by Region',
                 hole=0.4, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.write_html(f'{OUTPUT_DIR}/plotly_interactive_pie.html')
    fig.write_image(f'{OUTPUT_DIR}/plotly_interactive_pie.png', scale=2)
    print("Saved: plotly_interactive_pie.html & .png")


def plotly_interactive_scatter(df):
    """24. Interactive scatter: Units Sold vs Revenue with hover info."""
    if not HAS_PLOTLY:
        print("Plotly not installed. Skipping interactive scatter.")
        return
    sample = df.sample(min(800, len(df)))
    fig = px.scatter(sample, x='Units_Sold', y='Total_Revenue',
                     color='Region', size='Unit_Price',
                     hover_data=['Salesperson', 'Product', 'Date'],
                     title='Plotly Interactive Scatter: Units Sold vs Revenue',
                     opacity=0.7)
    fig.write_html(f'{OUTPUT_DIR}/plotly_interactive_scatter.html')
    fig.write_image(f'{OUTPUT_DIR}/plotly_interactive_scatter.png', scale=2)
    print("Saved: plotly_interactive_scatter.html & .png")


def plotly_3d_scatter(df):
    """25. 3D scatter plot: Units Sold, Unit Price, Revenue."""
    if not HAS_PLOTLY:
        print("Plotly not installed. Skipping 3D scatter.")
        return
    sample = df.sample(min(500, len(df)))
    fig = px.scatter_3d(sample, x='Units_Sold', y='Unit_Price', z='Total_Revenue',
                        color='Region', size='Total_Revenue',
                        hover_data=['Salesperson', 'Product'],
                        title='Plotly 3D Scatter: Sales Dimensions')
    fig.write_html(f'{OUTPUT_DIR}/plotly_3d_scatter.html')
    fig.write_image(f'{OUTPUT_DIR}/plotly_3d_scatter.png', scale=2)
    print("Saved: plotly_3d_scatter.html & .png")


def plotly_sunburst(df):
    """26. Sunburst chart: Hierarchical view of Region -> Product revenue."""
    if not HAS_PLOTLY:
        print("Plotly not installed. Skipping sunburst.")
        return
    sunburst_data = df.groupby(['Region', 'Product'], as_index=False)['Total_Revenue'].sum()
    fig = px.sunburst(sunburst_data, path=['Region', 'Product'], values='Total_Revenue',
                      title='Plotly Sunburst: Revenue Hierarchy',
                      color='Total_Revenue', color_continuous_scale='RdBu')
    fig.write_html(f'{OUTPUT_DIR}/plotly_sunburst.html')
    fig.write_image(f'{OUTPUT_DIR}/plotly_sunburst.png', scale=2)
    print("Saved: plotly_sunburst.html & .png")


def plotly_treemap(df):
    """27. Treemap: Hierarchical revenue breakdown."""
    if not HAS_PLOTLY:
        print("Plotly not installed. Skipping treemap.")
        return
    treemap_data = df.groupby(['Region', 'Salesperson'], as_index=False)['Total_Revenue'].sum()
    fig = px.treemap(treemap_data, path=[px.Constant('Total'), 'Region', 'Salesperson'],
                     values='Total_Revenue', color='Total_Revenue',
                     color_continuous_scale='Viridis',
                     title='Plotly Treemap: Revenue Breakdown')
    fig.data[0].textinfo = 'label+value+percent parent'
    fig.write_html(f'{OUTPUT_DIR}/plotly_treemap.html')
    fig.write_image(f'{OUTPUT_DIR}/plotly_treemap.png', scale=2)
    print("Saved: plotly_treemap.html & .png")


# ============================================================
# D. PANDAS NATIVE CHARTS
# ============================================================

def pandas_parallel_coordinates(df):
    """28. Parallel coordinates: Multivariate comparison of salespeople."""
    person_stats = df.groupby('Salesperson').agg(
        Total_Revenue=('Total_Revenue', 'sum'),
        Units_Sold=('Units_Sold', 'sum'),
        Avg_Price=('Unit_Price', 'mean'),
        Transactions=('Total_Revenue', 'count')
    ).reset_index()
    for col in person_stats.columns[1:]:
        person_stats[col] = (person_stats[col] - person_stats[col].min()) / (person_stats[col].max() - person_stats[col].min())
    
    fig, ax = plt.subplots(figsize=(10, 6))
    pd.plotting.parallel_coordinates(person_stats, 'Salesperson', colormap='tab10', ax=ax)
    ax.set_title('Pandas Parallel Coordinates: Salesperson Comparison', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/pandas_parallel_coordinates.png', dpi=300)
    plt.close(fig)
    print("Saved: pandas_parallel_coordinates.png")


def pandas_andrews_curves(df):
    """29. Andrews curves: Multivariate patterns in salesperson data."""
    person_stats = df.groupby('Salesperson').agg(
        Total_Revenue=('Total_Revenue', 'sum'),
        Units_Sold=('Units_Sold', 'sum'),
        Avg_Price=('Unit_Price', 'mean'),
        Transactions=('Total_Revenue', 'count')
    ).reset_index()
    for col in person_stats.columns[1:]:
        person_stats[col] = (person_stats[col] - person_stats[col].min()) / (person_stats[col].max() - person_stats[col].min())
    
    fig, ax = plt.subplots(figsize=(10, 6))
    pd.plotting.andrews_curves(person_stats, 'Salesperson', colormap='tab10', ax=ax)
    ax.set_title('Pandas Andrews Curves: Salesperson Patterns', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/pandas_andrews_curves.png', dpi=300)
    plt.close(fig)
    print("Saved: pandas_andrews_curves.png")


def pandas_hexbin_native(df):
    """30. Pandas native hexbin plot."""
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot.hexbin(x='Units_Sold', y='Total_Revenue', gridsize=20, cmap='plasma', ax=ax)
    ax.set_title('Pandas Hexbin: Units Sold vs Revenue', fontsize=14, fontweight='bold')
    plt.tight_layout()
    fig.savefig(f'{OUTPUT_DIR}/pandas_hexbin.png', dpi=300)
    plt.close(fig)
    print("Saved: pandas_hexbin.png")


def pandas_scatter_matrix(df):
    """31. Scatter matrix: Pairwise relationships via Pandas."""
    numeric_df = df[['Units_Sold', 'Unit_Price', 'Total_Revenue']].sample(min(500, len(df)))
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))
    pd.plotting.scatter_matrix(numeric_df, alpha=0.5, diagonal='kde', ax=axes)
    fig.suptitle('Pandas Scatter Matrix: Numeric Relationships', fontsize=14, fontweight='bold', y=1.02)
    fig.savefig(f'{OUTPUT_DIR}/pandas_scatter_matrix.png', dpi=300)
    plt.close(fig)
    print("Saved: pandas_scatter_matrix.png")


# ============================================================
# MAIN RUNNER
# ============================================================

ALL_CHARTS = [
    # Matplotlib (13 charts)
    matplotlib_scatter,
    matplotlib_bubble,
    matplotlib_stacked_bar,
    matplotlib_grouped_bar,
    matplotlib_area,
    matplotlib_boxplot,
    matplotlib_violin,
    matplotlib_heatmap,
    matplotlib_donut,
    matplotlib_radar,
    matplotlib_waterfall,
    matplotlib_lollipop,
    matplotlib_hexbin,
    # Seaborn (7 charts)
    seaborn_pairplot,
    seaborn_jointplot,
    seaborn_regression,
    seaborn_countplot,
    seaborn_swarmplot,
    seaborn_kde,
    seaborn_clustermap,
    # Plotly (7 charts)
    plotly_interactive_line,
    plotly_interactive_bar,
    plotly_interactive_pie,
    plotly_interactive_scatter,
    plotly_3d_scatter,
    plotly_sunburst,
    plotly_treemap,
    # Pandas (4 charts)
    pandas_parallel_coordinates,
    pandas_andrews_curves,
    pandas_hexbin_native,
    pandas_scatter_matrix,
]


def run_gallery(filepath='sales_data.csv', selected=None):
    """
    Generate all charts in the gallery.

    Args:
        filepath: path to sales_data.csv
        selected: optional list of chart function names or indices to run.
                  If None, runs all charts.
    """
    print("=" * 60)
    print("COMPREHENSIVE CHART GALLERY")
    print("=" * 60)
    df = load_sales_data(filepath)
    print(f"Loaded {len(df)} records from {filepath}\n")

    charts_to_run = ALL_CHARTS
    if selected is not None:
        charts_to_run = [c for c in ALL_CHARTS if c.__name__ in selected or ALL_CHARTS.index(c) in selected]

    total = len(charts_to_run)
    for i, chart_func in enumerate(charts_to_run, 1):
        try:
            print(f"\n[{i}/{total}] Running: {chart_func.__name__} ...")
            chart_func(df)
        except Exception as e:
            print(f"  ERROR in {chart_func.__name__}: {e}")

    print("\n" + "=" * 60)
    print("GALLERY COMPLETE!")
    print(f"Total charts generated: {total}")
    print(f"Output directory: {OUTPUT_DIR}/")
    print("=" * 60)


if __name__ == "__main__":
    run_gallery()
