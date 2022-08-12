from typing import Any, Optional


class Node:
    """
        A class used to represent the node.

        Attributes:
            value (Optional[str]): A value.
                (default is None)
            children (dict): Child nodes with key as a value and value as a node.
            count (int): Word count.

        Methods:
            get_value(): Return the value.
            get_child(value: Optional[str] = None): Return the child node.
            put_child(node: Any): Add the child node.
            get_count(): Return the word count.
            increment_count(): Increment the word count.
    """
    def __init__(self, value: Optional[str] = None) -> None:
        """
            Attributes:
                value (Optional[str]): A value.
                    (default is None)
                children (dict): Child nodes with key as a value and value as a node.
                count (int): Word count.
        """
        self.value = value
        self.children = dict()
        self.count = 0
        
    def get_value(self) -> Optional[str]:
        """
            Return the value.

            Returns:
                Optional[str]: A value.
        """
        return self.value

    def get_child(self, value: Optional[str] = None) -> Any:
        """
            Return the child node.

            Returns:
                Any: A child node.
        """
        return self.children.get(value)

    def put_child(self, node: Any) -> None:
        """
            Add the child node.
        """
        self.children[node.get_value()] = node

    def get_count(self) -> int:
        """
            Return the word count.

            Returns:
                int: Word count.
        """
        return self.count

    def increment_count(self) -> None:
        """
            Increment the word count.
        """
        self.count += 1