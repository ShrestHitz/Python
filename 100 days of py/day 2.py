print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What % tip would you like to give? 10 12 15\n"))
people = int(input("How many people to split the bill? \n"))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)


