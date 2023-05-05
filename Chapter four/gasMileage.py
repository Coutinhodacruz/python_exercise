class Scanner:
    @staticmethod
    def nextInt(prompt: str) -> int:
        return int(input(prompt))


def main():
    total_miles = 0
    total_gallons = 0
    trips = 0

    while True:
        miles = Scanner.nextInt("Enter miles driven (-1 to quit): ")
        if miles == -1:
            break

        gallons = Scanner.nextInt("Enter gallons used: ")
        mpg = miles / gallons

        print(f"Miles per gallon for this tankful: {mpg:.2f}\n")

        total_miles += miles
        total_gallons += gallons
        trips += 1

        if trips > 0:
            combined_mpg = total_miles / total_gallons
            print(f"Total miles per gallon for all tankfuls: {combined_mpg:.2f}\n")

    print("Exiting...")


if __name__ == "__main__":
    main()
