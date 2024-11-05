#!/bin/sh
# Do not remove this file!
# Checks to see if original search results exists, no need to run first search again every run.

if [ -f /output/test.zip ]; then
  echo "Search results already exist. Skipping first search."
  exit 0
else
  echo "Search results not found. Proceeding with search."
  exec /app/entrypoint.sh "$@"
fi

