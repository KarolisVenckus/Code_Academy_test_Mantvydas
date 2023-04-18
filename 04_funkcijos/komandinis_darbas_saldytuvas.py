'''
************************PROGRAMOS APRASYMAS************************
Parašykite programą šaldytuvas, kuri:
- saugo produktus žodyne, kur:
-- produkto pavadinimas yra raktas
-- kiekis yra reikšmė float
Tarkime, kad:
- kieti produktai matuojami kilogramais
- skysti litrais
- paruošti patiekalai matuojami vienetais
tokiu atveju, mums nereikia apibrėžti mato vieneto
Šaldytuvas turi meniu, per kurį galime:
- įdėti produktus
- išimti produktus
-- jeigu produkto kiekis tampa 0, ištriname
- peržiūrėti produktų sąrašą
- suskaičiuoti šaldytuvo turinio svorį
-- skystų tankis = 1
-- paruoštų patiekalų porcija sveria 1kg
BONUS:
Įterpti meniu punktą "ar išeina", kur vartotojo prašo įvesti:
- vienos porcijos receptą
-- įvedimo formatas: "ingredientas: kiekis" vienoje eilutėje.
- porcijų kiekį
Tada programa turėtų:
- išvesti, ar užtenka ingredientų patiekalams paruošti
- jeigu neužtenka, išvardinti ko ir kiek trūksta (shopping list).
- išvesti, kelioms porcijoms užtenka ingredientų, jei yra perteklius
'''

import time
import os

products = {'milk': 2.0, 'fish': 5.0, 'beer': 4.0}


def view_product_list(item_dict):  # Karolis Venckus
    print("Product List:")
    for item_name, item_weight in item_dict.items():
        print(f"{item_name}: {item_weight}")


def remove_if_zero(item_dict):   # Karolis Venckus
    empty_products = [product for product, details in item_dict.items() if details == 0]

    for product in empty_products:
        del item_dict[product]
    if empty_products:
        print(f"{', '.join(empty_products)} removed from the product list.")


# ------------------- ADD_PRODUCT -----------------------------
# Funkcija pridėjimo į sąrašą. Jei toks produktas egzistuoja
# prie jo prideda count reikšmę
def add_product(product_dict, product_name, count):  # Karolis Jasadavičius
    # add products, 
    # if product is solid unit == kg
    # if product is liquid unit == litres (l)
    if product_name in product_dict:
        product_dict[product_name] += count
        print(f"{product_name} count changed successfully)")
    else:
        product_dict[product_name] = count
    # Pavyzdys patikrinimui su user input'ais.
    # added_product = input("Enter product name you wish to add: ")
    # product_count = float(input("Enter the amount you are adding: "))
    # add_product(products, added_product, product_count)
    # print(products)

# ------------------- REMOVE_PRODUCT --------------------------
# Funkcija produkto išėmimui iš sąrašo
# Count_reduce naudojame, kaip kintamąjį su kurio atemame produkto kiekį,
# jeigu paliekame 0, produktas istrinamas
def remove_product(product_dict, product_name, count_reduce=0): # Karolis Jasadavičius
    if product_name in product_dict:
        if count_reduce == 0:
            del product_dict[product_name]
            print(f"{product_name} removed successfully")
        else:
            product_dict[product_name] -= count_reduce
            print(f"{product_name} count lowered by {count_reduce} (Removed if reaches 0)")
            remove_if_zero(products)
    else:
        print(f"{product_name} is not in the fridge")


def calculate_fridge_mass(products_list):  # Milda Auglytė
    items_mass = 0
    for item in products_list:
        items_mass = items_mass + item
    return items_mass
# ------------------- PAVYZDYS -------------------------------
# print(products)
# remove_product_name = input("Enter the name of the product to update: ")
# if remove_product_name in products:
#     reduction = input("Enter the amount you want to reduce (leave blank for complete removal): ")
#     if len(reduction) == 0: # Patikriname ką iveda vartotojas/ar paliko tuščią
#         reduction = 0.0
#     else:
#         reduction = float(reduction) # Konvertuojame įvestą string
#     products = remove_product(products, remove_product_name, count_reduce=reduction)
#     print("Updated product list:", products)
# else:
#     print(f"{remove_product} is not in the product list.")


