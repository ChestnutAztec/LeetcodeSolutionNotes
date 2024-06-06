#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

import random
import math
from collections import deque
from .binary_tree_visualizer import BinaryTreeVisualizer

class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        """TODO: Docstring for __str__.
        :returns: TODO
        """
        left_val = 'null' if not self.left else self.left.val
        right_val = 'null' if not self.right else self.right.val
        return f'[{left_val} <- {self.val} -> {right_val}]'


class BinaryTreePrint(object):
    """docstring for BinaryTreePrint"""
    def __init__(self):
        pass

    def _fill(self, node, row, left_column, right_column, matrix):
        """TODO: Docstring for _fill.
        :root: TODO
        :returns: TODO
        """
        if not node:
            return
        start = left_column + get_width(node.left)
        node_len = len(f'{node.val}')
        matrix[row][start:start + node_len] = [s for s in f'{node.val}']
        self._fill(node.left, row + 1, left_column, start, matrix)
        self._fill(node.right, row + 1, start + node_len, right_column, matrix)

    def print_tree(self, root):
        """TODO: Docstring for print_tree.
        :root: TODO
        :returns: TODO
        """
        if not root:
            return
        self.height = get_height(root)
        self.width = get_width(root)
        matrix = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        self._fill(root, 0, 0, self.width, matrix)
        for row in matrix:
            print(''.join(row))


def get_height(root):
    """TODO: Docstring for get_height.
    height of a binary tree
    when root is None, height = 0
    :root: TODO
    :returns: TODO
    """
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


def get_width(node):
    """TODO: Docstring for get_width.
    返回当前节点的绘制宽度
    :root: TODO
    :returns: TODO
    """
    if not node:
        return 0
    return get_width(node.left) + get_width(node.right) + len(f'{node.val}')


def make_tree(val_list):
    """TODO: Docstring for make_tree.
    :val_list: TODO
    :returns: TODO
    """
    if not val_list:
        return None
    node_list = []
    for ind, val in enumerate(val_list):
        if val is None:
            node_list.append(None)
        else:
            node = TreeNode(val)
            if ind > 0:
                p_ind = (ind - 1) // 2
                parent = node_list[p_ind]
                if ind % 2 == 1:
                    parent.left = node
                else:
                    parent.right = node
            node_list.append(node)
    return node_list[0]


def make_random_tree(max_node_num=255):
    """TODO: Docstring for make_random_tree.
    max_node_num: 最大节点数
    :returns: TODO
    随机构造一棵树
    """
    max_height = int(math.log2(max_node_num))
    min_val, max_val = 0, 20
    tree_list = []
    while max_node_num:
        if random.randint(0, max_node_num + 10 - len(tree_list)) == 0:
            break
        p_ind = (len(tree_list) - 1) // 2
        node_candidate = random.randint(min_val, max_val)
        if p_ind < 0:
            tree_list.append(node_candidate)
        elif tree_list[p_ind] is None:
            tree_list.append(None)
        else:
            n = len(tree_list) + 1
            h = int(math.log2(n))
            # h 越小, 子节点为空的概率越低
            tree_list.append(random.choice([node_candidate] * (max_height - h) + [None]))
        max_node_num -= 1
    right = len(tree_list) - 1
    while tree_list[right] is None:
        right -= 1
    return tree_list[:right+1]


def print_tree_list(tree_list):
    """TODO: Docstring for print_tree_list.
    :tree_list: TODO
    :returns: TODO
    """
    height = 0
    level_list = []
    for i, val in enumerate(tree_list):
        if i >= 2 ** height - 1:
            level_list.append([])
            height += 1
        level_list[-1].append(val)
    for l in level_list:
        print(l)

