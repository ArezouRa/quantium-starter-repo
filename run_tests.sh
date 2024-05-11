#!/bin/bash

# Activate virtual environment (if using one)
source env/bin/activate

# Run test suite and capture the exit code
python -m pytest test_app.py
pytest_exit_code=$?

# Deactivate virtual environment (if activated)
deactivate

# Check the exit code and return accordingly
if [ $pytest_exit_code -eq 0 ]; then
  exit 0  # All tests passed
else
  exit 1  # Some tests failed or an error occurred
fi
