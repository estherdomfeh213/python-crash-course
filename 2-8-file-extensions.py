# Python has a removesuffix() method that works
# exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable
# called filename. Then use the removesuffix() method to display the filename
# without the file extension, like some file browsers do.


# ? Assign the value 'python_notes.txt' to a variable called filename

filename = 'python_notes.txt'

cleaned_name = filename.removeprefix("python_")

print(cleaned_name)