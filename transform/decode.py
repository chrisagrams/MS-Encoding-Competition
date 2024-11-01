import pandas as pd
import numpy as np


def decode_log_transform(df):
    # Apply the exponential to reverse the log transform, then subtract 1
    df['int'] = df['int'].apply(lambda x: np.expm1(x).astype(np.float64))
    return df


def decoder(df):
    decoded_df = decode_log_transform(df)
    return decoded_df
