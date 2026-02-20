# Think of at least five places in the world you’d like
# to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly;
# just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing
# the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s
# back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.



#* list of five places i like to visit
location_to_visit = ["singapore", "belguim", "germany", "ethiopia", "london"]

# original_list = location_to_visit

# print(original_list)

#? original list 
print(location_to_visit)

#? Print list in alphabetical order w/o modifying original list
print(sorted(location_to_visit))

#? original list
print(location_to_visit)

#? reverse-alphabetical using sorted()
print("\n Here is a sorted=reverse")
sorted_location_to_visit = sorted(location_to_visit, reverse=True)
print(sorted_location_to_visit)

#? reverse to change order 
print("\nReverse Order")
location_to_visit.reverse()
print(location_to_visit)

#? reserve to change order again-i can revert to the original order by applying reverse again to the list the second time 
print("\n Reverse again to revert to original list")
location_to_visit.reverse()
print(location_to_visit)


#? sort to change alphabetical order
print("\n Permantly sort")
location_to_visit.sort()
print(location_to_visit)

#? sort in reverse-alphabetical order
print("\nReserve Sort")
location_to_visit.sort(reverse=True)
print(location_to_visit)