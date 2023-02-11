print("Ready to get your spending in check? Lets start with some common outgoings..")

rent = input ("Rent: £")
bills = input("Bills (Water, Gas & Electric): £")
food = input ("Food: £")
phoneBill = input ("Phone Bill: £")
tv = input ("TV/Broadband: £")
gym = input("Gym Membership: £")

totalSpending = int(rent) + int(bills) + int(food) + int(phoneBill) + int(tv) + int(gym) 

print("£",totalSpending)