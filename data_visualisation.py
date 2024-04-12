import pandas as pd
import matplotlib.pyplot as plt

def best_and_worst_selling():
    df = pd.read_csv('clean_orders.csv')

    # Group by product and calculate total sales
    product_sales = df.groupby('Product Purchased')['Price'].sum().sort_values()

    # Select top 5 best selling products and bottom 5 worst selling products
    top_5 = product_sales.tail(5)
    bottom_5 = product_sales.head(5)

    # Plotting
    plt.figure(figsize=(17, 8))

    # Top 5 best selling products
    plt.subplot(1, 2, 1)
    top_5.plot(kind='bar', color='green')
    plt.title('Top 5 Best Selling Products')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')

    # Bottom 5 worst selling products
    plt.subplot(1, 2, 2)
    bottom_5.plot(kind='bar', color='red')
    plt.title('Bottom 5 Worst Selling Products')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')

    plt.tight_layout()
    plt.show()