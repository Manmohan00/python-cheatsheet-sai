a = [0, 1, 2, 3, 4, 9]
for i in a:
    print(i, end=" ")    # ,end=" " wont let the print go to next line automatically

# for loop with strings
# to check how many letter "a" are present
count = 0
s = "helpsfe u sadwfweasfsda"
for x in s:
    if x == 'a':
        count += 1
print("\n" + str(count))
