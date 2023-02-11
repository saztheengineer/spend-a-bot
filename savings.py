#intro
print("Welcome to Spend-a-Bot!") 

name = input("What's your name? ")

print()
print("Hi 👋,", name, "! I'm Cody!🤖")
print()
print("Do you want to know what you're spending monthly on all your essential bills? Well you've come to the right place!")
print()
print("Don't worry if some of these dont apply to you, just put 0 and we'll remove it from the calculations.")
print()

#salary info
salary = input("Okay first, what is your average salary income a month? £")
print()
print("Great! Lets see what chunk of that is for bills then..")
print()

#bill breakdowns
rent = input ("Rent 🏡: £")
bills = input("Utility bills(Water, Gas & Electric) 🔧: £")
food = input ("Food shop 🥦: £")
phoneBill = input ("Phone Bill 📱: £")
tv = input ("TV/Broadband 📺: £")
gym = input("Gym Membership 🦾: £")
pet = input("Pet bills 🐾: £")
print()

#extra outgoings
print("Do you have any other monthly expenses that I haven't mentioned? ")

extraExsp = input("yes or no?")
if extraExsp == "yes" or extraExsp == "Yes":
    print()
    print("Crikey! You're quite the big spender! I think we'll stick with what we've got for now, I think my wires will spark!")
elif extraExsp == "no" or extraExsp == "No":
    print()
    print("Okay lets see what your monthly bill total is...")
else:
    print()
    print("I don't know what you just said but we'll just pretend that never happened..")
print()


#results..
totalSpending = int(rent) + int(bills) + int(food) + int(phoneBill) + int(tv) + int(gym) + int(pet)

print("Okay so, drum roll please..")
print()
print("🥁🥁🥁")
print()
print("Your monthly total spend is: £",totalSpending)
print()

print("Now lets see what you have left over..")

leftOver = int(salary)-int(totalSpending)
print("£",leftOver)
print()

#end of the chat
print("So is that what you were expecting? Do you have as much money left over as you thought?") 
print("Enough for a cheeky takeaway tonight though, right? 🍕")