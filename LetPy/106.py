string = str(input("Введите что-нибудь: "))
sentence = string.split()
longest_word = ''
for word in sentence:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)