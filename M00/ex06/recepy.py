

def print_names(book):
    print(*book.keys(), sep='\n')

def recipe_details(name):
    if name not in cookbook:
        print('There is no such reciope')
        return None
    for key, value in cookbook[name].items():
        print(key, '-',  value)

def delete_recipe(name):
    cookbook.pop(name)

def add_recipe():
    print('Enter a name:')
    s = input()
    if s == '':
        print('There is no name')
        return None
    print('Enter ingredients:')
    ingr = []
    tmp = ' '
    while tmp != '':
        tmp = input()
        if tmp != '':
            ingr.append(tmp)
    cookbook[s] = {'ingredients':ingr}
    print('Enter a meal type:')
    cookbook[s]['meal'] = input()
    print('Enter a preparation time:')
    cookbook[s]['prep_time'] = int(input())


cookbook = {'Sandwich':{'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal':'lunch', 'prep_time':10},
            'Cake':{'ingredients': ['flour', 'sugar', 'eggs'], 'meal':'dessert', 'prep_time':60} ,
             'Salad':{'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal':'lunch', 'prep_time':15}}

print('Welcome to the Python Cookbook !')
print('List of available option:')
print('1: Add a recipe')
print('2: Delete a recipe')
print('3: Print a recipe')
print('4: Print the cookbook')
print('5: Quit')

while True:
    i = int(input())
    if i == 5:
        print('Bye')
        break
    elif i == 1:
        add_recipe()
    elif i == 2:
        delete_recipe(input())
    elif i == 3:
        recipe_details(input())
    elif i == 4:
        print_names(cookbook)




