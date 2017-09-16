word_list = ['hello','world','my','name','is','Anna']
letters = set('o')
for word in word_list:
    if letters & set(word):
        print word