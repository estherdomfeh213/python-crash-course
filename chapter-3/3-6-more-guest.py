# You just found a bigger dinner table, so now more space
# is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.

 #! Building on guest list 

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
