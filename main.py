# Write your code here
import requests
import pandas as pd

def get_actual_data():
    url = "https://dummyjson.com/products"
    params = {"limit": 150}  # Fetching more than 100 products
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["products"]


def load_expected_data(filepath='./data/product_prices_calculated.parquet'):
    return pd.read_parquet(filepath)


def calculate_final_prices(products):
    for product in products:
        final_price = product['price'] * (1 - product['discountPercentage'] / 100)
        product['final_price'] = round(final_price, 2)
    return products


def find_most_expensive_product(products):
    return max(products, key=lambda x: x['final_price'])

def find_missing_products(actual_data, expected_data):
    actual_ids = {product['id'] for product in actual_data}
    expected_ids = set(expected_data['id'])
    missing_ids = actual_ids - expected_ids
    return [product for product in actual_data if product['id'] in missing_ids]


def compare_final_prices(actual_data, expected_data):
    expected_dict = expected_data.set_index('id')['final_price'].to_dict()
    matching_count = sum(1 for product in actual_data if product['final_price'] == expected_dict.get(product['id']))
    return matching_count


def main():
    actual_data = get_actual_data()
    actual_data = calculate_final_prices(actual_data)
    expected_data = load_expected_data()

    most_expensive_product = find_most_expensive_product(actual_data)
    missing_products = find_missing_products(actual_data, expected_data)
    matching_final_price_count = compare_final_prices(actual_data, expected_data)

    print("-------------------------------------")
    print("Most Expensive Product:")
    print(most_expensive_product)
    print("-------------------------------------")
    
    print("Missing Products:")
    print(missing_products)
    print("-------------------------------------")
    
    print("Matching Final Prices Count:")
    print(matching_final_price_count)
    print("-------------------------------------")


if __name__ == "__main__":
    main()
