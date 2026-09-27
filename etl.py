import csv


def extract_data(file_path):
    with open(file_path, mode="r") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    return data


def transform_data(data):
    cleaned_data = []
    for row in data:
        row["name"] = row["name"].strip().title()
        row["city"] = row["city"].strip().title()
        row["age"] = row["age"] if row["age"] else "0"
        cleaned_data.append(row)
    return cleaned_data


def load_data(data, output_path):
    with open(output_path, mode="w", newline="") as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        print(f"Data loaded successfully to {output_path}")


if __name__ == "__main__":
    row_data = extract_data("Data/input.csv")
    transformed_data = transform_data(row_data)
    load_data(transformed_data, "Data/output.csv")
