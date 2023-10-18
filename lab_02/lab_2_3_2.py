import csv

storeFileName = "store.csv"
categoriesFileName = "categories.csv"

categories = dict()

with open(storeFileName, 'r') as storeFile:
    reader = csv.DictReader(storeFile, delimiter=';')
    for line in reader:
        curCategory = line["Категория"]
        curPrice = float(line["Стоимость"])

        if categories.get(curCategory) is None:
            categories[curCategory] = curPrice
        else:
            categories[curCategory] += curPrice


with open(categoriesFileName, 'w', newline='') as categoriesFile:
    fieldNames = ["Категория", "Стоимость"]
    writer = csv.DictWriter(categoriesFile, fieldNames, delimiter=";")
    writer.writeheader()

    for i in categories:
        writer.writerow({'Категория': i, 'Стоимость': format(float(categories[i]), '.2f')})
