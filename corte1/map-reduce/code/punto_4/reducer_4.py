import sys

# Se ordenan los datos por consola con la instruccón sort -t "," -k3 -n

word = None
year = 0
value = 0

order = list()

for line in sys.stdin:
    word, year, value = line.split(",")
    if(word != "Town/City "):
        if word == "STAMFORD " and year == " 1995 ":
            print('%s,%s,%s' % (word, year, value), end="")


