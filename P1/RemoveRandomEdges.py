import csv
import random
import matplotlib.pyplot as plt
import time
import snap

#fout = open('edges1.txt', "w")

X = []
#noOfNodesX = []


for i in range(91,92,10):

  if i== 101:
      i = 100

  fin = open('D:\AnonymizedEdgeList.csv', "r")
  reader = csv.reader(fin)

  data_list = []
  
  for row in reader:
    data_list.append(row[0]+' '+row[1])
    
  noedges = int(i * len(data_list)/100)
  print noedges
  
  for j in range(1,noedges+1):
    line = random.sample(range(1,len(data_list)), 1)
    #print line[0]
    data_list.pop(line[0])
    #print str(line[0]) + "popped"

  print 'Length of Data List is ' + str(len(data_list))
  
  with open('test.csv', 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    for item in data_list:
       l = []
       l = item.split()
       a.writerow([l[0],l[1]])

  readerNew = csv.reader(open('test.csv','r'))

  G1 = snap.TUNGraph.New()

  for k in range(1,191772):
      G1.AddNode(k)
      
  for r in readerNew:
      G1.AddEdge(int(r[0]),int(r[1]))

  MxScc = snap.GetMxScc(G1)
  
  print 'No of nodes in strongly connected component is ' + str(MxScc.GetNodes())

  X.append([i,MxScc.GetNodes()])

plt.plot(*zip(*X))
plt.xlabel('Size of X (%)')
plt.ylabel('Size of  Connected Component (No of Nodes)')
plt.show()
    

