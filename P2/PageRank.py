__author__ = 'Harsh'

import csv
import snap
import operator

G1 = snap.TNGraph.New()

reader = csv.reader(open('AnonymizedEdgeList.csv','rb'))

for i in range(1,191772):
    G1.AddNode(i)

for row in reader:
    G1.AddEdge(int(row[0]),int(row[1]))

PRankH = snap.TIntFltH()
snap.GetPageRank(G1, PRankH)
dict = {}
for item in PRankH:
   # print item, PRankH[item]
    dict[item] = PRankH[item]

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse= True)

print sorted_dict[0]
print sorted_dict[1]
print sorted_dict[2]
