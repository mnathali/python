import sys

def text_analizer(s = None):
    '''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text'''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if s == None:
        print('What is the text to analyze?')
        s = input()
        
    assert type(s) == type(''), "argument is not a string"

    d = {"U":0, "L":0, "P":0, "S":0}
    for c in s:
        if c.isupper():
            d["U"] += 1
        elif c.islower():
            d["L"] += 1
        elif c.isspace():
            d["S"] += 1
        elif c in punctuations:
            d["P"] += 1
    print('The text contains', len(s), 'character(s):')
    print('-', d['U'], 'upper letter(s)')
    print('-', d['L'], 'lower letter(s)')
    print('-', d['P'], 'punctuation mark(s)')
    print('-', d['S'], 'space(s)')

def main():
    assert len(sys.argv) == 2, "wrong arguments"
    text_analizer(sys.argv[1])

if __name__ == "__main__":
    main()