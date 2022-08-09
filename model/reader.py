import re

from .trie import Trie


class Reader:
    """
        A class used to represent the file reader which builds trie.

        Attributes:
            file (str): A file name.
            trie (Trie): A Trie.

        Methods:
            parse(): Parse the file and build a trie.
            get_word_count(word: str): Return the word count in the file.
    """
    def __init__(self, file: str) -> None:
        """
            Attributes:
                file (str): A file name.
                trie (Trie): A Trie.
        """
        self.file = file
        self.trie: Trie = Trie()
        self._parse()

    def _parse(self) -> None:
        """
            Parse the file and build a trie.
        """
        with open(self.file, 'r') as file:
            for line in file:
                words = re.findall(r'\w+', line)
                for word in words:
                    self.trie.put_word(word)
    
    def get_word_count(self, word: str) -> int:
        """
            Return the word count.

            Arguments:
                word (str): A word.

            Returns:
                int: A word count.
        """
        return self.trie.get_word_count(word)