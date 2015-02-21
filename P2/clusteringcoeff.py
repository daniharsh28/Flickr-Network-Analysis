__author__ = 'Harsh'

import snap
import csv

G1 = snap.TNGraph.New()

reader = csv.reader(open('AnonymizedEdgeList.csv','rb'))

for i in range(1,191772):
    G1.AddNode(i)

for row in reader:
    G1.AddEdge(int(row[0]),int(row[1]))

sum = 0
NIdCCfh = snap.TIntFltH()
snap.GetNodeClustCf(G1,NIdCCfh)
for item in NIdCCfh:
    sum += NIdCCfh[item]
avgcoeff = sum/G1.GetNodes()
print 'Average clustering coefficient is ' + str(avgcoeff)

#Global Clustering Coefficient
print 'Global Clustering coefficient is ' + str(snap.GetClustCf (G1, -1))
