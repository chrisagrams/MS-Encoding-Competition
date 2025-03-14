# MS Encoding Competition

A competition set out to determine the best encoding/decoding methods for mass spectrometry data.

## Overview
Provided in this repository is a pipeline to easily allow you to test how a given encoding/decoding strategy affects the search results of an mzML file. Your code should only be contained within the `transform` directory under `encode.py` and `decode.py`. Feel free to utilize any Python libraries found on pip, but make sure to update the `requirements.txt` accordingly (if you choose to do so).

Below is a high level overview of the steps found in the pipeline:
- (Step 0): Download test file.
    - A test mzML file is downloaded from a Dropbox directory locally to your machine. This file is only downloaded once, or if the file is not present within the `input` directory. This mzML file, named `test.mzML` is a 64-bit encoded file with no compression applied. 
- Step 1: Deconstruct mzML to XML and binary parts.
    - In this step, we take the mzML and extract the binary out of the XML document tree to a separate `.npy` file. In this pipeline, we do not make any changes to the XML tree of the mzML, only transforming the binary data found within the mzML file. The implementation of this step can be found at https://github.com/chrisagrams/mzML-Construct
- Step 2: Run MSFragger on original mzML file.
    - To establish the baseline, we run a MSFragger search using default parameters on the `test.mzML` file. The result files are compressed and stored within `output/test.zip`. Note, this step will not re-run if `test.zip` is present inside of the output directory (as running the search on the original mzML file for each iteration is redundant).
- Step 3: **Encode the binary**
    - The code inside of `transform` is built into a Docker container and ran utilizing the extracted binary from Step 1. The encoding function you provide inside of `transform/encode.py` is executed, and results are exported to `output/transformed.npy`.
    - The `encoder` function within `encode.py` is provided with a Pandas DataFrame with the following columns: `mz` (m/z), `int` (intensity), `ms_level`, and `retention_time`. Each row represents a mass spectrum with index equaling the index of the original mzML file. The `mz` and `int` columns contain an array representing the full binary of that spectrum. **Only perform transformations on the `mz` and `int` columns.**
    - The `encoder` function returns a Pandas DataFrame that will be exported to file. Any NumPy data type can be stored within the cells for `mz` and `int` columns. **Ensure your transformations are applied to the returned DataFrame.**
    - When you first clone this repository, you'll find an initial encoding implementation in `encode.py` in the `encode_log_transform` function. This function simply performs a $log_2$ transformation on the intensity values.
- Step 4: **Decode the binary**
    - Utilizing the built `transform` container, the encoded binary from Step 3 is decoded and exported to `new.npy` utilizing the decode function you provide in `transform/decode.py`. The decoded binary is written to `output/new.npy`
    - The `decoder` function within `decode.py` is provided with the Pandas DataFrame you returned from `encoder` function in Step 3. Perform transformations on the `mz` and `int` columns and return a DataFrame similarly to Step 3.
    - When you first clone this repository, you'll find an initial decoding implementation in `decode.py` that reverses the $log_2$ transformation performed in `encode.py` by applying $2^x$ inside the `decode_log_transform` function.
- Step 5: Reconstruct the mzML file.
    - Here, we reconstruct the mzML file using the transformed binary (after encoding and decoding) utilizing the same implementation as found in Step 1. The transformed mzML file is located under `output/new.mzML`
- Step 6: Run MSFragger on transformed mzML file.
    - Utilizing the same search parameters as in Step 2, we run the same MSFragger search on the transformed mzML file. The results are written to `output/new.zip`
- Step 7: Compare search results.
    - Once the search results for the original and transformed mzML files are complete, we perform a comparison on the peptides identified between the two search results. We output the following results under the `results` directory:
        - `results.csv`: This file contains: the percent of peptide identifications that were preserved during the transformation, the percent of identifications missed after the transformation, and the percent of new identifications that were introduced after the transformation.
        - `venn_diagram.png`: A Venn Diagram to visualize the overlap in identifications before/after transformation.
        - `missed_identifications.csv`: A CSV containing a list of ScanNr (from original search) for identifications lost after transformation.
        `new_identifications.csv`: A CSV containing a list of ScanNR (from new search) for identifications introduced after transformation.
- Step 8: Compute the deflate ratio.
    - The deflate ratio is computed as:
    $$\frac{\text{original binary size} - \text{transformed binary size}}{\text{original binary size}}$$
    - Where a higher deflate ratio signifies a better binary size reduction.
    - The deflate ratio is exported to a CSV file under `results/deflate_ratio.csv`
- Step 9: Export results.
    - The results for this run, along with the code contained within `transform` directory, is written to a zip file with timestamp under the `results` directory. 

## Important Notes
1. The output dataframe needs to be kept at the same dimension, if you remove rows,  you need to put place holders (like a 0 or empty list).

2. The resulting dataframe's column order matters, as the npy save file does not save column names, so please make sure your decoded dataframe has the same column order.

## Usage
To run the encoding and testing pipeline locally, make sure to have [Docker](https://www.docker.com/products/docker-desktop/) and Git installed on your system.

1. Clone the repository
``` sh
git clone https://github.com/chrisagrams/MS-Encoding-Competition.git
```

2. Run Docker Compose within the directory
```
docker compose up --build
```

> **Note:** The `--build` flag ensures the Docker container inside the `transform` directory is built before running the pipeline. Without this flag, the previous build may be used.

The pipeline will take some time to run on first execution. Result files are located under the `results` directory.

## Submitting Results
> **Note:** Submission and validation is still under development. **Store your result zips for now.**