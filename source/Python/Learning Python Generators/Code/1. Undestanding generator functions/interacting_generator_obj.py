some_words = ["potatoes", 'shallow', 'voice', 'conversation', 'more', 'myself', 'thirty', 'certainly', 'needle', 'learn']

#generator object
def contains_i(words):
    for word in words:
        if 'i' in word:
            yield word

gen_ob = contains_i(some_words)

# convert type
print(list(gen_ob))
print(set(contains_i(some_words)))
print(tuple(contains_i(some_words)))
print("-------------------------------------------------------\n")

#loop
gen_ob = contains_i(some_words)
for element in gen_ob:
    print(element)
print("-------------------------------------------------------\n")

#next(), be carefull with the number of next. If you exceed it will throw an error
gen_ob = contains_i(some_words)
print(next(gen_ob))
print(next(gen_ob))
print(next(gen_ob))
print(next(gen_ob))
print(next(gen_ob))
print("-------------------------------------------------------\n")