def calculate_fridge_mass(products):  # Milda Auglytė
    products_list = list(products.values())
    items_kg = 0
    for item in products_list:
        items_kg = items_kg + item
    return items_kg


# milk: 1, fish: 2
def check_recipe(products):
    recipe = input("Enter the recipe in the format 'ingredient: quantity' (e.g. 'apple: 2'):\n")
    servings = int(input("Enter the number of servings:\n"))
    recipe_dict = {}
    for item in recipe.split(','):
        item_list = item.split(':')
        recipe_dict[item_list[0].strip()] = float(item_list[1].strip())
    missing_items = {}
    for item, quantity in recipe_dict.items():
        if item not in products:
            missing_items[item] = quantity * servings
        elif products[item] < quantity * servings:
            missing_items[item] = products[item] - quantity * servings
    if missing_items:
        print("You don't have enough of the following ingredients to make this recipe:")
        for item, quantity in missing_items.items():
            print(f"{item}:{quantity}")
    print("You have enough ingredients to make this recipe.")
    for item, quantity in recipe_dict.items():
        products[item] -= quantity * servings
    if not len(missing_items) > 0:
        decision_to_take_out = input("Do you wanna take out products for recipe (yes / no)?: ")
        if decision_to_take_out == 'yes':    
            print(f"You used {servings} servings of the following ingredients:")
            for item, quantity in recipe_dict.items():
                print(f"{item}: {quantity * servings:.2f}")


# def shopping_list(products):
#     print("Shopping list:")
#     for item, data in products.items():
#         if data['weight'] <= 0:
#             print(f"{item}: {abs(data['weight']):.2f} {PRODUCT_TYPES[item]}")

# def num_dishes(products):
#     num_dishes = float('inf')
#     for item, data in products.items():
#         if item not in DISHES:
#             continue
#         if data['weight'] <= 0:
#             return 0
#         num_dishes = min(num_dishes, data['weight'] // DISHES[item])
#     return int(num_dishes)


while True:
    os.system('cls')
    print('----------[ FRIDGE ]----------\n')
    print('Choose 1 if you want to view product list')
    print('Choose 2 if you want to add product.')
    print('Choose 3 if you want to remove product.')
    print('Choose 4 if you want to count total mass of products.')
    print('Choose 5 if you want to check recipies.')
    print('Choose 9 if you want to exit program.')
    choice_main_menu = input('Choose: ')


    if choice_main_menu == '1':  # view product list
        os.system('cls')
        remove_if_zero(products)
        view_product_list(products)
        input('Smash ENTER to continue: ')


    elif choice_main_menu == '2':  # add product
        os.system('cls')
        added_product = input("Enter product name you wish to add: ")
        product_count = float(input("Enter the amount you are adding: "))
        add_product(products, added_product, product_count)
        input('Smash ENTER to continue: ')


    elif choice_main_menu == '3':  # remove product
        os.system('cls')
        product_name = input("Enter product name you wish to take: ")
        product_name_count = float(input("Enter the amount of product you're taking out: "))
        remove_product(products, product_name, product_name_count)  # NEED TO FIX
        input('Smash ENTER to continue: ')


    elif choice_main_menu == '4':  # count total mass of products.
        os.system('cls')
        print('\033[96mTotal fridge mass:\033[0m', calculate_fridge_mass(products))
        input('smash ENTER to continue: ')


    elif choice_main_menu == '5':  # recipe check.
        os.system('cls')
        print('RECIPE CHECKING: ')
        # print('Available ingredients: ', view_product_list(products))
        check_recipe(products)
        input('Smash ENTER to continue: ')


    elif choice_main_menu == '9':
        print('Exiting program..')
        break
