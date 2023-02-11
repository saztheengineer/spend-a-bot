print("Ready to get your spending in check? Lets start with some common outgoings..")

rent = input ("Rent: £")
food = input ("Food: £")
phoneBill = input ("Phone Bill: £")
tv = input ("TV/Broadband: £")
gym = input("Gym Membership: £")
bills = input("Bills (Water, Gas & Electric): £")


totalSpending = int(rent) + int(food) + int(phoneBill) + int(tv) + int(gym) + int(bills)

print(totalSpending)