import pandas as pd
import numpy as np


def decode_log_transform(df: pd.DataFrame) -> pd.DataFrame:
    # An example encoding function is provided:
    # Apply the exponential to reverse the log transform, divide by scale factor to reverse scaling, then subtract 1
    scale_factor = 72.0
    df['int'] = df['int'].apply(lambda x: (np.exp2(x / scale_factor) - 1).astype(np.float64))
    return df


def decoder(df: pd.DataFrame) -> pd.DataFrame:
    # Call your decoding function here and return transformed DataFrame
    decoded_df = decode_log_transform(df)
    return decoded_df
