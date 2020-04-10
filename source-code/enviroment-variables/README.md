# Environment variables

This directory shows some examples of how to use environment variables in a Python
script.

## What is it?

1. `accumulate_data.py`: script that will read all `.txt` files in a directory defined
  in an environment variable `DATA_DIR`.
1. `data`: directory that contains two text files with data.

## How to use it?

```bash
$ export DATA_DIR="$(pwd)/data"
$ ./accumulate_data.py
```
