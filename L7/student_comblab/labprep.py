from functions_comblab import *

# NETWORK demo
network = Network()
network.read_network('simple_network.txt')

# LIST iteration demo
for node in network.nodes:
    for arc in node.arcs_in:
        print(node.name, arc.to_node)

# SET demo 1 - node objects in unvisited set
unvisited_set = set(network.nodes)
unvisited_set.remove(network.get_node('A'))

# SET demo 2 - node names in unvisited set
unvisited_set = set([node.name for node in network.nodes])
unvisited_set.remove('A')