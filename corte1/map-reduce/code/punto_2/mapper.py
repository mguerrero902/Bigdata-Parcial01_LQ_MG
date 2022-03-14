import sys

for line in sys.stdin:
    print(line.split(",")[6].replace(".", ""), ",", 1, ",", line.split(",")[1])
