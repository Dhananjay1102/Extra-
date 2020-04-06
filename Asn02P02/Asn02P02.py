import sys
try:
    with open(sys.argv[1], 'r') as f:
        contents = f.readlines()
        string = [x.strip() for x in contents]
except:
        print("No input file specified!!")
        sys.exit(1)
m = int(input("Enter or specify the number to rotate the given words: "))
b =[]
i=0
j=0
while  i<m :
    b.append(string[i])
    i+=1
del string[0:m]

while  j<len(b) :
    string.append(b[j])
    j+=1

for x in range(len(string)):
    print(string[x],end=' ')
