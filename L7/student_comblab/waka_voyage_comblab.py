# ENGSCI233: Lab - Combinatorics

# imports
from functions_comblab import *

# create network object
network = Network()
network.read_network('waka_voyage_network.txt')

# TODO - your code here in Task 3
travel_time, path = shortest_path(network, 'Taiwan', 'Hokianga')





highest_time = []

pair_recieved = []
time_v2 = []

# check path pairs with the source being Taiwan always and destination varying -> sort out that list
# one source -> paired with all other destinations -> regardless in path or not ()

for i in network.nodes:
     network_nodes = []
     list_times = []
     for j in network.nodes:
          if i != j: # ignores similar value - i will assemble this into a function # --
               test_time, test_path = shortest_path(network,i.name,j.name)
               if test_time != None:
                    network_nodes.append([i.name,j.name])
                    list_times.append(test_time)
               else:
                    continue # there shortest paths
          else: 
               continue # continue to find non-matching pair
     if network_nodes != [] or list_times != []:
          sorted_corresponding = [x for y, x in sorted(zip(list_times, network_nodes))] # sorting out tuple pair w/ times
          pair_recieved.append(sorted_corresponding[-1]) # takes the last value
          time_review, path_review = shortest_path(network,pair_recieved[-1][0],pair_recieved[-1][-1])
          time_v2.append(time_review) # -> for pair recieved end of j iteration
     else:
          continue

# for overall after final pair added
sorted_corresponding2 = [m for n, m in sorted(zip(time_v2, pair_recieved))]
highest_node_pair = sorted_corresponding2[-1]
time_highest, path_highest = shortest_path(network, highest_node_pair[0],highest_node_pair[-1])

x = path_highest


# finding the greatest travel distance