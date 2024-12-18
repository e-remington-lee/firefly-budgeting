import csv

# Define a function to map descriptions to expense types
def map_expense_type(description):
    description = description.upper()
    if 'UBER' in description or 'SEPTA' in description or 'TAXI' in description or 'TRANSPORTATION' in description:
        return 'Transport'
    elif 'E-Z PASS' in description:
        return 'Toll'
    elif 'GAS' in description:
        return 'Fuel'
    elif 'RESTAURANT' in description or 'RISTORANTE' in description or 'PUB' in description:
        return 'Dining'
    elif ('SHOPRITE' in description or 'WHOLEFDS' in description or 'SPROUTS' in description or 
        'GROCERIES' in description):
        return 'Groceries'
    elif 'DANCE' in description:
        return 'Entertainment'
    else:
        return description

# Read the CSV file and process each line
with open('gold_expenses.csv', mode='r') as infile, open('gold_expenses_with_category.csv', mode='w', newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)
    
    # Write the header row with the new column
    header = next(csv_reader)
    header.append('Category_cleaned')
    new_csv_headers = [header[0], header[2], header[3], 'category_mapped']
    csv_writer.writerow(new_csv_headers)
    
    # Process each row and write to the new CSV file
    for row in csv_reader:
        print(row)
        category = row[10]
        expense_type = map_expense_type(category)
        new_row = [row[0], row[2], row[3], expense_type]
        print(new_row)
        csv_writer.writerow(new_row)
