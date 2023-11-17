import csv

temp_data = []
id_update = '2'
new_age = '26'

with open('example.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp_data.append(row)
print(temp_data)

for row in temp_data:
    if row[0] == id_update:
        row[2] = new_age

with open('example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(temp_data)
