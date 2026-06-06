import csv
import json

# Step 1: Read data from a CSV file
def read_csv(file_path):
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

# Step 2: Clean data (remove empty rows)
def clean_data(data):
    return [row for row in data if all(value.strip() != "" for value in row.values())]

# Step 3: Transform data (convert numeric fields)
def transform_data(data):
    for row in data:
        if "amount" in row:
            row["amount"] = float(row["amount"])
    return data

# Step 4: Save processed data to JSON
def save_json(data, file_path):
    with open(file_path, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# Example usage
if __name__ == "__main__":
    raw_data = read_csv("input.csv")
    cleaned = clean_data(raw_data)
    transformed = transform_data(cleaned)
    save_json(transformed, "output.json")
    print("Data processing complete! ✅")
