import re

fh = open('actual.txt')
lis = [ ]
for line in fh:
    line = line.rstrip()
    w = re.findall('[0-9]+', line)
    if len(w) != 0:
        for i in w:
            lis.append(int(i))
print(sum(lis))
