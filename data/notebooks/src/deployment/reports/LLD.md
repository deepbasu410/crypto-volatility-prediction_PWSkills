# Low Level Design (LLD)

## 1. Data Preprocessing Module (`preprocess.py`)
### Responsibilities
- Load the dataset from CSV format
- Handle missing values using forward fill
- Generate derived features related to volatility

### Key Function
- `preprocess_data(path)`
  - Reads dataset
  - Calculates log returns
  - Computes 7-day rolling volatility
  - Calculates liquidity ratio
  - Returns cleaned dataset

---

## 2. Feature Engineering
The following features are engineered:
- **Log Returns**: Measures daily price movement
- **Rolling Volatility (7-day)**: Captures short-term risk
- **Liquidity Ratio**: Volume divided by Market Capitalization

---

## 3. Model Training Module (`train.py`)
### Responsibilities
- Split dataset into training and testing sets
- Scale numerical features
- Train machine learning model

### Implementation Details
- Feature scaling using StandardScaler
- 80:20 train-test split
- Random Forest Regressor for training

---

## 4. Model Evaluation Module (`evaluate.py`)
### Responsibilities
- Evaluate trained model performance

### Metrics Used
- Root Mean Squared Error (RMSE)
- R² Score

---

## 5. Deployment Module (`app.py`)
### Responsibilities
- Provide a simple user interface
- Allow dataset upload
- Train model dynamically

### Framework Used
- Streamlit

---

## 6. Notebook (`Crypto_Volatility_Prediction.ipynb`)
### Purpose
- Perform Exploratory Data Analysis (EDA)
- Visualize data trends
- Experiment with features and models
- Display evaluation results

