#!/bin/bash

PAYTHONPATH="${PAYTHONPATH};$(pwd)"
export PAYTHONPATH

WORKSPACE="$(pwd)/testdata"
export WORKSPACE

python start.py
