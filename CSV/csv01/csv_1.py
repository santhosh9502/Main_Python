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
male = 0
female = 0
for i in csv_data:
    if i[4] == 'Male':
        male += 1
    elif i[4] == 'Female':
        female += 1
    else:
        pass
print(f"male count is {male}")
print(f"female count is {female}")
print(f"the Ratio is {male/female}")

# 
# with open('data.csv', newline='\n') as csvfile:
#     reader = csv.DictReader(csvfile)
#     data = []
#     for row in reader:
#         data.append(row)
# print(data)

# 
# f = open('data.csv','r')
# s = f.read()
# f.close()
