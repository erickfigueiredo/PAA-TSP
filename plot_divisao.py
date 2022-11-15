import networkx as nx
import matplotlib.pyplot as plt
import sys

G = nx.DiGraph()


pontos_file = sys.argv[1]
solucao_file = sys.argv[2]


p = open(pontos_file,'r')
s = open(solucao_file,'r')

dicionario = {}

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

    try:
        dicionario[(x,y)] += 1
    except:
        dicionario[(x,y)] = i+1
        


arestas=[]
#ignora os dados anteriores
for i in range(5): aux = s.readline()

for i in range(n):
    a,b = s.readline().rstrip('\n').split('->')
    a = a.split(','); b = b.split(',')
    a = (int(a[0]),int(a[1]))
    b = (int(b[0]),int(b[1]))

    G.add_edge(dicionario[a],dicionario[b], color='blue', weight=1)



# nodes = G.nodes()
# print(nodes)
# print(arestas)



print(G.edges())
node_colors = nx.get_node_attributes(G, 'color').values()

#coordenadas
pos = nx.circular_layout(G)

#ax contém os eixos
fig, ax = plt.subplots()

# desenha o grafo
# nx.draw_networkx_labels(G,pos=pos)
# nx.draw_networkx_edges(G, pos, edge_color='black')
# nx.draw_networkx_nodes(G,pos = pos,node_color = node_colors, ax=ax,node_size=100)
nx.draw_spring(G, node_color = node_colors, with_labels = True, node_size = 10,arrows = False)

#coloca os eixos no plt
ax.tick_params(left=True, bottom=True, labelleft=True,labelbottom=True)
plt.show()