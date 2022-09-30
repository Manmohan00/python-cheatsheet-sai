# open the file
file = open("sample", "r")
#   w   - write
#   a   - append
#   wb  - write binary
#   rb  - read binary
#   r+  - read and write (shortcut)

# read the entire file content
#c = file.read()
#print("Entire file = " + c)

# read only n bytes
print(file.read(4))
print(file.read(2))
print(file.read(-1))
file.close()

# write
file = open("sample", "w")
file.write("Extra ine")
file.close()

file = open("sample", "r")
print(file.read())

# close the file after using
file.close()

