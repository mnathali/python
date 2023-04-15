
class Recipe:
    def __init__(self, name = '', cooking_lvl = 1, cooking_time = 0,
                 ingredients = [], description  = '', recipe_type = ''):
        self.name = name
        self.cooking_lvl = cooking_lvl if cooking_lvl <= 5 and cooking_lvl > 0 else 1
        self.cooking_time = cooking_time if cooking_time > 0 else 0
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f'This recipe wiil help you to cook "{self.name}".\nUse these ingredients: {self.ingredients}\n\
        Time of cooking: {self.cooking_time} | type of food: {self.recipe_type}\n\
        {self.description}'
        return txt



s = Recipe('Cake', 3, 30, ['water', 'sugar', 'apple'], 'Take this and put there ...', 'dessert')
print(s)