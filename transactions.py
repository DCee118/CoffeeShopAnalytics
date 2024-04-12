import csv
import os
# splitting date and time column and removing sensitive data
def cleaning_csv(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            transaction_data = list(reader)
            
            # Header
            header = ['Date', 'Time', 'Location', 'Products Purchased', 'Total Price', 'Payment Method']
            
            with open(output_file, 'w', newline='') as new_file:
                csv_writer = csv.writer(new_file)
                csv_writer.writerow(header)  
                
                for row in transaction_data:
                    date_time = row[0]
                    location = row[1]
                    products_and_prices = row[3]
                    total_price = row[4]
                    payment_method = row[5]
                    
                    date, time = date_time.split(' ')
                    csv_writer.writerow([date, time, location, products_and_prices, total_price, payment_method])
                    
        print(f"Transformation completed. New file: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
# removing prices from products purchases
def removing_individual_prices(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            transaction_data = list(reader)
            
            # Header
            header = ['Date', 'Time', 'Location', 'Products Purchased', 'Total Price', 'Payment Method']
            
            with open(output_file, 'w', newline='') as new_file:
                csv_writer = csv.writer(new_file)
                
                for row in transaction_data:
                    date = row[0]
                    time = row[1]
                    location = row[2]
                    products_purchased = row[3]
                    total_price = row[4]
                    payment_method = row[5]
                    
                    products_purchased_cleaned = ', '.join([item.split('-')[0].strip() for item in products_purchased.split(',')])
                
                    csv_writer.writerow([date, time, location, products_purchased_cleaned, total_price, payment_method])
                

        print(f"Transformation completed. New file: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
# Delete unwanted CSV files
def delete_csv_files(*files):
    for file in files:
        try:
            if file not in ['clean_transactions.csv', 'transactions.csv']:  # Exclude specific files from deletion
                os.remove(file)
                print(f"Deleted file: {file}")
            else:
                print(f"Skipping deletion of file: {file}")
        except FileNotFoundError:
            print(f"File not found: {file}")
        except Exception as e:
            print(f"An error occurred while deleting file {file}: {e}")
            

