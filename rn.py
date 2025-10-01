import random
Pass = input('what nubmer are you searchig for: ')
iter = 1000
Num = ""

for i in range(iter-1):
    Num += str(random.randint(10000, 60000))
Num += "12345"
"""
with open("wrd.txt", "w") as file:
    file.write("testing5")
"""
print(Num)
found = False
print(Num.find("12345"))

if "12345" in Num:
    print("found")

"""
for i in range(iter*5-4):
    print(Num[i:i+5])
    if Num[i:i+5] == Pass:
        print("found at index", i)
        found = True
        #break
if not found:
    print("not found")"""