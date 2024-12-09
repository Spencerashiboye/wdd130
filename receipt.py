""" Purpose: Receipt running 
Arthur: Ashiboye Spencer
"""
import csv
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {}

    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader) # to skip the header row

            for row in reader:
                key = row[key_column_index]
                compound_dict[key] = row
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        raise
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'")
        raise

    return compound_dict

def main():
    products_dict = read_dictionary("products.csv", 0)
    store_name = "Ashiboye Prices"
    print(f"{store_name}")
    
    #open and process the request.csv file 
    with open ("request.csv", mode='r') as file:
        reader = csv.reader(file)
        next(reader) # to skip the header row

        total_items = 0
        subtotal = 0

        for row in reader:
            product_number = row[0]
            quantity = int(row[1]) 

             # Find the product in the dictionary
            product_info = products_dict.get(product_number)
            if product_info:
                product_name = product_info[1]
                product_price = float(product_info[2])
                total_price = product_price * quantity
                print(f"{product_name}, {quantity}, @ {product_price:.2f}")
                total_items += quantity
                subtotal += total_price
            else:
                print(f"Product number {product_number}: not found in products dictionary.")

        
              # Calculate totals
        sales_tax_rate = 0.06
        sales_tax = round(subtotal * sales_tax_rate, 2)
        total_due = round(subtotal + sales_tax, 2)

                #print summary
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total_due:.2f}")
        print(f"Thank you for shopping at the {store_name}.")

    

                #print current date and time 
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%a %b %d %H:%M:%S %Y")
        print(formatted_datetime)

         # Calculate and print "return by" date
        return_by_date = current_datetime + timedelta(days=30)
        return_by_time = return_by_date.replace(hour=21, minute=0, second=0, microsecond=0)
        print(f"Return by: {return_by_time.strftime('%a %b %d %Y at %I:%M %p')}")
    
   


# Ensure the main function runs only when this file is executed directly
if __name__ == "__main__":
    main()
