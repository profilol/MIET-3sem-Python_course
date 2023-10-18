str = input("Input base string:")
x = input("Input virus:")
baseStringLength = len(str)
virusLength = len(x)

while str.upper().find(x.upper()) != -1:
    startIndex = str.upper().find(x.upper())
    str = str[0:startIndex] + str[startIndex + virusLength:baseStringLength]

print("Result string:" + str)

# ШИЗОФРЕНИЯ НИЖЕ

# while i <= baseStringLength - virusLength:
#     curSubstringLength = 0
#     for j in range(virusLength):
#         curChar = str[i+j]
#         if curChar != x[j].lower() and curChar != x[j].upper():
#             break
#         curSubstringLength += 1
#     if curSubstringLength == virusLength:
#         i += virusLength
#     else:
#         resultString += str[i]
#         i += 1
#     if i > baseStringLength - virusLength:
#         resultString += str[i:baseStringLength]
#     while resultString.upper().find(x.upper()):
