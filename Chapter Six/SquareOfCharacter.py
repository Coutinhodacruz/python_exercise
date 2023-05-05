def square_of_characters(side, fill_character):
    for i in range(side):
        print(fill_character * side)



side = int(input("Enter the side length of the square: "))
fill_char = input("Enter the fill character: ")
square_of_characters(side, fill_char)
