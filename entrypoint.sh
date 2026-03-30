#!/bin/bash

set -e
set -o pipefail

echo "Waiting for selenoid..."

until curl -s http://selenoid:4444/status; do
  echo "Selenoid not ready yet..."
  sleep 2
done

echo "Selenoid is ready"

echo "Running tests..."
pytest tests -v --alluredir=allure-results --junitxml=report.xml -p no:cacheprovider