#Twitter hashtag
# input: Python is fun
# output: #PythonIsFun

text = "Python is fun"
list_of_words = text.split(" ")
print(list_of_words)
empty_list = []
for word in list_of_words:
    words_capitallized = word.capitalize()
    empty_list.append(words_capitallized)

words_joined = "".join(empty_list)
print(words_joined)
print("#"+words_joined)

