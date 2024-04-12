import csv
import os 

# creating new csv with new headers 
def create_orders_csv(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            transaction_data = list(reader)

            # Header
            header = ['Location', 'Product Purchased', 'Price', 'Payment Method']

            with open(output_file, 'w', newline='') as new_file:
                csv_writer = csv.writer(new_file)
                csv_writer.writerow(header)

                for row in transaction_data:
                    location = row[1]  # Assuming location is in the second column
                    product_purchased = row[3]
                    price = row[4]
                    payment_method = row[5]

                    csv_writer.writerow([location, product_purchased, price, payment_method])

        print(f"Transformation completed. New file: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
# split products on different rows
def split_products(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            transaction_data = list(reader)

            # Header
            header = ['Location', 'Product Purchased', 'Price', 'Payment Method']

            with open(output_file, 'w', newline='') as new_file:
                csv_writer = csv.writer(new_file)
                csv_writer.writerow(header)

                for i, row in enumerate(transaction_data):
                    if i == 0:
                        continue

                    location = row[0]  # Assuming location is in the first column
                    products = row[1].split(', ')
                    price = row[2]
                    payment_method = row[3]

                    for product in products:
                        csv_writer.writerow([location, product, price, payment_method])

        print(f"Transformation completed. New file: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
# move price 
def move_price_to_column(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            transaction_data = list(reader)

            # Header
            header = ['Location', 'Product Purchased', 'Price', 'Payment Method']

            with open(output_file, 'w', newline='') as new_file:
                csv_writer = csv.writer(new_file)
                csv_writer.writerow(header)

                for i, row in enumerate(transaction_data):
                    if i == 0:
                        continue

                    location = row[0]  # Assuming location is in the first column
                    price_index = row[1].rfind('-') + 1
                    price = row[1][price_index:].strip()
                    product_purchased = row[1][:price_index-1].strip()
                    payment_method = row[3]

                    products = product_purchased.split(', ')
                    for product in products:
                        csv_writer.writerow([location, product.strip(), price, payment_method])

        print(f"Transformation completed. New file: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
# delete unwanted files
def delete_csv_files(*files):
    for file in files:
        try:
            if file not in ['clean_orders.csv', 'transactions.csv']:  # Exclude specific files from deletion
                os.remove(file)
                print(f"Deleted file: {file}")
            else:
                print(f"Skipping deletion of file: {file}")
        except FileNotFoundError:
            print(f"File not found: {file}")
        except Exception as e:
            print(f"An error occurred while deleting file {file}: {e}")