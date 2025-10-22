import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]
try:
    with open('packing_list.csv', 'r', encoding='utf16') as pf :
        csv_reader = csv.reader(pf)
        next(csv_reader)
        for row in csv_reader :
            print(row)

except FileNotFoundError :
    print("Packaging list not found. creating a new one")
    with open('packing_list.csv', 'w', encoding='utf16') as pf :
        csv_writer = csv.writer(pf)
        csv_writer.writerows(data)

