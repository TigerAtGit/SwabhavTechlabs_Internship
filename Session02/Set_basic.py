text = "to be or not to be that is the question"
splitted_string = text.split()
print(splitted_string)
s1 = set()
for word in splitted_string:
    s1.add(word)
list_word = list(s1)
list_word.sort()
print(list_word)