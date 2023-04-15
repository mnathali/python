

def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings before it is yielded.
    '''
    lst = text.split(sep)
    if option == None:
        for s in lst:
            yield s
    elif option == 'shuffle':
        st = set(lst)
        for s in st:
            yield s
    elif option == 'ordered':
        st = text.split(sep)
        st.sort()
        for s in st:
            yield s
    elif option == 'unique':
        st = list(dict.fromkeys(text.split(sep)))
        for s in st:
            yield s
    else:
        print('ERROR')
        return None


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option='ordd'):
    print(word)

