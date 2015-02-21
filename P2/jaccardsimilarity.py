
from __future__ import division
import snap
import csv
from sets import Set
import operator

G1 = snap.TNGraph.New()

reader = csv.reader(open('AnonymizedEdgeList.csv','rb'))

for i in range(1,191772):
    G1.AddNode(i)

for row in reader:
    G1.AddEdge(int(row[0]),int(row[1]))

dict = {}
for i in range(1,1001):
    print i
    for j in range(i,1001):
        print j
        if i == j:
            continue
        seta = Set([])
        setb = Set([])
        NodeVec1 = snap.TIntV()
        snap.GetNodesAtHop(G1, i, 1, NodeVec1, True)
        for item in NodeVec1:
            seta.add(item)
        NodeVec2 = snap.TIntV()
        snap.GetNodesAtHop(G1, j, 1, NodeVec2, True)
        for item in NodeVec2:
            setb.add(item)
        a = len(seta.intersection(setb))
        b = len(seta.union(setb))
        try:
            jaccard = a / b
        except Exception:
            jaccard = 0
        dict[(i,j)] = jaccard

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse= True)

print sorted_dict[0]
