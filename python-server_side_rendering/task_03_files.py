#!/usr/bin/python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json(filepath):
    """Read and return data from JSON file"""
    with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
    return data


def read_csv(filepath):
    """Read and return data from CSV file"""
    with open(filepath, mode='r', newline='', encoding='utf-8') as csvfile:
        data = list(csv.DictReader(csvfile))
    return data


@app.route('/products')
def products():
    """Display products from JSON or CSV file based on source parameter"""
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    products_list = []

    if source not in ['json', 'csv']:
        error = "Wrong source"
        return render_template('product_display.html', products=products_list, error=error)
    
    try:
        if source == 'json':
            products_list = read_json('products.json')
        elif source == 'csv':
            products_list = read_csv('products.csv')
    except Exception as e:
        error = str(e)
        return render_template('product_display.html', products=products_list, error=error)
    
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_list if int(p.get('id')) == product_id]
            if not filtered_products:
                error = "Product not found"
            else:
                products_list = filtered_products
        except ValueError:
            error = "Invalid product ID"
    
    return render_template('product_display.html', products=products_list, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
