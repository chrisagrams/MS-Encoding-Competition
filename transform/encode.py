import pandas as pd
import numpy as np


def encode_log_transform(df):
    # Take the log of the 'int' column, add 1 to avoid log(0), and cast to float16
    df['int'] = df['int'].apply(lambda x: np.log1p(x).astype(np.float16))
    return df


def encoder(df):
    encoded_df = encode_log_transform(df)
    return encoded_df
