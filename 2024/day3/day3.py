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

def getValidMultiplication(index, line):
  if len(line) < index+8:
      print("Aborted last 'mul'!")
      return -1
  if line[index+3] != "(":
      print("Aborted 'mul' at ", index)
      return -1
  if len(line[index:]) <= 4:
      return -1
  firstNumberSnippet = line[index+4:index+8]
  firstNumberSnippetCommaIndex = firstNumberSnippet.find(",")
  if firstNumberSnippetCommaIndex == -1:
      return -1
  else:
      firstNumberSnippet = firstNumberSnippet[:firstNumberSnippetCommaIndex]
      if not firstNumberSnippet.isdigit():
          return -1

  commaIndex = index+4+firstNumberSnippetCommaIndex
  secondNumberEndIndex = commaIndex+5
  remainingLineLength = len(line[commaIndex:])
  if remainingLineLength < 2:
    return -1
  else:
    if remainingLineLength < 5:
      secondNumberEndIndex = commaIndex+remainingLineLength
        
  secondNumberSnippet = line[commaIndex+1:secondNumberEndIndex]
  secondNumberSnippetParenthesisIndex = secondNumberSnippet.find(")")
  print("firstNumberSnippet: ", firstNumberSnippet, " — secondNumberSnippet: ", secondNumberSnippet)
  if secondNumberSnippetParenthesisIndex == -1:
      return -1
  else:
      secondNumberSnippet = secondNumberSnippet[:secondNumberSnippetParenthesisIndex]
      if not secondNumberSnippet.isdigit():
          return -1
      return int(firstNumberSnippet) * int(secondNumberSnippet)
  
def highestSmallerValue(value, list):
  values = []
  for e in list:
    if e < value:
      values.append(e)
  if len(values) == 0:
    return -1
  return max(values)

def isInValidZone(mulIndex, dontIndexes, doIndexes):
    # Check if mulIndex is after a dont and dos between the dont and the mulIndex
    if mulIndex < dontIndexes[0]:
       return True
    allegibleDontIndex = highestSmallerValue(mulIndex, dontIndexes)
    if allegibleDontIndex < mulIndex:
      allegibleDoIndex = highestSmallerValue(mulIndex, doIndexes)
      if allegibleDoIndex > allegibleDontIndex and allegibleDoIndex < mulIndex:
        return True
    return False


lines = getLinesFromFile("day3/input.txt")
firstLine = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
firstLines = [firstLine]

sumOfValidMultiplications = 0
for line in lines:
    occurencesOfMulP = [m.start() for m in re.finditer("mul", line)]
    occurencesOfDont = [m.start() for m in re.finditer("don't", line)]
    occurencesOfDo = [m.start() for m in re.finditer("do", line)]
    for e in occurencesOfDont:
      occurencesOfDo.remove(e)

    usableMulIndexes = []
    for i in range(len(occurencesOfMulP)):
      if isInValidZone(occurencesOfMulP[i], occurencesOfDont, occurencesOfDo):
        usableMulIndexes.append(occurencesOfMulP[i])
  
    print("all muls: ", occurencesOfMulP, " — dos: ", occurencesOfDo, " — donts: ", occurencesOfDont)
    print("usable muls: ", usableMulIndexes)
    for index in usableMulIndexes:
      multipliedNumber = getValidMultiplication(index, line)
      if multipliedNumber > 0:
          sumOfValidMultiplications += multipliedNumber


print("sum of valid multiplications: ", sumOfValidMultiplications)