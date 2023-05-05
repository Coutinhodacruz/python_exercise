print("Pythagorean Triples (side1, side2, hypotenuse):\n")
for side1 in range(1, 501):
    for side2 in range(side1, 501):
        for hypotenuse in range(side2, 501):
            if side1**2 + side2**2 == hypotenuse**2:
                print(f"({side1}, {side2}, {hypotenuse})")
