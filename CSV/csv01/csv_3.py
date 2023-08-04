import csv
with open('E:/Python Web Project/New Trains/CSV/csv01/data.csv', newline='\n') as csvfile:
    # datareader = csv.reader(csvfile, delimiter=';', quotechar='|')
    # data extracted to data reader and retruns a reader object
    
    datareader = csv.reader(csvfile, delimiter=',')
    
    data_iter = iter(datareader)
    col_names = next(data_iter)

    csv_data = []

    for row in data_iter:
        csv_data.append(row)

print(col_names)
print(csv_data)

country = {}
for i in csv_data:
    if country.get(i[5]):
        country[i[5]] += 1
    else:
        country[i[5]] = 1
print()
print(country,"the highest population country is ",max(country,key=lambda x: country[x]))