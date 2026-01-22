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


The project follows a structured machine learning pipeline to ensure reliable
and scalable cryptocurrency volatility prediction.

### Step 1: Data Ingestion
- Historical cryptocurrency market data is loaded from a CSV file.
- Data includes OHLC prices, trading volume, and market capitalization.

### Step 2: Data Preprocessing
- Missing values are handled using forward fill.
- Data consistency is ensured across numerical features.
- Cleaned data is prepared for feature engineering.

### Step 3: Feature Engineering
- Log returns are calculated from closing prices.
- Rolling volatility (7-day) is computed as the target variable.
- Liquidity ratio (Volume / Market Capitalization) is generated.

### Step 4: Exploratory Data Analysis (EDA)
- Volatility trends are visualized over time.
- Feature correlations are analyzed.
- Distribution of returns and volatility is examined.

### Step 5: Model Training
- Dataset is split into training and testing sets.
- Numerical features are scaled using StandardScaler.
- Random Forest Regressor is trained on engineered features.

### Step 6: Model Evaluation
- Model performance is evaluated using:
  - Root Mean Squared Error (RMSE)
  - R² Score

### Step 7: Deployment
- The trained model is deployed locally using Streamlit.
- Users can upload a dataset and train the model interactively.

---
