#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
链表数据结构
is_double_linked_list: False 单向链表; True 双向. Default: False

>>> from data_structure import Node
>>> from data_structure import make_linked_list, print_linked_list, get_tail

>>> val_list = range(0, 5)

>>> # 单向
>>> head = make_linked_list(val_list)
>>> print_linked_list(head)

>>> # 双向
>>> head = make_linked_list(val_list, is_double_linked_list=True)
>>> print_linked_list(head)
>>> tail = get_tail(head)
>>> print_linked_list(tail, direction=0)        # direction=0 时, 作为双向链表向前遍历
"""


class Node(object):
    """docstring for Node"""
    def __init__(self, val='', next=None, prev=None, is_double_linked_list=False):
        self.val = val
        self.next = None
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
    cur.next = Node(val=val, is_double_linked_list=is_double_linked_list)
    if is_double_linked_list:
        cur.next.prev = cur
    cur = cur.next
    return cur


def make_linked_list(val_list, is_double_linked_list=False):
    """TODO: Docstring for make_linked_list.
    构造链表
    :val_list: TODO
    :is_double_linked_list: TODO
    :returns: TODO
    """
    if not val_list:
        return None
    head = Node(is_double_linked_list=is_double_linked_list)
    cur = head
    for val in val_list:
        cur = append_node(cur, val, is_double_linked_list=is_double_linked_list)
    head.next.prev = None
    return head.next


def get_tail(head):
    """TODO: Docstring for get_tail.
    :head: TODO
    :returns: TODO
    """
    if not head:
        return None
    dump_head = Node()
    dump_head.next = head
    cur = dump_head
    while cur.next:
        cur = cur.next
    return cur

def print_linked_list(head, direction=1, detail=False):
    """TODO: Docstring for print_linked_list.
    :head: TODO
    :returns: TODO
    """
    if not head:
        return
    val_list = []
    if direction == 1:
        dump_head = Node()
        dump_head.next = head
        cur = dump_head.next
        while cur:
            if detail:
                print(cur)
            val_list.append(cur.val)
            cur = cur.next
    else:
        dump_head = Node()
        dump_head.prev = head
        cur = dump_head.prev
        while cur:
            if detail:
                print(cur)
            val_list.append(cur.val)
            cur = cur.prev
    print(' -> '.join(f'{item}' for item in val_list))

