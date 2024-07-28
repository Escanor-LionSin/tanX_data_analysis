import csv
from collections import defaultdict
from datetime import datetime
import sys
import os

def read_csv(file_path):
    # Error Handling
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{file_path}'.")
        sys.exit(1)
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

def compute_monthly_revenue(orders):
    monthly_revenue = defaultdict(float)
    for order in orders:
        try:
            date = datetime.strptime(order['order_date'], '%Y-%m-%d')
            month_key = f"{date.year}-{date.month:02d}"
            revenue = float(order['product_price']) * int(order['quantity'])
            monthly_revenue[month_key] += revenue
        except ValueError as e:
            print(f"Error processing order: {e}")
            continue
    return dict(monthly_revenue)

def compute_product_revenue(orders):
    product_revenue = defaultdict(float)
    for order in orders:
        try:
            product_id = order['product_id']
            revenue = float(order['product_price']) * int(order['quantity'])
            product_revenue[product_id] += revenue
        except ValueError as e:
            print(f"Error processing order: {e}")
            continue
    return dict(product_revenue)

def compute_customer_revenue(orders):
    customer_revenue = defaultdict(float)
    for order in orders:
        try:
            customer_id = order['customer_id']
            revenue = float(order['product_price']) * int(order['quantity'])
            customer_revenue[customer_id] += revenue
        except ValueError as e:
            print(f"Error processing order: {e}")
            continue
    return dict(customer_revenue)

def get_top_customers(customer_revenue, n=10):
    return sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True)[:n]

def main(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)

    orders = read_csv(file_path)
    
    if not orders:
        print("Error: No orders found in the CSV file.")
        sys.exit(1)

    try:
        monthly_revenue = compute_monthly_revenue(orders)
        print("Monthly Revenue:")
        for month, revenue in monthly_revenue.items():
            print(f"{month}: ${revenue:.2f}")
    
        product_revenue = compute_product_revenue(orders)
        print("\nProduct Revenue:")
        for product, revenue in product_revenue.items():
            print(f"{product}: ${revenue:.2f}")
    
        customer_revenue = compute_customer_revenue(orders)
        print("\nCustomer Revenue:")
        for customer, revenue in customer_revenue.items():
            print(f"{customer}: ${revenue:.2f}")
    
        top_customers = get_top_customers(customer_revenue)
        print("\nTop 10 Customers:")
        for customer, revenue in top_customers:
            print(f"{customer}: ${revenue:.2f}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    file_path = "data/orders.csv"
    main(file_path)