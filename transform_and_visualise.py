# cleaning transactions csv 
from transactions import cleaning_csv
cleaning_csv('transactions.csv','new_transactions.csv')
from transactions import removing_individual_prices
removing_individual_prices('new_transactions.csv','clean_transactions.csv')
from transactions import delete_csv_files
delete_csv_files('new_transactions.csv')

# creating and cleaning orders csv
from orders import create_orders_csv
create_orders_csv('transactions.csv', 'orders.csv')
from orders import split_products
split_products('orders.csv', 'new_orders.csv')
from orders import move_price_to_column
move_price_to_column('new_orders.csv', 'clean_orders.csv')
from orders import delete_csv_files
delete_csv_files('orders.csv', 'new_orders.csv')

# create and clean products csv
from products import create_products_csv
create_products_csv('clean_orders.csv', 'products.csv')
from products import remove_duplicate_products
remove_duplicate_products('products.csv', 'clean_products.csv')
from products import delete_csv_files
delete_csv_files('products.csv')

# show best and worst selling drinks
from data_visualisation import best_and_worst_selling
best_and_worst_selling()