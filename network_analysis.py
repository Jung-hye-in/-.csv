#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
#자폐증관련유전자리스트 가져오기
#Q-value 0.1미만인 유전자 리스트만 가져오기 
A=pd.read_csv('자폐증관련유전자리스트.csv',header=None)
line=1
A_list=[0,]
while(line <len(A)):
    i=A[14][line]
    i=pd.to_numeric(i)
    if i <0.1:
        #print(i)
        A_list.append(line)
        line=line+1
    else:
        line=line+1
#print(A_list)
#print(len(A_list))
A_preprocessing=A.iloc[A_list]

import import_ipynb
#import FormattedFileProcessor as ffp
A_preprocessing.to_csv('A_Output.csv')
#B=ffp.read(A_preprocessing)
import network_utilities as nw
import networkx 
import random,os,numpy,copy
from matplotlib import pyplot as plt
A_network=networkx.Graph()
A_genelist=[]
count=1
while(count<len(A_preprocessing)):
    i=A_preprocessing[0][count]
    A_genelist.append(i)
    count=count+1
A_network.add_nodes_from(A_genelist)
n_node=A_network.number_of_nodes()
n_edge=A_network.number_of_edges()
new_graph=networkx.create_empty_copy(A_network)
nodes=list(A_network.nodes())

random_nodes=list(A_network.nodes())
random.shuffle(random_nodes)
new_graph.add_edges_from([(nodes[i],random_nodes[i]) for i in range (len(nodes))])
#edge의 개수 
def get_number_of_distinct_edges(G):
    edges_list=G.edges()
    edge_set=set()
    for id1, id2 in edges_list:
        edge_set.add((id1, id2))
    return len(edge_set)
networkx.draw(new_graph)
plt.show()
#equivalences = dict([(nodes[i],random_nodes[i]) for i in range(len(nodes))])
#new_graph.add_edges_from([ (equivalences[current_edge[0]], equivalences[current_edge[1]],
# A_network.get_edge_data(current_edge[0],current_edge[1])) for current_edge in A_network.edges() ])
#print(new_graph.edges())
#print(new_graph.nodes())
#print(L[0])
#print(A_network.edges())
#random_network=nw.randomize_graph(graph=A_network,randomization_type="preserve_topology")
#print(A_genelist)
#A_preprocessing


# In[5]:


#조현병관련유전자리스트 가져오기
#Q meta 0.1미만인 유전자 리스트만 가져오기 
S=pd.read_csv('조현병관련유전자리스트.csv',header=None)
line=1

S_list=[0,]
while(line <len(S)):
    i=S[12][line]
    i=pd.to_numeric(i)
    if i <0.1:
        #print(i)
        S_list.append(line)
        line=line+1
    else:
        line=line+1
#print(S_list)
print(len(S_list))
S_preprocessing=S.iloc[S_list]

import import_ipynb
#import FormattedFileProcessor as ffp
A_preprocessing.to_csv('A_Output.csv')
#B=ffp.read(A_preprocessing)
import network_utilities as nw
import networkx 
import random,os,numpy,copy
from matplotlib import pyplot as plt
S_network=networkx.Graph()
S_genelist=[]
count=1
while(count<len(S_preprocessing)):
    i=S_preprocessing[0][count]
    S_genelist.append(i)
    count=count+1
S_network.add_nodes_from(S_genelist)
n_node=S_network.number_of_nodes()
n_edge=S_network.number_of_edges()
new_graph=networkx.create_empty_copy(S_network)
nodes=list(S_network.nodes())

random_nodes=list(S_network.nodes())
random.shuffle(random_nodes)
new_graph.add_edges_from([(nodes[i],random_nodes[i]) for i in range (len(nodes))])
#edge의 개수 
def get_number_of_distinct_edges(G):
    edges_list=G.edges()
    edge_set=set()
    for id1, id2 in edges_list:
        edge_set.add((id1, id2))
    return len(edge_set)
networkx.draw(new_graph)
plt.show()


# In[ ]:





# In[ ]:




