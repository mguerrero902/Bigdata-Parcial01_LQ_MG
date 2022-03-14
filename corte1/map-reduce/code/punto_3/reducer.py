import sys

current_word = None
current_value = 0
word = None
value = 0

for line in sys.stdin:
    word, value = line.split(",")
    if(word != "Town/City "):
        value = int(value)

        if current_word == word:
            if value < current_value:
                current_value = value
        else:
            if current_word:
                print('%s,%s' % (current_word, current_value))
            current_word = word
            current_value = value

if current_word == word:
    print('%s,%s' % (current_word, current_value))
