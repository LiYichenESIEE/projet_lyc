# Massachusetts Election Data Visualization Dashboard
## Project Overview
This project is a Dash-based interactive dashboard that visualizes median income, Citizen Voting Age Population (CVAP), and the 2020 general election results in Massachusetts. Through multiple interactive charts and maps, users can explore the relationship between income levels and election outcomes.

## Features
* Median Income Map: Displays the distribution of median income by congressional district.
* Biden and Trump Vote Share Maps: Visualizes the vote shares of Joe Biden and Donald Trump across congressional districts.
* Vote Share Distribution Histograms: Shows the distribution of vote shares for both candidates.
* Income vs. Vote Share Scatter Plots: Analyzes the relationship between median income and vote shares.
* Total Votes Bar Chart: Compares the total votes received by each candidate.
* Bubble Chart: Illustrates median income versus Biden's vote share with bubble sizes representing total votes.

## Installation Guide
### Prerequisites
Python 3.6 or higher



## Data Preparation
Ensure the following data files are downloaded and placed in the data/raw/ directory:

* Median Income Data: 2022 Block Group ACS Income Data (2018-2022)/ma_inc_2022_bg.shp
* CVAP Data: Massachusetts 116th Congressional District CVAP Data (2020)/ma_cvap_2020_cd.shp
* Election Results Data: Massachusetts 2020 General Election Results Disaggregated to the 2020 Block/ma_2020_gen_2020_blocks.shp
* Tip: These datasets may need to be obtained from official sources. Ensure compliance with data usage policies.

## Running the Application
In the project root directory, execute:
```
python main.py
```

Open your web browser and navigate to http://127.0.0.1:8050/ to view the dashboard.

##  Project Structure
- main.py: The main application script defining the layout and initializing the dashboard.
- src/components/: Contains functions for generating charts.
- chart.py: Functions to create histograms, scatter plots, bar charts, and bubble charts.
- component_geopandas.py: Functions to create interactive maps using GeoPandas.
- src/myutils/clean_data.py: Functions for data loading and preprocessing.

## Dependencies
- Dash: Web application framework for Python.
- Dash Bootstrap Components: Provides Bootstrap-themed components.
- Plotly: Library for creating interactive visualizations.
- Pandas: Data manipulation and analysis.
- GeoPandas: Extends pandas data types to allow spatial operations on geometric types.
Notes

## Analysis Report

This section summarizes the key findings from the data analysis.

### 1. Overall Trends
- The analysis shows significant regional differences in income distribution and voting results across congressional districts. For example, **districts with higher median income tend to support Biden**, whereas districts with lower income levels show higher support for Trump.

### 2. Key Findings
- **Biden Vote Share**: Districts with higher median income exhibit a higher vote share for Biden, indicating that residents in economically developed areas are more inclined to support Biden.
- **Trump Vote Share**: Districts with lower median income exhibit a relatively higher vote share for Trump, possibly reflecting the preferences of residents in these areas for Trump’s policies.

### 3. Data Distribution
- **Distribution of Biden Vote Share**: The histogram shows that Biden's vote share mainly ranges from 0.6 to 0.75, with some districts reaching up to 0.85.
- **Distribution of Trump Vote Share**: Trump’s vote share is more dispersed but is primarily concentrated between 0.15 and 0.4.

### 4. Correlation Analysis
- **Relationship between Income and Biden Vote Share**: The scatter plot and regression line indicate a positive correlation between median income and Biden vote share, suggesting that districts with higher income are more likely to support Biden.
- **Relationship between Income and Trump Vote Share**: In contrast, median income and Trump vote share show a negative correlation, implying that districts with lower income levels are more likely to support Trump.

### 5. Conclusion and Recommendations
- Through data analysis, it has been demonstrated that there is a significant correlation between median income levels and voter support tendencies. Voters in high-income areas are more inclined to support Biden, while those in low-income areas tend to favor Trump.
- It is recommended that future campaigns consider the economic profile of each district to tailor outreach strategies and potentially increase support.

## Copyright

I hereby declare that the code provided in this project is authored by me(YICHEN_LI), with the following exceptions:

- For any borrowed lines of code (or code segments), references to the sources and explanations of the usage have been provided.
- Any lines or segments of code without a declaration of external sources are assumed to be created by the author(s) of this project. Omission or misrepresentation of these declarations will be considered plagiarism.
