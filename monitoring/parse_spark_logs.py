def extract_errors(log_file):
    with open(log_file, 'r') as f:
        for line in f:
            if "ERROR" in line:
                print(line.strip())

if __name__ == "__main__":
    extract_errors("/var/log/spark/spark-driver.log")
