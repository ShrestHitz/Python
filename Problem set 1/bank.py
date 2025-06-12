greetings = input("Greetings: ")

if greetings.strip().startswith("Hello"):
    print("$0", end="")
elif greetings.strip().startswith ("H"):
    print("$20", end="")
else:
    print("$100", end="")
