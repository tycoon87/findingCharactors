
def find_char(a,b):
    for word in word_list:
        if letters & set(word):
            print word

word_list = ['hello','world','my','name','is','Anna']
letters = set('o')

find_char(word_list , letters)