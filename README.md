# 🧾 Sales Validation and Reporting System

This Python program validates sales data and generates a detailed sales report. It is designed to help small businesses or analysts ensure that their sales transactions are accurate and well-documented.

## 🚀 Features

- ✅ **Validation of Sales Records**  
  Checks if each sale:
  - Matches known item types in the price list
  - Has a total within ±0.01 of the expected price × quantity

- 📋 **Error Flagging**  
  Identifies invalid sales caused by:
  - Unlisted item types
  - Incorrect sale totals

- 📊 **Report Generation**  
  For each item type, the program summarizes:
  - Total units sold
  - Total number of sales
  - Average income per valid sale
  - Number of invalid sales

- 🔍 **Handles Unknown Items Gracefully**  
  Items not listed in the price dictionary are still reported with error counts.

## 🧠 How It Works

There are three core functions:

1. **`is_valid_sale(price, item_type, item_quantity, sale_total)`**  
   Validates if the sale matches expected totals and known item types.

2. **`flag_invalid_sales(price, sales)`**  
   Filters and returns a list of invalid sales.

3. **`generate_sales_report(price, sales)`**  
   Generates a dictionary report summarizing valid and invalid sales statistics per item.

## 📦 Example Usage

```python
if __name__ == "__main__":
    price = {"apple": 2.0, "orange": 3.0, "tangerine": 4.0}
    sales = [
        ["apple", 1, 2.0],
        ["apple", 3, 6.0],
        ["orange", 1, 2.0],    # Invalid: wrong total
        ["carrot", 1, 8.0],    # Invalid: unknown item
    ]

    print("SALES REPORT")
    print(generate_sales_report(price, sales))
