
def getCalibrationValue(line):
    line=line.strip()
    digits=''
    for char in line:
        if char.isdigit():
            digits+=char
            break
    
    for char in reversed(line):
        if char.isdigit():
            digits+=char
            break
    return int(digits)


def getSum():
    sum=0;
    with open('./input.txt') as calibration_file:
        for line in calibration_file:
            sum+=getCalibrationValue(line)
    print(sum)
    return sum
getSum()

