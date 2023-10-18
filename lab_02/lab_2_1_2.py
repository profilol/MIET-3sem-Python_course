maxIp = 255

with open("mask.log", 'w') as fileLog:
    step = 1
    ip1 = maxIp
    ip2 = maxIp
    ip3 = maxIp
    ip4 = maxIp

    while ip4 > 0:
        curStr = f'{ip1:03}.{ip2:03}.{ip3:03}.{ip4:03}\n'
        ip4 -= step
        step *= 2
        fileLog.write(curStr)
    step = 1
    while ip3 > 0:
        curStr = f'{ip1:03}.{ip2:03}.{ip3:03}.{ip4:03}\n'
        ip3 -= step
        step *= 2
        fileLog.write(curStr)
    step = 1
    while ip2 > 0:
        curStr = f'{ip1:03}.{ip2:03}.{ip3:03}.{ip4:03}\n'
        ip2 -= step
        step *= 2
        fileLog.write(curStr)
    step = 1
    while ip1 >= 0:
        curStr = f'{ip1:03}.{ip2:03}.{ip3:03}.{ip4:03}\n'
        ip1 -= step
        step *= 2
        fileLog.write(curStr)
