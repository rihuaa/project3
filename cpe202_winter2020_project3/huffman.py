"""HuffmanNode
CPE202

Author:
    Richard Hua
"""
class HuffmanNode:
    """Write docstring for this class
    """
    def __init__(self, frequency, char=None, left=None, right=None):
        self.freq = frequency
        self.char = char
        self.left = left
        self.right = right

    def __eq__(self, other):
        return isinstance(other, HuffmanNode)\
        and (self.freq == other.freq)\
        and (self.char == other.char)\
        and (self.left == other.left)\
        and (self.right == other.right)

    def __repr__(self):
        return 'HuffmanNode(freq=%s, char=%s, left=%s, right=%s)'\
        % (self.freq, self.char, self.left, self.right)

    def __lt__(self, other):
        """Implementing this function let you compare two HuffmanNode objects
         with < in your program
        Args:
            other (HuffmanNode): other HUffmanNode object to be compared with self
        Returns:
            True if self <= other, else return False
        """
        # overloading needed for comparison in minpq
        if self.freq < other.freq:
            return True
        if self.freq == other.freq:
            # return True if ord(self.char) < ord(other.char) else False
            return bool(self.char < other.char)
        return False
