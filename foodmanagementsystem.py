print("---Welcome to Food Management System---")

foods = []
while True:
    print("----------------------------------------")
    print("0. Exit")
    print("1. Add Foods")
    print("2. Remove Foods")
    print("3. View All Favourite  Foods")
    op = int(input("Please Choose a option : "))
    if op == 0:
        break
    elif op == 1:
        food = input('Enter  your favourite food : ')
        foods.append(food)
        print(f'{food} added successfully ')
    elif op == 2:
        food = input('which food do you want remove : ')
        if food in foods:
            foods.remove(food)
            print(f'{food} remove successful')
        else:
            print(f'{food} not exists ')
    elif op == 3:
        if foods:
            print('Your all favourite foods : ')
            for ind, food in enumerate(foods, start=1):
                print(f"{ind}.{food}")
        else:
            print('No food exists ')
    else:
        print('Wrong input .. try again !!!')

print('Thanks For Using Food Management System')