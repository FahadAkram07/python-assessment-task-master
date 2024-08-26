# Product Price Analysis

This project involves a Python script that interacts with a product API, processes the data, and performs various analyses such as finding the most expensive product, identifying missing products, and comparing final prices between actual and expected data.

## Project Structure

The project contains the following files:

- `main.py`: The main Python script that contains all the functions and logic to fetch, process, and analyze the product data.
- `data/product_prices_calculated.parquet`: A Parquet file containing the expected data, which includes product IDs and their calculated final prices.

## Dependencies

To run this project, you need to install the following Python libraries:

- `requests`
- `pandas`

You can install these dependencies using pip:

```bash
pip install requests pandas
```

## How to Run the Script

Ensure that all dependencies are installed. Place the expected data file (`product_prices_calculated.parquet`) in the `data` directory. Run the script using the command:

```bash
python main.py
```

## Output

The script will output the following information:

1. **Most Expensive Product:** Displays the details of the most expensive product based on the calculated final price.
2. **Missing Products:** Lists the products that are present in the actual data but missing from the expected data.
3. **Matching Final Prices Count:** Shows the number of products with matching final prices between the actual and expected data.




