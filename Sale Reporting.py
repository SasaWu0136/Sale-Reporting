'''
    Validates a single sale by checking if the item type exists in the price dictionary and if
    the sale total matches the expected total based on item price and quantity.

    Arguments:
        price (dict): Dictionary mapping item_type(str) to respective unit prices (float).
        item_type(str): Type of item being sold.
        item_quantity(int): Number of units sold.
        sale_total (float): Recorded total amount for sale.

    Returns:
        bool(True): if the sale is valid (item exists and total is within 0.01 of expected), False otherwise.
'''
def is_valid_sale(price, item_type, item_quantity, sale_total):
    if item_type not in price: # if item is not in the price table , it is not valid
        return False
    
    future_sale_total = price[item_type] * item_quantity # caculator the future sale total we expect

    return future_sale_total == sale_total # return to check is it same as the real sale total

    '''
    Identifies invalid sales from a list of sales by using `is_valid_sale()` function to verify each sale.

    Arguments:
        price(dict): Dictionary containing the mapping of item types(str) to their unit prices(float).
        sales(list): List of sales, where each sale is a list containing `item_type`(str), `item_quantity`(int), `sale_total`(float).

    Returns: 
        list : List of invalid sales, where each sale is a list containing `item_type`(str), `item_quantity`(int), `sale_total`(float).
    '''
def flag_invalid_sales(price, sales): # use for find some invalid sales
    invalid_sales = []

    for sale in sales:
        item_type, item_quantity, sale_total = sale

        if not is_valid_sale(price, item_type, item_quantity, sale_total):
            invalid_sales.append(sale) # if it is invalid , put it into the wrong list

    return invalid_sales 
    '''
    Generates a comprehensive sales report summarising units sold, sales made, average income per valid sale and errors for each item type.
    Verify whether sale is valid using `is_valid_sale()` function.

    Arguments:
        price(dict): Dictionary mapping `item_type`(str) to it's respective `unit_price`(float).
        sales(dict): List of sales where each sale is a list containing `item_type`(str), `item_quantity`(int), `sale_total`(float).

    Returns:
        dict : Dictionary mapping `item_type`(str) to tuples containing `units_sold`(int), `sales_made`(int), `average_income`(float) and `errors`(int). 
        units_sold(int): Total units sold in valid sales.
        sales_made(int): Total number of sales attempted.
        average_income(float): Average income per valid sale.
        errors(int): Number of invalid sales.
    
    1. Average income is only calculated on valid sales. If no valid sales exist, then it is 0.0.
    2. Sales are considered invalid if the item is not in `price` OR if the sale total deviates from the expected total by more than the permissible range of 0.01.
    3. The reports include all items from `price` dictionary , even if they have no sales.
    4. Items not in `price` but present in `sales` are included in the report with the appropriate error counts.
    '''

def generate_sales_report(price, sales):
    # find out all the invalid_sales report
    invalid_sales = flag_invalid_sales(price, sales)

    # initialization the report,every items point to a dictionary
    report = {}

    for item in price:
        report[item] = {
            "units_sold": 0,        # total units sold
            "sale_total": 0.0,      # total price sale
            "errors": 0,            # errors roll
            "valid_sales": 0,       # every sale roll
            "invalid_sales": 0,     # wrong roll
        }
    #according to the sale report and accumulation
    for sale in sales:
        item_type, item_quantity, sale_total = sale

        # if there is some products not in the price table ,and then initialization the report fields 
        if item_type not in report:
            report[item_type] = {"units_sold":0 , "sale_total":0.0 ,"errors":0 ,"valid_sales":0 ,"invalid_sales":0}

        # if it is valid sale
        if item_type in price and sale not in invalid_sales:
            report[item_type]["units_sold"] += item_quantity
            report[item_type]["sale_total"] += sale_total

        # no matter correct or not, all of them can have add one valid record
        report[item_type]["valid_sales"] += 1

        # if it is wrong record
        if sale in invalid_sales:
            report[item_type]["errors"] +=1
            report[item_type]["invalid_sales"] += 1

    # arrange the final output
    sales_reports = {}

    for item, data in report.items():
        if data["valid_sales"] - data["errors"] > 0 :
            average_income = data["sale_total"] / (data["valid_sales"] - data["errors"])
        else :
            average_income = 0.0 

        sales_reports[item] =(
            data["units_sold"],
            data["valid_sales"],
            round(average_income, 1),
            data["errors"]
        )
    return sales_reports


# WARNING!!! *DO NOT* REMOVE THIS LINE
# THIS ENSURES THAT THE CODE BELLOW ONLY RUNS WHEN YOU HIT THE GREEN `Run` BUTTON, AND NOT THE BLUE `Test` BUTTON
if __name__ == "__main__":
    price = {"apple": 2.0, "orange": 3.0, "tangerine": 4.0}
    sales = [
            ["apple", 1, 2.0],
            ["apple", 3, 6.0],
            ["orange", 1, 2.0],
            ["carrot", 1, 8.0],
        ]

    print("SALES REPORT")
    print(generate_sales_report(price,sales))
