# High Level Design (HLD)

## 1. Project Overview
The objective of this project is to predict cryptocurrency market volatility using machine learning techniques.
Volatility indicates the degree of price fluctuation over time and plays a crucial role in risk management
and trading strategies.

---

## 2. System Architecture
The system follows a modular machine learning pipeline that processes historical cryptocurrency market data
to predict future volatility levels.

---

## 3. High-Level Components

### a. Data Source
- Historical cryptocurrency market data
- Features include Open, High, Low, Close prices, Volume, and Market Capitalization

### b. Data Preprocessing Layer
- Handles missing values
- Cleans and standardizes numerical features

### c. Feature Engineering Layer
- Generates volatility and liquidity related features
- Converts raw prices into meaningful indicators

### d. Model Layer
- Uses Random Forest Regressor for volatility prediction

### e. Evaluation Layer
- Evaluates model performance using RMSE and R² score

### f. Deployment Layer
- Local deployment using Streamlit for interactive testing

---

## 4. Pipeline Architecture

