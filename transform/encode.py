import pandas as pd
import numpy as np


def encode_log_transform(df: pd.DataFrame) -> pd.DataFrame:
    # An example encoding function is provided:
    # Take the log of the intensities ('int' column), add 1 to avoid log(0), multiply by a scale factor, floor and store as uint16
    scale_factor = 72.0
    df["int"] = df["int"].apply(
        lambda x: (np.floor(np.log2(x + 1) * scale_factor)).astype(np.uint16)
    )
    return df


def encoder(df: pd.DataFrame) -> pd.DataFrame:
    # Call your encoding function here and return transformed DataFrame
    encoded_df = encode_log_transform(df)
    return encoded_df
