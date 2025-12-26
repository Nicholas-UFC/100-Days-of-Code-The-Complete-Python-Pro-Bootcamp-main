print("Welcome to the secret auction program.")

Player = {}
run = "yes"
Big_name = ""
Big_bid = 0

while run == "yes":
    name = input("What is your name? ")
    bid = int(input("What's your bid? "))

    Player[name] = bid

    run = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    print("\n" * 100)
    if run == "no":
        for index in Player:
            if Player[name] > Big_bid:
                Big_name = index
                Big_bid = Player[index]

        print(f"The winner is {Big_name} with a bid of R${Big_bid}")
