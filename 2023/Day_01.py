#Varibles
temp1 = ''
temp2 = ''
first = True
x = []
y = []
final = 0

#Open and read file
f = open('x.txt', 'r')
for i in range(1000):
    x.append(f.readline())

#Main program
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
