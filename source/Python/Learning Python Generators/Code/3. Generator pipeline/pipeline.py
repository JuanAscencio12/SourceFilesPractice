words = [
"able lost darkness learn",
"road older goes",
"basic",
"must seed laid itself hot must",
"compound decide",
"trap active paragraph hair review stay written",
"facing smile vowel chose other",
"occur shop box metal equal mouse some city"
]

#most = (len(phrase.split(" ")) for phrase in words)
# Remember that generator are lazy, so if you use them in another case
# such as ind_word in word_lenght it will not print because ind_words
# was previously used. 
ind_words = (string.split(" ") for string in words)
word_lenght = (len(lista) for lista in ind_words)
most = max(word_lenght)

print(list(ind_words))
print(list(word_lenght))
print(most)