#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graphviz import Digraph


class BinaryTreeVisualizer(object):
    """docstring for BinaryTreeVisualizer"""
    def __init__(self):
        pass

    def _add_nodes_edges(self, node):
        """TODO: Docstring for _add_nodes_edges.
        :node: TODO
        :returns: TODO
        """
        if not node:
            return
        self.graph.node(str(id(node)), f'{node.val}')
        if node.left:
            self.graph.node(str(id(node.left)), f'{node.left.val}')
            self.graph.edge(str(id(node)), str(id(node.left)))
            self._add_nodes_edges(node.left)
        if node.right:
            self.graph.node(str(id(node.right)), f'{node.right.val}')
            self.graph.edge(str(id(node)), str(id(node.right)))
            self._add_nodes_edges(node.right)

    def visualizer_tree(self, root):
        """TODO: Docstring for visualizer_tree.
        :root: TODO
        :returns: TODO
        """
        if not root:
            return
        self.id = 0
        self.graph = Digraph(comment="Binary Tree", node_attr={'shape': 'circle'})
        self._add_nodes_edges(root)
        self.graph.format = 'png'
        file_name = './binary_tree'
        self.graph.render(file_name, view=True)
