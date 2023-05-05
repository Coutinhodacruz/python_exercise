x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

if x1 == x2:
    print("The points are on a line perpendicular to the y-axis.")
elif y1 == y2:
    print("The points are on a line perpendicular to the x-axis.")
else:
    print("The points are not on a line perpendicular to either axis.")
