import networkx as nx
import matplotlib.pyplot as plt
import sys

G = nx.DiGraph()


pontos_file = sys.argv[1]
solucao_file = sys.argv[2]


p = open(pontos_file,'r')
s = open(solucao_file,'r')

pontos = []
n = int(p.readline())
for i in range(n):
    x,y = p.readline().split(' ')
    x = int(x); y = int(y)
    if i == 0:
        G.add_node(i+1,color='red',pos=(x,y))
        _x = x; _y = y
    else:
        G.add_node(i+1,color='blue',pos=(x,y))

# G.add_node(i,color='red',pos=(_x,_y))
for i in range(2): s.readline()
arestas = [int(i)+1 for i in s.readline().replace(' ','').split('->')]

nodes = G.nodes()
print(nodes)
print(arestas)


for i in range(len(arestas) - 1):
    G.add_edge(arestas[i],arestas[i+1], color='blue', weight=1)

print(G.edges())
node_colors = nx.get_node_attributes(G, 'color').values()

#coordenadas
pos = nx.get_node_attributes(G, 'pos')

#ax contém os eixos
fig, ax = plt.subplots()

#desenha o grafo
# nx.draw_networkx_labels(G,pos=pos)
# nx.draw_networkx_edges(G, pos, edge_color='black')
# nx.draw_networkx_nodes(G,pos = pos,node_color = node_colors, ax=ax,node_size=100)
nx.draw(G, node_color = node_colors, with_labels = True, node_size = 100)

#coloca os eixos no plt
ax.tick_params(left=True, bottom=True, labelleft=True,labelbottom=True)
plt.show()