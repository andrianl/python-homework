
def UniqueLetters(string):
    string_copy=string.lower()
    unique_letters = set(string_copy)
    analize={}
    for letter in unique_letters:
        analize[letter]=string_copy.count(letter)
    return analize


text=input('Enter your text:\n')
text.lower()


print(UniqueLetters(text))
