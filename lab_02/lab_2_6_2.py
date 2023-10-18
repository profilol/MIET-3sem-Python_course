articleFilename = "article.txt"
articleSolveFilename = "article_solve.txt"

letterStat = dict()
lettersCount = 0
with open(articleFilename, encoding='utf-8', mode='r') as articleFile:
    for line in articleFile:
        for char in line:
            lowerChar = char.lower()
            if 'a' <= lowerChar <= 'z' or 'а' <= lowerChar <= 'я' or lowerChar == 'ё':
                lettersCount += 1
                if letterStat.get(lowerChar) is None:
                    letterStat[lowerChar] = 1
                else:
                    letterStat[lowerChar] += 1

resultArr = []
for i in letterStat:
    curStat = tuple([letterStat[i], i])
    if len(resultArr) == 0:
        resultArr.append(curStat)
    else:
        j = 0
        while j < len(resultArr) and curStat[0] < resultArr[j][0]:
            j += 1
        if j == resultArr:
            resultArr.append(curStat)
        else:
            resultArr.insert(j, curStat)

with open(articleSolveFilename, encoding='utf-8', mode='w') as solveFile:
    for i in resultArr:
        curStat = f'{i[1]}:{format(i[0] / lettersCount, ".4f")}\n'
        solveFile.write(curStat)
