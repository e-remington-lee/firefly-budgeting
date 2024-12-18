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
    elif 'TRAVEL' in description or 'AIRLINE' in description or 'HOTEL' in description:
        return 'Airlines, travel, hotels'
    else:
        return description

# Read the CSV file and process each line
with open('plat_expenses.csv', mode='r', encoding='ISO-8859-1') as infile, open('plat_expenses_with_category.csv', mode='w', newline='', encoding='ISO-8859-1') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)
    prev_row = []
    try: 
        # Write the header row with the new column
        header = next(csv_reader)
        header.append('Category_cleaned')
        # DATE, DESCRIPTION, AMOUNT, CATEGORY_MAPPED  
        new_csv_headers = [header[0], header[1], header[2], 'category_mapped']
        csv_writer.writerow(new_csv_headers)
        
        # Process each row and write to the new CSV file
        for row in csv_reader:
            prev_row = row
            category = row[10]
            expense_type = map_expense_type(category)
            new_row = [row[0], row[1], row[2], expense_type]
            print(new_row)
            csv_writer.writerow(new_row)
    except Exception as e:
        print('Error processing CSV file' + str(e))
        print(prev_row)
