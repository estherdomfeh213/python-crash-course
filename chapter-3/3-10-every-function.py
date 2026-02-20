# Think of things you could store in a list. For
# example, you could make a list of mountains, rivers, countries, cities,
# languages, or anything else you’d like. Write a program that creates a list
# containing these items and then uses each function introduced in this
# chapter at least once.


mountains = ["Mount Everest", "Kangchenjunga", "Makalu", "Cho Oyu"]
rivers = ["yellow river", "nile", "volga"]
countries = ["nigeria", "kenya", "togo"]

#* using sorted()

print(mountains)
print(sorted(mountains))
sorted = sorted(mountains, reverse=True)
print(mountains)

#* using reverse 
print(rivers)
rivers.reverse()
print(rivers)
#! reverse to revert to original list
rivers.reverse()
print(rivers)

#* Using sort function 
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)

#* Using len
print(len(mountains))
print(len(rivers))
print(len(countries))