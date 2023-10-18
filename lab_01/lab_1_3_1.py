n = int(input("Input record's count: "))

records = set()
for i in range(n):
    curRecord = tuple(input("Input {} record: ".format(i)).split())
    records.add(curRecord)

k = dict()
for i in records:
    key = tuple([i[0], i[1]])
    curValue = k.get(key)
    if curValue is None:
        k[key] = 1
    else:
        k[key] = int(curValue) + 1

for i in k:
    print("{} {} - {}".format(i[0], i[1], k.get(i)))
