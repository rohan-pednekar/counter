from .node import Node


class Trie:
    """
        A class used to represent the trie.

        Attributes:
            root (Node): A root node.

        Methods:
            put_word(word: str): Add the word in the trie.
            get_word_count(word: str): Return the word count.
    """
    def __init__(self) -> None:
        """
            Attributes:
                root (Node): A root node.
        """
        self.root = Node()

    def put_word(self, word: str) -> None:
        """
            Add the word in the trie.

            Attributes:
                word (str): A word.
        """
        self._put_word_helper(self.root, word)

    def _put_word_helper(self, parent: Node, word: str) -> None:
        """
            A helper method to add the word in the trie.

            Attributes:
                parent (Node): A parent node.
                word (str): A word.
        """
        if len(word) == 0:
            node: Node = parent.get_child()
            if node is None:
                node = Node()
                parent.put_child(node)
            node.increment_count()
        else:
            node: Node = parent.get_child(word[0])
            if node is None:
                node = Node(word[0])
                parent.put_child(node)
            self._put_word_helper(node, word[1:])

    def get_word_count(self, word: str) -> int:
        """
            Return the word count.

            Attributes:
                word (str): A word.

            Returns:
                int: A word count.
        """
        return self._get_word_count_helper(self.root, word)

    def _get_word_count_helper(self, parent: Node, word: str) -> int:
        """
            A helper method to get the word count.

            Attributes:
                parent (Node): A parent node.
                word (str): A word.

            Returns:
                int: A word count.
        """
        if len(word) == 0:
            node: Node = parent.get_child()
            if node is None:
                return 0
            return node.get_count()
        node: Node = parent.get_child(word[0])
        if node is None:
            return 0
        return self._get_word_count_helper(node, word[1:])