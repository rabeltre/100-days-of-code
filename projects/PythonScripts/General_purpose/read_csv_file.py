import csv

csv_data = []
with open('external_data/csv/test_data.csv') as csv_file:
    file_read = csv.reader(csv_file)
    for row in file_read:
        csv_data.append({"time": row[0], "open": row[1],  "high": row[2], "low": row[3], "close": row[4], "volume": row[5] })


for row in csv_data[1:]:
    print(row)