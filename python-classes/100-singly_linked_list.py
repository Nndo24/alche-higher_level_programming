#!/usr/bin/python3
"""Defines classes for a singly-linked list."""


class Node:
    """Represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the Node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the Node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Define the print representation of a SinglyLinkedList."""
        values = []
        curr = self.__head
        while curr is not None:
            values.append(str(curr.data))
            curr = curr.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList in sorted order.

        Args:
            value (int): The value of the new Node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return

        if self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        curr = self.__head
        while curr.next_node is not None and curr.next_node.data < value:
            curr = curr.next_node

        new_node.next_node = curr.next_node
        curr.next_node = new_node
