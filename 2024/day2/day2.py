matrix = []

with open("day2/input.txt", "r") as file:
    for line in file.readlines():
        # spilt string of space separated numbers into a list of numbers
        list = [int(x) for x in line.split()]
        matrix.append(list)
file.close()

def isInRange(num):
    return num >= 1 and num <= 3

def areReportSafe(list):
  isIncreasing = False
  isDecreasing = False
  for j in range(len(list)-1):
      diff = list[j] - list[j+1]
      if diff < 0:
          isIncreasing = True
      elif diff > 0:
          isDecreasing = True
      if isIncreasing == isDecreasing:
          return "Unsafe"
      if not isInRange(abs(diff)):
          return "Unsafe"
  return "Safe"

reportsSafety = []

for i in range(len(matrix)):
    if areReportSafe(matrix[i]) == "Safe":
        reportsSafety.append("Safe")
        continue
    
    isOkIfOneElementRemoved = False
    for k in range(len(matrix[i])):
        temp = matrix[i][:]
        temp.pop(k)
        if areReportSafe(temp) == "Safe":
            isOkIfOneElementRemoved = True
            break
    if isOkIfOneElementRemoved:
      reportsSafety.append("Safe")
    else:
      reportsSafety.append("Unsafe")

print(reportsSafety.count("Safe"))