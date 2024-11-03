# MS Encoding Competition

A competition set out to determine the best encoding/decoding methods for mass spectrometry data.

## Introduction


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