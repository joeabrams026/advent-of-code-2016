from collections import Counter
cols = []

with open('day06.data', 'r') as myfile:
    for line in myfile:
        for i,letter in enumerate(line):
            if len(cols) < i+1:
                cols.append(Counter())
            cols[i][letter]+=1

print "".join(col.most_common(1)[0][0] for col in cols)
