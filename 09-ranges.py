n = list(range(5))
print(n)

for i in range(6):
    print(str(i), end=" ")
print()
n = list(range(3, 20, 3))
for i in n:
    print(str(i), end=" ")
print("\n" + str(n[0:3]))
print(n[:5])
print(n[3:])
#reverse of n
print(n[::-1])
