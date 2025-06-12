import argparse
from analyzer.core import parse_log

def main():
    parser = argparse.ArgumentParser(description="Analyze log files for error patterns.")
    parser.add_argument('--file', required=True, help='Path to log file')
    parser.add_argument('--level', default='ERROR', help='Log level to filter (e.g., ERROR, WARNING)')
    args = parser.parse_args()

    parse_log(args.file, args.level)

if __name__ == "__main__":
    main()
