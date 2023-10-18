def string_logical_and(ip, mask):
    result = ""
    for i in range(0, len(mask)):
        result += str(int(ip[i]) and int(mask[i]))
    return result


ipv4 = input("Input ipv4: ").split(".")

with open("ip_solve.log", 'w') as resultFile:
    with open("mask.log", 'r') as maskFile:
        for line in maskFile:
            curMask = line.split(".")
            resultString = ""
            for i in range(len(ipv4)):
                ipBin = format(int(ipv4[i]), '08b')
                maskBin = format(int(curMask[i]), '08b')
                resultString += str(int(string_logical_and(ipBin, maskBin), 2))
                if i != len(ipv4) - 1:
                    resultString += "."
            resultString += "\n"
            resultFile.write(resultString)
