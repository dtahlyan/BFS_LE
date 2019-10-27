#Author: Divyakant Tahlyan
# BFS-LE route choice set generation
#Python 3.7
import networkx as nx
import pandas as pd
import csv
import timeit
#import sys
import math
import random
#---------------------------------------------------------------------------#
#read list of LINK_IDs and corresponding lengths (meters)
Link_Length = pd.read_csv('data/Length.csv',low_memory=False, dtype={'LINK_ID':int, 'Shape_Length':float})
#---------------------------------------------------------------------------#
# read graph from txt
G = nx.read_edgelist('data/network.txt',create_using = nx.DiGraph(),delimiter = "," ,nodetype=int, data=(('LINK_ID',float),('TT',float),('Length',float)))
#---------------------------------------------------------------------------#
# used for writing line variable names
namespace = globals()
#---------------------------------------------------------------------------#
# create a queue class
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print(items,)

    def shuffle(self):
        random.shuffle(self.items, lambda: rr)

#---------------------------------------------------------------------------#
# read origin-destination node list
OD = pd.read_csv('data/OD.csv',low_memory=False)
#---------------------------------------------------------------------------#
rr = random.random()
#---------------------------------------------------------------------------#


#--------------------------Define stopping conditions------------------------#
Max_time = 3600 #Maximum time for route generation in seconds. 3600 seconds = 1 hour
Max_unique = 10 #Maximum number of unique routes to generate
#---------------------------------------------------------------------------#

