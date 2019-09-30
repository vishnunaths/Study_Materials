Day 8: Dictionaries and Maps
# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
phoneBook = {}
for i in range(x):
    entry = input()
    entry = entry.split()
    phoneBook[entry[0]] = entry[1]
while True:
    try:
        zzz = input()
        if zzz in list(phoneBook.keys()):
            print(zzz+'='+phoneBook[zzz])
        else:
            print('Not found')
    except:
        break