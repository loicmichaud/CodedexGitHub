import csv

max_sales = 0  # Initialize max sales
best_selling_book = None

with open("Bestseller.csv", 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header

    for row in csv_reader:
        current_sales = float(row[4])  # Assuming 'sales' is in column 4
        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_book = row

# After finding best seller, write it to new CSV
with open("bestseller_info.csv", 'w', newline='', encoding='utf8') as outfile:
    csv_writer = csv.writer(outfile)
    csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
    csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])
