# Final Report – Cryptocurrency Volatility Prediction

## 1. Introduction
Cryptocurrency markets are highly volatile, making volatility prediction an important task for traders and
investors. This project applies machine learning techniques to predict cryptocurrency volatility using
historical market data.

---

## 2. Dataset Description
The dataset consists of historical daily records of cryptocurrencies with the following attributes:
- Open, High, Low, Close prices
- Trading Volume
- Market Capitalization

---

## 3. Methodology
The project follows a structured machine learning workflow:
1. Data preprocessing and cleaning
2. Feature engineering
3. Exploratory Data Analysis (EDA)
4. Model training
5. Model evaluation
6. Local deployment

---

## 4. Exploratory Data Analysis (EDA)
EDA helped identify:
- Significant variation in volatility over time
- Relationship between trading volume and volatility
- Distribution patterns of returns

Visualizations were used to understand trends and correlations.

---

## 5. Model and Evaluation
- **Model Used**: Random Forest Regressor
- **Evaluation Metrics**:
  - RMSE
  - R² Score

The model demonstrated effective performance in predicting short-term volatility.

---

## 6. Results and Insights
- Engineered features significantly improved prediction accuracy
- Liquidity and price movements are strong indicators of volatility
- The model can identify high-risk market periods

---

## 7. Deployment
The trained model was deployed locally using a Streamlit application, allowing users to upload a dataset and
train the model interactively.

---

## 8. Conclusion
This project successfully demonstrates the use of machine learning for cryptocurrency volatility prediction.
The solution is modular, scalable, and suitable for real-world extensions.

---

## 9. Future Enhancements
- Implement deep learning models such as LSTM
- Use real-time cryptocurrency data
- Extend support for multiple cryptocurrencies

