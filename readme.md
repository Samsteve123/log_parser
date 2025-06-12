##Log Analyzer with Command Line Interface

A Python tool to parse and summarize log files for error patterns, timestamps, and message frequency.

## Features
- Parse structured or semi-structured log files
- Extract error/warning lines and timestamps
- CLI options for filtering by date, keyword, or severity
- Optional: Output summary table or basic charts

## Usage
```bash
python log_parse.py --file logs/sample_log.txt --level ERROR
