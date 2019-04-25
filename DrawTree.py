import pydot


class DrawTree:
    graph = None

    def __init__(self, tree):
        self.graph = pydot.Dot(graph_type='graph')

        # remember that decision tree can contain different nodes with same label
        # so we assign each node a unique ID: <parent-id>_<node-label>

        # in our dict(tree), keys at odd levels(starting from 0) are edges

        # create root node
        key = next(iter(tree))
        self.graph.add_node(pydot.Node(key, label=key))

        # draw children
        for k, v in tree[key].items():
            self.draw(v, parent_id=key, edge_label=k)

        # after everything's done
        self.graph.write_png('output.png')

    def draw(self, tree, parent_id, edge_label):
        if isinstance(tree, dict):
            key = next(iter(tree))
        else:  # its a leaf
            key = tree

        curr_id = parent_id + '_' + edge_label + '_' + key

        # create a node. add parent edge
        self.graph.add_node(pydot.Node(curr_id, label=key))
        self.graph.add_edge(pydot.Edge(parent_id, curr_id, label=edge_label))

        # check if not a string(leaf)
        if isinstance(tree, dict):
            for k, v in tree[key].items():
                self.draw(v, parent_id=curr_id, edge_label=k)
