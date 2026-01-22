import pandas as pd
import numpy as np

def preprocess_data(path):
    df = pd.read_csv(path)
    df.fillna(method='ffill', inplace=True)

    df['returns'] = np.log(df['close'] / df['close'].shift(1))
    df['volatility_7d'] = df['returns'].rolling(7).std()
    df['liquidity_ratio'] = df['volume'] / df['market_cap']

    df.dropna(inplace=True)
    return df
