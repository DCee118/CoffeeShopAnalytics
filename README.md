# CoffeeShopAnalytics
This repository contains a Python application for analyzing coffee transaction data, performing data cleaning operations, and generating insightful visualizations to understand sales trends and patterns in a coffee shop or similar business setting.

## Purpose
Managing and analyzing transaction data in the coffee industry is crucial for understanding customer preferences, optimizing inventory management, and maximizing revenue. However, raw transaction data often contains inconsistencies, errors, and sensitive information that need to be cleaned and organized before meaningful analysis can be performed. Additionally, visualizing the cleaned data can provide valuable insights into sales performance, popular products, and customer behavior.

## Description
 - **Data Cleaning**: The application provides functions to clean raw transaction data, removing duplicates, inconsistencies, and unnecessary information. It standardizes the format of transaction records and prepares the data for further analysis.

 - **Order Processing**: It processes transaction data to generate organized order records, separating individual products and associating them with specific orders. This step facilitates a granular analysis of product sales and customer purchase behavior.

 - **Product Management**: The application creates and manages a product database, ensuring that product information is accurate, up-to-date, and free from duplicates. It streamlines product inventory management and supports data-driven decisions regarding product offerings.

 - **Data Visualization**: Using the cleaned and organized data, the application generates interactive visualizations to explore sales trends, identify top-selling products, compare sales performance over time, and analyze customer preferences. These visualizations aid stakeholders in making informed business decisions and developing targeted marketing strategies.

## Setup 
1. Clone the repository: <br />
``git clone https://github.com/DCee118/CoffeeShopAnalytics.git``
2. Install the required dependencies: <br />
``pip install -r requirements.txt``
3. Run the Application: <br />
Windows: ``python transform_and_visualise.py`` <br />
Mac: ``python3 transform_and_visualise.py``
