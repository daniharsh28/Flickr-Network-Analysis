__author__ = 'Harsh'

import csv
import snap
import operator

G1 = snap.TNGraph.New()

#Please also run matlab file for the same!
# This method requires directed graph to convert into undirected graph!
# Because of undirected graph similarity values might change!
reader = csv.reader(open('D:\AnonymizedEdgeList.csv','rb'))

for i in range(1,191772):
    G1.AddNode(i)

for row in reader:
    G1.AddEdge(int(row[0]),int(row[1]))

G2 =snap.GetUnDir(G1)
#print G2.GetEdges()
G3 = snap.ConvertGraph(snap.PUNGraph, G2)

NIdEigenH = snap.TIntFltH()
snap.GetEigenVectorCentr(G3, NIdEigenH)

dict = {}
for item in NIdEigenH:
    dict[item] = NIdEigenH[item]

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse= True)

print sorted_dict[0]
print sorted_dict[1]
print sorted_dict[2]
