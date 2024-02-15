print("🎲🎲 Roll it 13 🎲🎲")


# loop for testing purposes

while True:
    want_instructions = input("Do you want to read the instructions? ").lower()

    # check user enter yes (y) or no (n)
    if want_instructions == "yes": or want_instructions == "y":
        print("you choose yes")
    elif want_instructions == "no": or want_instructions == "n":
        print("you choose no")
    else:
        print("You did not choose a valid response")

