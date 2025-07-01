# TODO-1: Ask the user for input
auction = {}
auction_over = False

while not auction_over:

    name = input("Please enter your name: ")
    price = int(input("Please enter your bid: "))

    # TODO-2: Save data into dictionary {name: price}

    auction[name] = price

    endAuction = input("Are there any other bidders? 'y' for yes, 'n' for no:")

    if endAuction == 'n':
        auction_over = True


# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

winning_bid = 0

for bid in auction:
    if auction[bid] > winning_bid:
        winning_bid = auction[bid]


print(f"The winning bid is: {winning_bid}")