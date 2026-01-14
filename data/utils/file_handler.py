import csv
import os

def read_sales_file(data/sales_data.csv):
    records = []

    with open(sales_data, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                records.append(line)

    return records


def write_clean_data(data/clean_sales_data.csv, data):
    os.makedirs("output", exist_ok=True)

    with open(clean_sales_data.csv, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "TransactionID", "CustomerID", "ProductName", "Category",
            "Quantity", "UnitPrice", "Region", "Date"
        ])

        for row in data:
            writer.writerow(row)

    print(f"Clean data written to {clean_sales_data.csv}")
