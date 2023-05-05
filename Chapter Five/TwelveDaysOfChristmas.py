def print_day(day):
    switcher = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    return switcher.get(day)


def print_verse(day):
    switcher = {
        1: "A partridge in a pear tree.",
        2: "Two turtle doves, and",
        3: "Three French hens,",
        4: "Four calling birds,",
        5: "Five golden rings,",
        6: "Six geese a-laying,",
        7: "Seven swans a-swimming,",
        8: "Eight maids a-milking,",
        9: "Nine ladies dancing,",
        10: "Ten lords a-leaping,",
        11: "Eleven pipers piping,",
        12: "Twelve drummers drumming,"
    }
    return switcher.get(day)


def print_song():
    for day in range(1, 13):
        print(f"On the {print_day(day)} day of christmas, ")
        print("My true love gave to me: ")
        for gift_day in range(day, 0, -1):
            if gift_day == 1:
                if day == 1:
                    print("A partridge in a peer tree")
                else:
                    print(print_verse(gift_day))
            else:
                print(print_verse(gift_day))
        print("\n")


print_song()
