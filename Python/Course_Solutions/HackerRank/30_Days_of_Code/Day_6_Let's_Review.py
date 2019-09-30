x = int(input())

for iLines in range(x):
    line = input()
    odd = ''
    even = ''
    for each in range(len(line)):
        if each %2 == 0:
            even += line[each]
        else:
            odd += line[each]
    print(even+' '+odd)