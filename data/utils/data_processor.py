def clean_sales_data(raw_lines):
    total_records = 0
    invalid_records = 0
    valid_records = []

    for line in raw_lines:
        total_records += 1
        fields = line.split("|")

        if len(fields) != 8:
            invalid_records += 1
            continue

        transaction_id = fields[0].strip()
        customer_id = fields[1].strip()
        product_name = fields[2].strip().replace(",", " ")
        category = fields[3].strip()
        quantity = fields[4].strip().replace(",", "")
        unit_price = fields[5].strip().replace(",", "")
        region = fields[6].strip()
        date = fields[7].strip()

        # Validation rules
        if not transaction_id.startswith("T"):
            invalid_records += 1
            continue

        if not customer_id or not region:
            invalid_records += 1
            continue

        try:
            quantity = int(quantity)
            unit_price = float(unit_price)
        except:
            invalid_records += 1
            continue

        if quantity <= 0 or unit_price <= 0:
            invalid_records += 1
            continue

        valid_records.append([
            transaction_id,
            customer_id,
            product_name,
            category,
            quantity,
            unit_price,
            region,
            date
        ])

    print(f"Total records parsed: {total_records}")
    print(f"Invalid records removed: {invalid_records}")
    print(f"Valid records after cleaning: {len(valid_records)}")

    return valid_records
