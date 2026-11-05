sentences = str(input("Enter the words: "))


def word_extractor(sentence):
    lst = []
    count = 0

    word = ""
    for letter in sentence:
        if letter != " ":
            word = word + letter

            if count == len(sentence)-1:
                lst.append(word)

        elif letter == " " and word != "":
            lst.append(word)
            word = ""

        count += 1
    return lst



words = word_extractor(sentences)
word_count = {}


for value in words:
    if value not in word_count:
        word_count[value] = 1
    elif value in word_count:
        word_count[value] += 1

print(word_count)

