import sys

try:
    with open(sys.argv[1], 'r') as f:
        contents = f.readlines()
        list2 = [x.strip() for x in contents]
except:
    print("No input file specified!!")
    sys.exit(1)
seq = []
for i in list2:
    seq.append(float(i))
a =[]
def sublist(list1):
    sub = [[]]
    for i in range(len(list1)+1):
        for j in range(i+1,len(list1)+1):
            sub1 = list1[i:j]
            sub.append(sub1)
    return sub


a = sublist(seq)

b = list(map(sum,a))

index = (b.index(max(b)))

print("The subsequence with max sum is ",a[index]," and the sum is ",max(b))