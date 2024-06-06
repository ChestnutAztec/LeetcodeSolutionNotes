#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from data_structure import Node
from data_structure import make_linked_list, print_linked_list, get_tail


class ReverseLinkedList(object):
    """docstring for ReverseLinkedList"""
    def __init__(self):
        pass

    def reverse_linked_list_get_tail(self, head):
        """TODO: Docstring for reverse_linked_list_get_tail.
        :head: TODO
        :returns: TODO
        """
        if not head:
            dump_head = Node()
            return dump_head, dump_head
        new_head, tail = self.reverse_linked_list_get_tail(head.next)
        tail.next = head
        head.next = None
        tail = tail.next
        return new_head, tail

    def reverse_linked_list(self, head):
        """TODO: Docstring for reverse_linked_list.
        反转链表
        :head: TODO
        :returns: TODO
        """
        if not head:
            return head
        new_head, tail = self.reverse_linked_list_get_tail(head)
        return_head = new_head.next

        # 删除 dummy_head
        new_head.next = None
        del new_head

        return return_head

    def reverse_double_linked_list_get_tail(self, head):
        """TODO: Docstring for reverse_double_linked_list_get_tail.
        反转双向链表, 返回 head 和 tail
        :head: TODO
        :returns: TODO
        """
        if not head:
            dump_head = Node(val='dummy')
            return dump_head, dump_head
        new_head, tail = self.reverse_double_linked_list_get_tail(head.next)
        tail.next = head
        head.next = None
        head.prev = tail
        tail = tail.next
        return new_head, tail

    def reverse_double_linked_list(self, head):
        """TODO: Docstring for reverse_double_linked_list.
        反转双向链表
        :returns: TODO
        """
        if not head:
            return head
        new_head, tail = self.reverse_double_linked_list_get_tail(head)
        new_head.next.prev = None       # new head 的 prev 要置为 None

        # 删除 dummy_head
        return_head = new_head.next
        new_head.next= None
        del new_head

        return return_head

    def reverse_by_k(self, head, k):
        """TODO: Docstring for reverse_by_k.
        :head: TODO
        :k: TODO
        :returns: TODO
        """
        if not head:
            return None
        if k == 1:
            return head
        dummy_head = Node()
        dummy_head.next = head
        p = dummy_head
        q = dummy_head
        for i in range(0, k):
            if q.next:
                q = q.next
        tmp_head = q.next
        q.next = None
        new_head = self.reverse_linked_list(p.next)

        tmp_head = self.reverse_by_k(tmp_head, k)
        p = new_head
        while p.next:
            p = p.next
        p.next = tmp_head
        return new_head

    def find_middle_node(self, head):
        """TODO: Docstring for find_middle_node.
        :head: TODO
        :returns: TODO
        """
        if not head:
            return None
        dummy_head = Node()
        dummy_head.next = head
        p = dummy_head
        q = dummy_head
        #while p.next and q.next.next:
        while q and q.next:
            p = p.next
            q = q.next
            if q.next:
                q = q.next
        return p


def main():
    """TODO: Docstring for main.
    :returns: TODO
    """
    ## 单向
    #print('single linked list:')
    #head = make_linked_list(range(0, 5))
    #print_linked_list(head)
    #new_head = ReverseLinkedList().reverse_linked_list(head)
    #print_linked_list(new_head)

    ## 双向
    #print()
    #print('double linked list:')
    #head = make_linked_list(range(0, 5), is_double_linked_list=True)
    ##head = make_linked_list([], is_double_linked_list=True)
    #print_linked_list(head)
    #new_head = ReverseLinkedList().reverse_double_linked_list(head)
    #print_linked_list(new_head, detail=True)

    # reverse by K
    n = random.randint(0, 13)
    #n = 1
    k = 3
    head = make_linked_list(range(0, n))
    print_linked_list(head)
    new_head = ReverseLinkedList().reverse_by_k(head, k)
    print_linked_list(new_head)

    # 中点
    ##n = random.randint(5, 13)
    #for n in range(0, 11):
        #val_list = list(range(0, n))
        #head = make_linked_list(val_list)
        #print_linked_list(head)
        #middle = ReverseLinkedList().find_middle_node(head)
        #print(n)
        #assert(middle is None and n == 0 or n > 0 and middle.val == val_list[(len(val_list) - 1)//2])


if __name__ == "__main__":
    main()

