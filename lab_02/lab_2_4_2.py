import os
import random

extensions = [
    "txt", "log", "csv", "bat", "c", "cpp", "h", "hpp", "xml", "json"
]

os.mkdir("example")

for i in range(100):
    fileName = f'./example/{i}File.{extensions[random.randint(0,9)]}'
    with open(fileName, 'w') as newBornFile:
        pass
