#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data_structure.linked_list import Node
from data_structure.linked_list import make_linked_list, print_linked_list

val_list = range(0, 5)
head, tail = make_linked_list(val_list, is_double_linked_list=True)
print_linked_list(head)
print_linked_list(tail, direction=0)
print(head)
print(tail)
