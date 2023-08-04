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

country_count = {}
for i in csv_data:
    if i[5] not in country_count:
        country_count[i[5]] = 1
    else:
        country_count[i[5]] += 1
country = max(country_count,key=lambda x: country_count[x])
print(country,country_count[country])
