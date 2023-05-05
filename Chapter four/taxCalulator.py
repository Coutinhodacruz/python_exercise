class Scanner:
    @staticmethod
    def nextInt(prompt: str) -> int:
        return int(input(prompt))

    @staticmethod
    def nextFloat(prompt: str) -> float:
        return float(input(prompt))


def calculate_tax(earnings: float) -> float:
    if earnings <= 30000:
        return earnings * 0.15
    else:
        return 30000 * 0.15 + (earnings - 30000) * 0.20


def main():
    citizens = [
        ("Alice", 25000.0),
        ("Bob", 40000.0),
        ("Charlie", 20000.0),
    ]

    for name, earnings in citizens:
        print(f"Enter earnings for {name}: ")
        earnings_input = Scanner.nextFloat("")
        tax = calculate_tax(earnings_input)
        print(f"Total tax for {name}: {tax:.2f}\n")

    print("Exiting...")


if __name__ == "__main__":
    main()
