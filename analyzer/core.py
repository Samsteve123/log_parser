def parse_log(file_path, level):
    try:
        with open(file_path, 'r') as file:
            print(f"\n")
            print(f"Filtering log entries for level: {level}\n")
            count = 0
            for line in file:
                if level.upper() in line:
                    print(line.strip())
                    count += 1
            if count == 0:
                print("No matching log entries found.")
            else:
                print(f"Total entries found:", count)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
