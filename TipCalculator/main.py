def main():
    print("Welcome to the tip calculator!")
    bill = float(input("What was the total bill? $"))
    tipPercent = int(input("How much tip would you like to give? %10, %12, or %15? %"))
    numPeople = int(input("How many people to split the bill? "))
    amountPerPerson = (bill + (bill/100*tipPercent)) / numPeople
    finalAmount = "{:.2f}".format(amountPerPerson)

    print(f"Each person should pay: £{finalAmount}")


main()