some_words = ["potatoes", 'shallow', 'voice', 'conversation', 'more', 'myself', 'thirty', 'certainly', 'needle', 'learn']

#normal way
def x_contains_i(words):
    i_words = []
    for word in words:
        if 'i' in word:
            i_words.append(word)
    return i_words

#generator object
def contains_i(words):
    for word in words:
        if 'i' in word:
            yield word


print(x_contains_i(some_words))
print(contains_i(some_words))       #it returns a generator object, but you cannot see what is inside at least you convert it to a list
print(list(contains_i(some_words)))       #it returns a generator object, but you cannot see what is inside at least you convert it to a list
