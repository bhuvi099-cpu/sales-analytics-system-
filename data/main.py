from utils.file_handler import read_sales_file, write_clean_data
from utils.data_processor import clean_sales_data
from utils.api_handler import fetch_product_info

DATA_FILE = "data/sales_data.txt"
OUTPUT_FILE = "output/clean_sales_data.csv"

def main():
    raw_data = read_sales_file(DATA_FILE)
    cleaned_data = clean_sales_data(raw_data)

    write_clean_data(OUTPUT_FILE, cleaned_data)

    # Example API call
    product_info = fetch_product_info("Laptop")
    print("Sample API Data:", product_info)

if __name__ == "__main__":
    main()
