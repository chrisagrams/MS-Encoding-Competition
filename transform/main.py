import argparse

import numpy as np
import pandas as pd
from encode import encoder
from decode import decoder


def parse_arguments():
    parser = argparse.ArgumentParser(description="Encode/decode MS binary.")
    parser.add_argument(
        "input_file", help="Path to the input data file (binary or npy)"
    )
    parser.add_argument(
        "output_file", help="Path to the output data file (binary or npy)"
    )
    parser.add_argument(
        "--mode",
        choices=["encode", "decode"],
        required=True,
        help="Specify the mode: 'encode' for encoding, 'decode' for decoding.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    if args.mode == "encode":
        df = pd.DataFrame(
            np.load(args.input_file, allow_pickle=True),
            columns=["mz", "int", "ms_level", "retention_time"],
        )
        encoded_df = encoder(df)
        np.save(args.output_file, encoded_df)
    if args.mode == "decode":
        np_data = np.load(args.input_file, allow_pickle=True)
        df = pd.DataFrame(np_data, columns=["mz", "int", "ms_level", "retention_time"])
        decoded_df = decoder(df)
        np.save(args.output_file, df)
