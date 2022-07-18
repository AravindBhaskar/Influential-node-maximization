#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Adding vertex
def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print("Vertex already exists.")
    else:
        vertices_no = vertices_no + 1
        graph[v] = []
# Adding edge and weight
def add_edge(v1,v2,e):
    global graph
    if v1 not in graph:
        print("Vertex does not exist")
    elif v2 not in graph:
        print("Vertex does not exist")
    else:
        temp = [v2, e]
        graph[v1].append(temp)
# print graph
def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print(vertex,"->",edges[0],"edge weight: ", edges[1])
# code
graph = {}
vertices_no = 0
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
print_graph()

print ("Internal representation: ", graph)


# In[9]:


graph = {
    '1' : ['2','3'],
    '2' : ['4','5'],
    '3' : ['6'],
    '4' : [],
    '5' : ['6'],
    '6' : []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        
        for vertex in graph[s]:
            if vertex not in visited:
                visited.append(vertex)
                queue.append(vertex)
                
bfs(visited, graph,'1')


# In[10]:


graph = {
    '1' : ['2','3'],
    '2' : ['4','5'],
    '3' : ['6'],
    '4' : [],
    '5' : ['6'],
    '6' : []
}
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for vertex in graph[node]:
            dfs(visited, graph, vertex)

dfs(visited, graph, '1')


# In[3]:


import networkx as nx
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings; warnings.simplefilter('ignore')


# In[4]:


G_symmetric = nx.Graph()


# In[5]:


G_symmetric.add_edge('Steven',  'Laura')
G_symmetric.add_edge('Steven',  'Marc')
G_symmetric.add_edge('Steven',  'John')
G_symmetric.add_edge('Steven',  'Michelle')
G_symmetric.add_edge('Laura',   'Michelle')
G_symmetric.add_edge('Michelle','Marc')
G_symmetric.add_edge('George',  'John')
G_symmetric.add_edge('George',  'Steven')


# In[6]:


print(nx.info(G_symmetric))


# In[7]:


plt.figure(figsize=(5,5))
nx.draw_networkx(G_symmetric);


# In[8]:


G_asymmetric = nx.DiGraph()
G_asymmetric.add_edge('A','B')
G_asymmetric.add_edge('A','D')
G_asymmetric.add_edge('C','A')
G_asymmetric.add_edge('D','E')


# In[9]:


nx.spring_layout(G_asymmetric)
nx.draw_networkx(G_asymmetric)


# In[10]:


G_weighted = nx.Graph()

G_weighted.add_edge('Steven',  'Laura',   weight=25)
G_weighted.add_edge('Steven',  'Marc',    weight=8)
G_weighted.add_edge('Steven',  'John',    weight=11)
G_weighted.add_edge('Steven',  'Michelle',weight=1)
G_weighted.add_edge('Laura',   'Michelle',weight=1)
G_weighted.add_edge('Michelle','Marc',    weight=1)
G_weighted.add_edge('George',  'John',    weight=8)
G_weighted.add_edge('George',  'Steven',  weight=4)


# In[11]:


elarge = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d['weight'] > 8]
esmall = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d['weight'] <= 8]

pos = nx.circular_layout(G_weighted)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G_weighted, pos, node_size=700)

# edges
nx.draw_networkx_edges(G_weighted, pos, edgelist=elarge,width=6)
nx.draw_networkx_edges(G_weighted, pos, edgelist=esmall,width=6, alpha=0.5, edge_color='b', style='dashed')

# labels
nx.draw_networkx_labels(G_weighted, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.show();


# In[12]:


nx.clustering(G_symmetric,'Michelle')


# In[13]:


nx.clustering(G_symmetric,'Laura')


# In[14]:


nx.average_clustering(G_symmetric)


# In[15]:


nx.degree(G_symmetric, 'Michelle')


# In[16]:


nx.shortest_path(G_symmetric, 'Michelle', 'John')


# In[17]:


nx.shortest_path_length(G_symmetric, 'Michelle', 'John')


# In[18]:


S = nx.bfs_tree(G_symmetric, 'Steven')
nx.draw_networkx(S)


# In[19]:


nx.eccentricity(G_symmetric,'Michelle')


# In[20]:


nx.eccentricity(G_symmetric,'Steven')


# In[21]:


nx.degree_centrality(G_symmetric)


# In[22]:


nx.closeness_centrality(G_symmetric)


# In[23]:


nx.betweenness_centrality(G_symmetric)


# In[ ]:




