# ENGSCI233: Lab - Combinatorics

# imports
from functions_comblab import *

# create network object
network = Network()
network.read_network('waka_voyage_network.txt')

# TODO - your code here in Task 3
travel_time, path = shortest_path(network, 'Taiwan', 'Hokianga')

# iterate across each pair of nodes
# does the source have to be == Taiwan?

x = 5