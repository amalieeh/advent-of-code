import re
def getLinesFromFile(fileName):
  lines = []
  with open(fileName, "r") as file:
      for line in file.readlines():
          lines.append(line)
  file.close()
  return lines


def isValidMulP(string):
  return string == "mul("

def isValidNumber(numberString):
  if 0 < len(numberString) < 4:
    if numberString.isdigit():
        return True
  return False

def getNumberUntil(endingLine, cha, minLength, maxLength): #ending line: "8,5))"
  length = len(endingLine)

  if cha not in endingLine:
    return -1
  if length < minLength:
    return -1
  if maxLength < length:
    length = maxLength

  commaIndex = endingLine[:length].find(cha)
  if commaIndex == -1:
    return -1
  numberString = endingLine[:commaIndex]
  if numberString.isdigit():
    return numberString

  


lines = getLinesFromFile("day3/input.txt")
# lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

isInValidZone = True


sumOfValidMultiplications = 0

for line in lines:
  print("All occurences of 'mul' (without starter parathesis) \n", [m.start() for m in re.finditer("mul", line)])
  for i in range(len(line)-4):
    if len(line[i:]) >= 7:
      if line[i:i+7] == "don't()":
        print("don't() found at ", i)
        isInValidZone = False
    if len(line[i:]) >= 4:
      if line[i:i+4] == "do()":
        print("do() found at ", i)
        isInValidZone = True
    if len(line[i:]) >= 8:
      if line[i:i+4] == "mul(":
        if isInValidZone:
          print("* Valid 'mul(' found at ", i, ) 
          firstNumber = getNumberUntil(line[i+4:], ",", 4, 8)
          if firstNumber == -1:
            print("  First number not found! -> aborting")
            continue
          secondNumberStartIndex = i+4+len(firstNumber)+1
          secondNumber = getNumberUntil(line[secondNumberStartIndex:], ")", 2, 4)
          if secondNumber == -1:
            print("  Second number not found! -> aborting")
            continue
          sumOfValidMultiplications += int(firstNumber) * int(secondNumber)
    else:
      break

print("Sum of valid multiplications: ", sumOfValidMultiplications)