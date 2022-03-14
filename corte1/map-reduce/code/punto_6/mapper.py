import sys

for line in sys.stdin:
    print(line.split(",")[8], ",", 1, ",", line.split(",")[6], ",", 1)
