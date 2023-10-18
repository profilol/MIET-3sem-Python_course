import os.path

inputExtension = input("Input extension without dot!: ")
filedir = "./example/"

cnt = 0

exampleFiles = os.listdir(filedir)
findExtension = "." + inputExtension
for file in exampleFiles:
    if file.find(findExtension) != -1:
        cnt += 1

print(f'Files with {findExtension} extension is {cnt}')
