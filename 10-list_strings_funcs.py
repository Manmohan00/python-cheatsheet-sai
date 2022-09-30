n = [1, 2, 3]
print(n)

n.append(4)
print(n)

n.insert(2, 2.5)
print(n)

print(n.index(3))

#max(list): Returns the maximum value.
#min(list): Returns the minimum value.
#list.count(item): Returns a count of how many times an item occurs in a list.
#list.remove(item): Removes an item from a list.
#list.reverse(): Reverses items in a list. 


s = "Num = {1} {0} ".format(1, 2)
print(s)

print(", ".join(["spam", "eggs", "ham" ])) #prints "spam, eggs, ham"
print("Hello ME".replace("ME", "world")) #prints "Hello world"
print("This is a sentence.".startswith("This")) # prints "True"
print("This is a sentence.".endswith("sentence.")) # prints "True"
print("This is a sentence.".upper()) # prints "THIS IS A SENTENCE."
print("AN ALL CAPS SENTENCE".lower()) #prints "an all caps sentence"
print("spam, eggs, ham".split(", ")) #prints "['spam', 'eggs', 'ham']"
