# ENGSCI233: Lab - Combinatorics

# imports
from functions_comblab import *

# create network object
network = Network()
network.read_network('waka_voyage_network.txt')

# TODO - your code here in Task 3
travel_time, path = shortest_path(network, 'Taiwan', 'Hokianga')
network_nodes = []
list_times = []

# check path pairs with the source being Taiwan always and destination varying -> sort out that list
# one source -> paired with all other destinations -> regardless in path or not ()
for i in network.nodes:
     for j in network_nodes:
          if i != j:
               network_nodes.append((i,j))
               list_times.append(shortest_path(network,i.name,j.name))
          else:
               continue
          
sorted_corresponding = [x for y, x in sorted(zip(node_distance, revision_list))]
node_recieved = network.get_node(sorted_corresponding[0])

# finding the greatest travle distance