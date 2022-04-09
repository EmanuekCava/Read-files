def availble(optionString):
    print("\n{} is not an availble option. Please try again".format(optionString))

def filterColumn():
    index = input("\nWrite an index column name: ")
    return index

def inputsConditionals():
    column = input("\nWrite a column value: ")
    row = input("Write a row value from {}: ".format(column))

    try:
        rowInt = int(row)
    except:
        availble(rowInt)

    return column, rowInt

def menu():

    option = 0

    while option < 1 or option > 7:
        print("\n\t.::Welcome::.")
        print("What type of file are you going to work with?\n")
        print("1: Excel")
        print("2: CSV OR ZIP")
        print("3: JSON")
        print("4: SQL")
        print("5: TXT or XML")
        print("6: HTML")
        print("7: PDF") 

        optionString = input("\nSelect an option: ")

        try:
            option = int(optionString)

            if option < 1 or option > 7:
                availble(option)

        except:
            availble(optionString)
        
    return option

def menuOption():

    option = -1

    while option < 0:

        print("\n\t.::MENU OF OPTIONS::.")
        print("\n0: Exit")
        print("1: Show columns")
        print("2: Print rows from one column")
        print("3: Print rows from a set of columns")
        print("4: Order alphabetically")
        print("5: Filter by index")
        print("6: Filter by a set of indices")
        print("7: Filter by a set of indices and columns")
        print("8: Filter by a number conditional")
        print("9: Filter a column by a text")
        print("10: Transform data")
        print("11: First values")
        print("12: Last values")

        optionString = input("\nSelect an option: ")

        try:
            option = int(optionString)

            if option < 0:
                availble(option)
        except:
            availble(optionString)

    return option

def nextStep():

    option = -1

    while option < 0 or option > 3:

        print("\n\t.::MENU OF OPTIONS::.")
        print("\n0: Exit")
        print("1: New file")
        print("2: Use the same file")
        print("3: Use the same file with changes")

        optionString = input("\nSelect an option: ")

        try:
            option = int(optionString)

            if option < 0:
                availble(option)
        except:
            availble(optionString)

    return option