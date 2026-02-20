# You just heard that one of your guests can’t
# make the dinner, so you need to send out a new set of invitations. You’ll
# have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in
# your list.


#! Building on guest list 

guest_list= ["agyei", "hanna", "edmund"]

#* guest couldn't make it 
print(f"{guest_list[2].title()} can't make it to dinner tomorrom!")

#* replacing edmund with john 
#? delete edmund
del guest_list[2]
#? add john to list
guest_list.append("john")
print(guest_list)

#* second set of invitation
#* invitation message
print(f"Hello {guest_list[0].title()}, consider this an ivitation to dinner tomorrow.")
print(f"Hello {guest_list[1].title()}, consider this an ivitation to dinner tomorrow.")
print(f"Hello {guest_list[2].title()}, consider this an invitation to dinner tomorrow.")