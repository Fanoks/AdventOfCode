temp1, temp2, first, x, y, final = '', '', True, [], [], 0
f = open('a.txt', 'r')
for i in range(1000):
    x.append(f.readline())
for i in range(1000):
    for element in x[i]:
        if element.isdigit() and first == True:
            temp1, temp2 = element, element
            first = False
        elif element.isdigit():
            temp2 = element
    first = True
    y.append(int((temp1 + temp2)))
for i in range(1000):
    final += y[i]
print(final)
