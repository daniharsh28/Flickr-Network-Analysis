__author__ = 'Harsh'

import snap
import csv
import math
import operator

# To plot the degree distribution GNUplot is necessary in working directory
G1 = snap.TNGraph.New()

reader = csv.reader(open('AnonymizedEdgeList.csv','rb'))

for i in range(1,191772):
    G1.AddNode(i)

for row in reader:
    G1.AddEdge(int(row[0]),int(row[1]))

G2 = snap.ConvertGraph(snap.PUNGraph, G1)

OutDegV = snap.TIntPrV()
snap.GetNodeOutDegV(G2, OutDegV)

sum = 0
for item in OutDegV:
    sum = sum + item.GetVal2()

avgdegree = sum/G2.GetNodes()

Rnd = snap.TRnd()
G3 = snap.GenPrefAttach(G2.GetNodes(), avgdegree, Rnd)

#1. Average Path Length

sumlen = 0
for i in range(0,100):
    x = snap.TInt.GetRnd(191772)
    y = snap.TInt.GetRnd(191772)
    Length = snap.GetShortPath(G3,x,y)
    sumlen = sumlen + Length

avgLen = sumlen/100
print avgLen

#2.Clustering Coefficient

GraphClustCoeff = snap.GetClustCf(G3, -1)
print GraphClustCoeff

#3. Degree Distribution

snap.PlotInDegDistr(G3, "indegree_prefattach", "prefattach in-degree Distribution")

snap.PlotOutDegDistr(G3, "outdegree_prefattach", "prefattach out-degree Distribution")

#4. Centrality measures

#1.) PageRank

PRankH = snap.TIntFltH()
snap.GetPageRank(G3, PRankH)
dict = {}
for item in PRankH:
   # print item, PRankH[item]
   dict[item] = PRankH[item]

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse= True)

print sorted_dict[0]
print sorted_dict[1]
print sorted_dict[2]

#2.) EigenVectorCentrality

#G3 = snap.ConvertGraph(snap.PUNGraph, G2)

NIdEigenH = snap.TIntFltH()
snap.GetEigenVectorCentr(G3, NIdEigenH)

dict1 = {}
for item in NIdEigenH:
    dict1[item] = NIdEigenH[item]

sorted_dict1 = sorted(dict1.items(), key=operator.itemgetter(1), reverse= True)

print sorted_dict1[0]
print sorted_dict1[1]
print sorted_dict1[2]

#3.) InDegree Centrality

InDegV = snap.TIntPrV()
snap.GetNodeInDegV(G3, InDegV)

dict2 = {}
for item in InDegV:
    dict2[item.GetVal1()] = item.GetVal2()

sorted_dict2 = sorted(dict2.items(), key=operator.itemgetter(1), reverse= True)

print sorted_dict2[0]
print sorted_dict2[1]
print sorted_dict2[2]
