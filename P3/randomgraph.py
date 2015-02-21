__author__ = 'Harsh'

import snap
import csv
import math
import operator
# To plot the degree ditribution GNUplot is necessary in current directory.
G1 = snap.TNGraph.New()

reader = csv.reader(open('AnonymizedEdgeList.csv','rb'))

for i in range(1,191772):
    G1.AddNode(i)

for row in reader:
    G1.AddEdge(int(row[0]),int(row[1]))

G2 = snap.GenRndGnm(snap.PNGraph, G1.GetNodes(), G1.GetEdges(), True)

#1. Average Path Length
# Average Path length is same as diameter in random graphs

result_degree = snap.TIntV()
snap.GetDegSeqV(G2, result_degree)
sum=0;
for i in range(0,result_degree.Len()):
    sum = sum+result_degree[i];

avg = sum/G2.GetNodes()
avpl = math.log(G2.GetNodes(),2)/math.log(avg,2)

print avpl

#2. Clustering Coefficient

GraphClustCoeff = snap.GetClustCf (G2, -1)
print GraphClustCoeff

#3. Degree Distribution

snap.PlotInDegDistr(G2, "indegree_random", "Random in-degree Distribution")

snap.PlotOutDegDistr(G2, "outdegree_random", "Random out-degree Distribution")

#4. Centrality measures

#1.) PageRank

PRankH = snap.TIntFltH()
snap.GetPageRank(G2, PRankH)
dict = {}
for item in PRankH:
   # print item, PRankH[item]
   dict[item] = PRankH[item]

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse= True)

print sorted_dict[0]
print sorted_dict[1]
print sorted_dict[2]

#2.) EigenVectorCentrality

G3 = snap.ConvertGraph(snap.PUNGraph, G2)

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
snap.GetNodeInDegV(G2, InDegV)

dict2 = {}
for item in InDegV:
    dict2[item.GetVal1()] = item.GetVal2()

sorted_dict2 = sorted(dict2.items(), key=operator.itemgetter(1), reverse= True)

print sorted_dict2[0]
print sorted_dict2[1]
print sorted_dict2[2]
