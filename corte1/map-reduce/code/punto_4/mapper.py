import sys

for line in sys.stdin:
    print(line.split(",")[6].replace(".", ""), ",", line.split(
        ",")[2][0:4],  ",", line.split(",")[1])
