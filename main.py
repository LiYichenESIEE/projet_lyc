# main.py
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import pandas as pd
from src.components.component_geopandas import get_geo_chart
from src.components.chart import get_scatter_plots_chart,get_histograms_chart,get_fig_bar_bubble_chart
from src.myutils.clean_data import *
from src.pages.home import home_layout

income_shapefile = 'data/raw/2022 Block Group ACS Income Data (2018-2022)/ma_inc_2022_bg.shp'
cvap_shapefile = 'data/raw/Massachusetts 116th Congressional District CVAP Data (2020)/ma_cvap_2020_cd.shp'
election_shapefile = 'data/raw/Massachusetts 2020 General Election Results Disaggregated to the 2020 Block/ma_2020_gen_2020_blocks.shp'

merged_gdf = load_and_process_data(income_shapefile, cvap_shapefile, election_shapefile)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = home_layout(merged_gdf)

if __name__ == '__main__':
    app.run_server(debug=True)
