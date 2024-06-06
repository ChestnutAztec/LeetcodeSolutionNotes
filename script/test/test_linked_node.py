#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_structure import Node
from data_structure import make_linked_list, print_linked_list, get_tail


val_list = list(range(0, 5))
#val_list = []
print(val_list)
head = make_linked_list(val_list, is_double_linked_list=True)
print(head)
print_linked_list(head)
tail = get_tail(head)
print(tail)
print_linked_list(tail, direction=0)
