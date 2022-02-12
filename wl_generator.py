def read(file):

    f = open(file, "r")

    text = f.read()

    f.close()

    return text

def write(file, text):

    f = open(file, "w")

    f.write(text)

    f.close()

def addNumber(file, word, numbers, len_limit):

    for num in numbers:

        if len(word) <= len_limit:

            new_word = word + num

            text = read(file)

            write(file, text + new_word + "\n")

            addNumber(file, new_word, numbers, len_limit)

file = input("File name: ")

write(file, "")

words = input("Enter the words: ")

words = words.split()

for word in words:

    text = read(file)

    write(file, text + word + "\n")

    number_count = input(f"How many numbers for word: {word}\n")

    numbers = ""

    if number_count != 0:

        numbers = input(f"Numbers for word: {word}\n")

        if numbers == "":

            numbers = "1234567890"

    len_limit = len(word) + int(number_count) - 1

    addNumber(file, word, numbers, len_limit)
