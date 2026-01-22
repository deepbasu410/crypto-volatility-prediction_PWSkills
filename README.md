# Cryptocurrency Volatility Prediction

This project focuses on predicting cryptocurrency market volatility using
machine learning techniques based on historical OHLC, trading volume,
and market capitalization data.

## Dataset
- Historical daily cryptocurrency data
- Features: Open, High, Low, Close, Volume, Market Cap

## Approach
1. Data preprocessing and missing value handling
2. Feature engineering (returns, rolling volatility, liquidity ratio)
3. Exploratory Data Analysis (EDA)
4. Model training using Random Forest Regressor
5. Model evaluation using RMSE and R² score
6. Local deployment using Streamlit

## Project Structure
- `data/` : Dataset
- `notebooks/` : EDA and experiments
- `src/` : Preprocessing, training, evaluation scripts
- `deployment/` : Streamlit application
- `reports/` : HLD, LLD and Final Report

## Evaluation Metrics
- RMSE
- R² Score

