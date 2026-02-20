# Working with one of the programs from Exercises 3-4
# through 3-7 (pages 41–42), use len() to print a message indicating the
# number of people you’re inviting to dinner.


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


#! NUMBER OF PEOPLE INVITED FOR DINNER 

print("\nNumber of guest invited to dinner:")
print(f"I have {len(guest_list)} guests coming for dinner.")