# loop over origin destination pairs
for xx in range (1):
    print(str ('OD pair number is____') + str(xx))
    # ---------------------------------------------------------------------------#
    exhaust = 0
    # ---------------------------------------------------------------------------#
    j = 0  # number for route
    # ---------------------------------------------------------------------------#
    p = 0  # number of unique route
    stop = 0
    start = 0
    while (stop - start < Max_time) and p < Max_unique and exhaust == 0:
        start = timeit.default_timer()
        # ---------------------------------------------------------------------------#
        common = open('generated_files/common'+ '_'+str(xx) +'.csv' , 'a')
        cr = csv.writer(common, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        # ---------------------------------------------------------------------------#
        #shortest path
        a = OD['Origin'].values[xx] #origin node
        b= OD['Destination'].values[xx] # destination node

        # ---------------------------------------------------------------------------#
        # find neighbors of the starting node
        n = list(G.neighbors(a))

        if len(n) > 1:
            #print('please wait...')
            aa = a
        else:
            d = nx.astar_path(G, source=a, target=b, heuristic=None, weight='TT')
            ss = 0
            while len(n) < 2:
                n = list(G.neighbors(d[ss]))
                aa = d[ss]
                ss = ss + 1

        bb = 0
        for nn in n:
            bb = bb + 1
            namespace['z_%d' % bb] = G[aa][nn]['LINK_ID']
            namespace['x_%d' % bb] = G[aa][nn]['TT']
            namespace['c_%d' % bb] = G[aa][nn]['Length']

        # ---------------------------------------------------------------------------#
        # find shortest path between OD pair
        try:
            route_0 = nx.astar_path(G, source = a, target = b, heuristic=None, weight='TT')
        except (nx.NetworkXNoPath, nx.exception.NetworkXError) as e:
            print(e)
        q_0 = Queue() # initialize queue
        w_0 = Queue() # initialize queue
        l_0 = 0 # initialize length of shortest route
        ul_0 = 0 # initialize length of first unique route, also same as shortest route
        ull_0 = [] # initialize list of links of shortest route

        # ---------------------------------------------------------------------------#
        # write the shortest path in routes csv
        routes = open('generated_files/routes'+ '_'+str(xx) +'.csv', 'a') # open route link list file
        unique = open('generated_files/unique'+ '_'+str(xx) +'.csv', 'a') # open unique link list file
        wr = csv.writer(routes, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n') # preparing for writing shortest route links in csv
        for q in range(1, len(route_0)): # loop over number of links in shortest route
            u = route_0[q - 1]
            v = route_0[q]
            k = int(G[u][v]['LINK_ID'])
            q_0.enqueue(u)
            w_0.enqueue(v)
            l_0 = l_0 + G[u][v]['Length'] # length of shortest route
            wr.writerow([xx,0, k])
        q_0.shuffle()
        w_0.shuffle()

        # ---------------------------------------------------------------------------#
        # write shortest path in unique routes csv
        qr = csv.writer(unique, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for q in range(1, len(route_0)):
            u = route_0[q - 1]
            v = route_0[q]
            k = int(G[u][v]['LINK_ID'])
            ul_0 = ul_0 + G[u][v]['Length'] # length of shortest unique route
            ull_0.append(k)
            qr.writerow([xx,0, k])

        # ---------------------------------------------------------------------------#
        # start link removal
        for y in range(len(n)):
            namespace['q_%d' % (y + 1)] = Queue()
            namespace['w_%d' % (y + 1)] = Queue()
            namespace['list_%d' % (y + 1)] = []
            if y==0:
                dkt = 0
            else:
                G.remove_edge(aa, n[y-1])
            while namespace['q_%d' % y].size() > 1 and stop - start < Max_time and p < Max_unique:
                u = namespace['q_%d' % y].items.pop()
                v = namespace['w_%d' % y].items.pop()
                while u == aa or v == b:
                    u = namespace['q_%d' % y].items.pop()
                    v = namespace['w_%d' % y].items.pop()
                else:
                    dkt =0
                f = len(list(G.neighbors(v)))
                if f == 1:
                    #print(str("skip"))
                    pass
                else:
                    j = j + 1
                    #print(j)
                    pass
                    z = G[u][v]['LINK_ID']
                    x = G[u][v]['TT']
                    c = G[u][v]['Length']
                    G.remove_edge(u, v)
                    try:
                        namespace['route_%d' % j] = nx.astar_path(G, source = a, target = b, heuristic=None, weight='TT')

                        G.add_edge(u, v, TT=x, LINK_ID=z, Length=c)
                        namespace['l_%d' % j] = 0
                        namespace['rl_%d' % j] = []
                        for m in range(1, len(namespace['route_%d' % j])):
                            u = namespace['route_%d' % j][m - 1]
                            v = namespace['route_%d' % j][m]
                            k = int(G[u][v]['LINK_ID'])
                            intersect = set([(u, v)]) - set(namespace['list_%d' % (y + 1)])
                
                            if list(intersect) == []:
                                dkt = 0
                            else:
                                namespace['q_%d' % (y + 1)].enqueue(u)
                                namespace['w_%d' % (y + 1)].enqueue(v)
                                namespace['list_%d' % (y + 1)].append((u,v))
                            wr.writerow([xx,j, k])
                            namespace['rl_%d' % j].append(k)
                            namespace['l_%d' % j] = namespace['l_%d' % j] + G[u][v]['Length']
                        namespace['q_%d' % (y)].shuffle()
                        namespace['w_%d' % (y)].shuffle()
                        CF_List = []
                        w = 0
                        CF = 0
                        while w < p+1 and CF < 0.95:
                            dk = set(namespace['rl_%d' % j]) & set(namespace['ull_%d' % w])
                            dk = list(dk)
                            if dk == []:
                                CL = 0
                            else:
                                df = pd.DataFrame.from_dict(dk)
                                df.columns = ['LINK_ID']
                                zz = pd.merge(Link_Length, df, how='inner', on=['LINK_ID'])
                                CL = zz['Shape_Length'].sum()
                            CF = CL/math.sqrt(namespace['l_%d' % j]*namespace['ul_%d' % w])
                            CF_List.append(CF)
                            cr.writerow([xx,j,w,CF])
                            #print(str(CF))
                            w = w + 1
                        if w == p + 1 and CF < 0.95:
                            p = p + 1
                            print(str("unique route found--") + str(p))
                            namespace['ull_%d' % p] = []
                            namespace['ul_%d' % p] = namespace['l_%d' % j]
                            for f in range(1, len(namespace['route_%d' % j])):
                                u = namespace['route_%d' % j][f - 1]
                                v = namespace['route_%d' % j][f]
                                k = int(G[u][v]['LINK_ID'])
                                namespace['ull_%d' % p].append(k)
                                qr.writerow([xx,p, k])
                        stop = timeit.default_timer()
                        #klm = stop - start
                        #print(stop - start)

                    except (nx.NetworkXNoPath, nx.exception.NetworkXError) as e:
                        print(e)
                        G.add_edge(u, v, TT=x, LINK_ID=z, Length=c)

        bb = 0
        for nn in n:
            bb = bb + 1
            G.add_edge(aa, nn, TT=namespace['x_%d' % bb], LINK_ID=namespace['z_%d' % bb], Length=namespace['c_%d' % bb])
        exhaust = 1

#time = open('generated_files/time.csv', 'a') 
#gr = csv.writer(time, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
#gr.writerow([xx,klm])
#time.close()
unique.close()
common.close()
routes.close()
