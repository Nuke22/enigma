alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
connector = [1, 15, 16, 13, 18, 9, 24, 6, 20, 17, 21, 3, 8, 25, 19, 2, 23, 10, 4, 0, 22, 14, 12, 5, 7, 11]
b = []
for i in range(0, 26):
    a = alphabet[connector[i]]
    b.extend(a)
print(b)