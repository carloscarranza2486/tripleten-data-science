import pandas as pd

sales_data = [
    ["Laptop", "North America", 120, 120000],
    ["Smartphone", "Europe", 340, 170000],
    ["Tablet", "Asia", 210, 63000],
    ["Headphones", "South America", 150, 45000],
    ["Smartwatch", "Africa", 95, 28500],
]

columns = ["product_name", "region", "units_sold", "revenue"]

sales_report = pd.DataFrame(data=sales_data, columns=columns)
print(sales_report)
