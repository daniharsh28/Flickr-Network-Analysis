import snap
import csv

# GNUPlot function is required to plot the degree distribution in working directory

G1 = snap.TNGraph.New()

reader = csv.reader(open('D:\AnonymizedEdgeList.csv','rb'))

for i in range(1,191772):
    G1.AddNode(i)

for row in reader:
    G1.AddEdge(int(row[0]),int(row[1]))

#print G1.Empty()

#print G1.GetNodes()

#print G1.GetEdges()

#Plotting Degree Distribution

snap.PlotInDegDistr(G1, "indegree", "in-degree Distribution")

snap.PlotOutDegDistr(G1, "outdegree", "out-degree Distribution", True)

# OutDegree

#OutDegV = snap.TIntPrV()
#snap.GetNodeOutDegV(G1, OutDegV)
#i = 0
#for item in OutDegV:
    #print "node ID %d: out-degree %d" % (item.GetVal1(), item.GetVal2())
#    i = i + 1
#    if i > 1000:
#        break

#Diameter of Graph
diam = snap.GetBfsFullDiam(G1, 100, False)
print 'Diameter of the graph is ' +str(diam)

#Average Local clustering Coefficient
#sum = 0
#NIdCCfh = snap.TIntFltH()
#snap.GetNodeClustCf(G1,NIdCCfh)
#for item in NIdCCfh:
#    sum += NIdCCfh[item]

#print sum/G1.GetNodes()

#Global Clustering Coefficient
#print snap.GetClustCf (G1, -1)

#No. of 3 loops in the graph
print 'No of 3-loops in the graph is ' + str(snap.GetTriads(G1))

#no. of bridges in the graph
G2 =snap.GetUnDir(G1)
#print G2.GetEdges()
G3 = snap.ConvertGraph(snap.PUNGraph, G1)
#print G3.GetEdges()
EdgeV = snap.TIntPrV()
snap.GetEdgeBridges(G3, EdgeV)
i = 0
for edge in EdgeV:
    i=i+1

print 'No. of bridges in the graph is ' + str(i)
