import requests

def fetch_product_info(product_name):
    """
    Mock API call (replace with real API if provided)
    """
    try:
        # Example public API (mock usage)
        url = f"https://dummyjson.com/products/search?q={product_name}"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "API request failed"}

    except Exception as e:
        return {"error": str(e)}
