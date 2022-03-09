import sys

current_word = None
current_count = 0
current_value = 0
word = None
count = 0
value = 0

for line in sys.stdin:
    word, count, value = line.split(",")
    if(word != "Town/City "):
        count = int(count[1])
        value = int(value)

        if current_word == word:
            current_count += count
            current_value += value
        else:
            if current_word:
                print('%s,%s' %
                      (current_word, current_value/current_count))
            current_count = count
            current_word = word
            current_value = value

if current_word == word:
    print('%s,%s' %
          (current_word, current_value/current_count))

