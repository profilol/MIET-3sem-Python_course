arr = [int(x) for x in input("input array:").split()]
n = len(arr)

flag = False
for i in arr:
    if i != 0:
        flag = True
        break
ans = 0
while flag:
    i = 0
    while i < n and arr[i] == 0:
        i += 1
    startPos = i
    if i == n:
        flag = False
    else:
        while i < n and arr[i] != 0:
            i += 1
        for j in range(startPos, i):
            arr[j] -= 1
        print(*arr)
        ans += 1

print("Answer =", ans)



