# You just found out that your new dinner table
# won’t arrive in time for the dinner, and now you have space for only two
# guests.
# Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names
# remain in your list. Each time you pop a name from your list, print a
# message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program.


#! Building on from guess list & more guest program


guest_list= ["agyei", "hanna", "john"]

#* Informing guest of bigger table
print(f"Hi {guest_list[0].title()}, we got a bigger table...Bring a plus one!")
print(f"Hi {guest_list[1].title()}, we got a bigger table...Bring a plus one!")
print(f"Hi {guest_list[2].title()}, we got a bigger table...Bring a plus one!")

#? add one new guest to the beggining of the list 
guest_list.insert(0, "jane")

#? add one new guest to the middle of the list 
guest_list.insert(2,"doe")

#? add one new guest to the end of the list 
guest_list.append("saint")

print(guest_list)

#* New set of invitations 
print(f"Hello {guest_list[0].title()}, you are invited to dinner tomorrow!")
print(f"Hello {guest_list[1].title()}, you are invited to dinner tomorrow!")
print(f"Hello {guest_list[2].title()}, you are invited to dinner tomorrow!")
print(f"Hello {guest_list[3].title()}, you are invited to dinner tomorrow!")
print(f"Hello {guest_list[4].title()}, you are invited to dinner tomorrow!")
print(f"Hello {guest_list[5].title()}, you are invited to dinner tomorrow!")


#* view guest list to print only two guest can be invited 
print("\nThis is the current list: ")
print(guest_list)

print("I am so sorry, we can only invite two people to dinner due to limited space.")

#? removing guest from list with message
print(f"Hi {guest_list[5].title()}, your dinner invitation is cancelled and I am so sorry.")
guest_list.pop(5)

print(f"Hi {guest_list[4].title()}, your dinner invitation is cancelled and I am so sorry.")
guest_list.pop()

print(f"Hi {guest_list[-1].title()}, your dinner invitation is cancelled and I am so sorry.")
guest_list.pop()

print(f"Hi {guest_list[2].title()}, your dinner invitation is cancelled and I am so sorry.")
guest_list.pop(2)

# ! view current guest list
print("----This is the new guest list-----")
print(guest_list)

#* invitation message to guest list
print(f"You're are still invited to dinner, {guest_list[0].title()}.")
print(f"You're are still invited to dinner, {guest_list[-1].title()}.")

print("\n")
#? empty list
del guest_list[0]
del guest_list[-1]

print("\t-----This is the current guest list-----")
print(guest_list)