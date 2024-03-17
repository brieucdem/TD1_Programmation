liste=[]
f = open('frenchssaccent.dic','r')
for ligne in f:
    liste.append(ligne[0:len(ligne)-1])
f.close()

def longmot(tirage):
    possible_words = []
    tirage_count = {}  # dictionary to count the number of letters in the print run
    for letter in tirage:
        tirage_count[letter] = tirage_count.get(letter, 0) + 1

    for word in liste:
        this_word_count = {}
        for letter in word:
            this_word_count[letter] = this_word_count.get(letter, 0) + 1
        if all(this_word_count.get(letter, 0) <= tirage_count.get(letter, 0) for letter in this_word_count):
            possible_words.append((word, len(word)))

    if possible_words:
        max_word = max(possible_words, key=lambda x: x[1])
        return max_word
    else:
        return None


tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
print(longmot(tirage))