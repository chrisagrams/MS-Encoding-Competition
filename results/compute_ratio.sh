#!/bin/bash
# Do not remove this file!

original_file="/output/test.npy"
compressed_file="/output/transformed.npy"
output_csv="/results/deflate_ratio.csv"


# Check if both files exist
if [[ ! -f "$original_file" || ! -f "$compressed_file" ]]; then
    echo "Error: One or both of the files ($original_file, $compressed_file) do not exist."
    exit 1
fi

# Get the file sizes in bytes
original_size=$(stat -c%s "$original_file")
compressed_size=$(stat -c%s "$compressed_file")

# Calculate the deflate ratio
deflate_ratio=$(echo "scale=4; ($original_size - $compressed_size) / $original_size" | bc)

echo "original_size,compressed_size,deflate_ratio" > "$output_csv"
echo "$original_size,$compressed_size,$deflate_ratio" >> "$output_csv"

echo "Deflate Ratio: $deflate_ratio (written to $output_csv)"
