#!/bin/sh

TARGET_FILE="/input/test.mzML"
DOWNLOAD_URL="https://uofi.box.com/shared/static/74pf1i9wug1hz9xmsnjlvrcr3wkx1nn8?dl=1"

# Check if the file already exists
if [ ! -f "$TARGET_FILE" ]; then
  echo "File not found. Downloading test.mzML..."
  curl -L -o "$TARGET_FILE" "$DOWNLOAD_URL"
else
  echo "test.mzML already exists in /input. Skipping download."
fi