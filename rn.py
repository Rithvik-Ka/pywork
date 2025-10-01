import random
Pass = input('what nubmer are you searchig for: ')
iter = 1000
Num = ""
for i in range(iter):
    Num += str(random.randint(10000, 60000))


with open("wrd.txt", "w") as file:
    file.write("testing5")

print(Num)


for i in range(iter):
    if Num[i:i+5] == Pass:
        print("found at index", i)
        break
print("not found")