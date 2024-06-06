#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# 加入项目的根目录到 sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structure import make_random_tree, make_tree, BinaryTreePrint, print_tree_list
from data_structure import BinaryTreeVisualizer

def main():
    """TODO: Docstring for main.
    :returns: TODO
    """
    val_list = make_random_tree()
    #val_list = [1, 3, 2, 15, 3, None, 9,8, 432, 82, 432]
    print_tree_list(val_list)
    root = make_tree(val_list)
    bt_printer = BinaryTreePrint()
    bt_printer.print_tree(root)
    BinaryTreeVisualizer().visualizer_tree(root)


if __name__ == "__main__":
    main()
