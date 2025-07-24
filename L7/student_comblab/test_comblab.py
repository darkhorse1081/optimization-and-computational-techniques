# ENGSCI233: Lab - Combinatorics

# imports
from functions_comblab import *


def test_search_value_negative_three():
    # create the tree object and assign values
    tree = Tree()
    tree.build(tree_tuple=('A', (('B', (('D', None), ('E', None), ('F', None))), ('C', (('G', None), ('H', None))))))
    tree.assign_values(val_dict={'A': 2, 'B': -1, 'D': 3, 'E': 0, 'F': -2, 'C': 1, 'G': -3, 'H': 4})

    # call your search algorithm for search_value of -3
    # node_name = search(tree=tree, search_value=-3)
    node_name1 = search(tree=tree, search_value=2)
    node_name2 = search(tree=tree, search_value=-1)
    node_name3 = search(tree=tree, search_value=1)
    node_name4 = search(tree=tree, search_value=3)
    node_name5 = search(tree=tree, search_value=0)
    node_name6 = search(tree=tree, search_value=-2)
    node_name7 = search(tree=tree, search_value=-3)
    node_name8 = search(tree=tree, search_value=4)
    node_name9 = search(tree=tree, search_value=5)


    node_list = []
    if node_name9 is not None:
        node_list.append(node_name9)
        tree.show(node_list)
    else:
        tree.show()

def test_shortest_path_simple_A_to_F():
    # create network object
    network = Network()
    network.read_network('simple_network.txt')

    # run the shortest path algorithm
    distance, path = shortest_path(network, 'F', 'A')

    # TODO - include your appropriate test in Task 2
    if ( distance is not None and path is not None ): # path should return list of arcs from source to target
        print("Shortest Distance from A to F...{}".format(distance))
        print("Shortest Path from A to F ... {}".format(path))
    else:
        print(network.arcs)
        print(network.nodes)
        print("Shortest path not found")



# test_search_value_negative_three()
test_shortest_path_simple_A_to_F()