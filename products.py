import csv
import pandas as pd
import os 
# create a new products csv
def create_products_csv(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            transaction_data = list(reader)

            header = ['Product', 'Price']

            with open(output_file, 'w', newline='') as new_file:
                csv_writer = csv.writer(new_file)
                csv_writer.writerow(header)
                
                for row in transaction_data[1:]:  # Skip the header row
                    csv_writer.writerow(row[:-1])

        print(f"Transformation completed. New file: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
# remove duplicates
def remove_duplicate_products(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        df.drop_duplicates(subset=['Product'], keep='first', inplace=True)
        df.to_csv(output_file, index=False)
        print(f"Duplicate products removed. New file: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
# delete unwanted files
def delete_csv_files(*files):
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted file: {file}")
        except FileNotFoundError:
            print(f"File not found: {file}")
        except Exception as e:
            print(f"An error occurred while deleting file {file}: {e}")
