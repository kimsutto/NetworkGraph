# networkx matplotlib.pyplot 사용 
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt


graph = nx.Graph()
graph.add_nodes_from((1,2,3,4,5))


nx.draw(graph)
plt.show()

#그래프를 이미지로 저장 
#plt.savefig("graph.png")
