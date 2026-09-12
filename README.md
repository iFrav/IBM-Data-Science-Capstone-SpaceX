# IBM Data Science Capstone - SpaceX Falcon 9 Landing Prediction

Final project for the IBM Applied Data Science Capstone.

This repository studies whether the Falcon 9 first stage will land successfully using an end-to-end data science workflow: data collection, wrangling, exploratory analysis, SQL, geospatial analytics, an interactive dashboard, and classification.

## Repository contents

- `01_data_collection_api.ipynb` - SpaceX REST API collection
- `01b_data_collection_web_scraping.ipynb` - historical launch data collection with web scraping
- `02_data_wrangling.ipynb` - cleaning, missing values and landing target preparation
- `03_eda_visualization.ipynb` - payload, flight, orbit and launch-site EDA
- `04_eda_sql.ipynb` - SQL exploration and aggregations
- `05_folium_analysis.ipynb` - geospatial launch-site analysis
- `06_machine_learning.ipynb` - Logistic Regression, SVM, Decision Tree and KNN comparison
- `spacex_dash_app.py` - interactive Plotly Dash application

## Project workflow

1. Collect historical launch data using the SpaceX API and web scraping.
2. Clean and transform the data and create the binary landing target.
3. Explore launch outcomes using visualization and SQL.
4. Analyze launch-site geography with Folium.
5. Explore site and payload effects interactively with Plotly Dash.
6. Standardize engineered features, tune classifiers with cross-validation, and evaluate on held-out test data.

## Main results

In the course dataset used for the final report:

- Logistic Regression: 84.6% cross-validation accuracy, 83.3% test accuracy
- SVM: 84.8% cross-validation accuracy, 83.3% test accuracy
- Decision Tree: 87.3% cross-validation accuracy, 83.3% test accuracy
- KNN: 84.8% cross-validation accuracy, 83.3% test accuracy

Decision Tree achieved the highest cross-validation score, while all four tuned classifiers tied on the held-out test set. The analysis also showed strong relationships between landing success and operational maturity, launch site, orbit, payload, reuse and recovery hardware.

## Selected SQL findings

- NASA (CRS) total payload in the course dataset: 45,596 kg
- Average payload for F9 v1.1: 2,928.4 kg
- First successful ground-pad landing: 2015-12-22

## Author

Ruslan Varfolomeev

GitHub: https://github.com/iFrav
