Day 10: Binary Numbers
if __name__ == '__main__':
    n = int(input())
    s = bin(n)[2:]
    length = 0
    max_l = 0
    for i in range(len(s)):
        if s[i] == '1':
            length += 1
            if length > max_l:
                max_l = length
        else:
            length = 0
    print(max_l)