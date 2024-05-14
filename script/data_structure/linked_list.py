#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
链表数据结构
is_double_linked_list: False 单向链表; True 双向. Default: False

>>> from data_structure.linked_list import Node
>>> from data_structure.linked_list import make_linked_list, print_linked_list

>>> val_list = range(0, 5)

>>> # 单向
>>> head, _ = make_linked_list(val)
>>> print_linked_list(head)

>>> # 双向
>>> head, tail = make_linked_list(val, is_double_linked_list=True)
>>> print_linked_list(head)
>>> print_linked_list(tail)
"""


class Node(object):
    """docstring for Node"""
    def __init__(self, val='', is_head_tail=0, is_double_linked_list=False):
        self.is_head_tail = is_head_tail
        self.val = val
        self.next = None
        if is_double_linked_list:
            self.prev = None

    def __str__(self):
        """TODO: Docstring for __str__.
        :returns: TODO
        """
        pre_val = None if self.prev is None else self.prev.val
        nxt_val = None if self.next is None else self.next.val
        result = f'cur[{self.val}] prev[{pre_val}] next[{nxt_val}]'
        return result


def append_node(cur, val='', is_head_tail=0, is_double_linked_list=False):
    """TODO: Docstring for append_node.
    :cur: TODO
    :val: TODO
    :returns: TODO
    """
    new_node = Node(val=val, is_head_tail=is_head_tail, is_double_linked_list=is_double_linked_list)
    cur.next = new_node
    if is_double_linked_list:
        new_node.prev = cur
    cur = cur.next
    return cur


def make_linked_list(val_list, is_double_linked_list=False):
    """TODO: Docstring for make_linked_list.
    构造链表
    :val_list: TODO
    :is_double_linked_list: TODO
    :returns: TODO
    """
    head = Node(is_head_tail=1,  is_double_linked_list=is_double_linked_list)
    tail = None
    cur = head
    for val in val_list:
        cur = append_node(cur, val, is_double_linked_list=is_double_linked_list)
    if is_double_linked_list:
        tail = append_node(cur, val='', is_head_tail=2, is_double_linked_list=is_double_linked_list)
    return head, tail


def print_linked_list(start, direction=1):
    """TODO: Docstring for print_linked_list.
    :head: TODO
    :returns: TODO
    """
    cur = start.next if direction == 1 else start.prev
    val_list = []
    while cur and cur.is_head_tail == 0:
        val_list.append(cur.val)
        cur = cur.next if direction  == 1 else cur.prev
    print(' -> '.join(f'{item}' for item in val_list))


def test():
    """TODO: Docstring for test.
    :returns: TODO
    """
    val_list = range(0, 5)
    print(val_list)
    head, tail = make_linked_list(val_list, is_double_linked_list=True)
    print_linked_list(head)
    print_linked_list(tail, direction=0)


if __name__ == "__main__":
    test()
