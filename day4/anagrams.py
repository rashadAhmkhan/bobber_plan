word_one = "listen"
word_two = "silent"

def freqCount(w):
    wordFreq = {}

    for char in w:
        if char in wordFreq:
            wordFreq[char] += 1
        else:
            wordFreq[char] = 1

    return wordFreq

def areAnagrams(s1, s2):
    d1 = freqCount(s1)
    d2 = freqCount(s2)

    return d1 == d2

print(areAnagrams(word_one,word_two))