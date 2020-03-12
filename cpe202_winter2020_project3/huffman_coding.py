"""Huffman Coding
CPE202

Author:
    Richard Hua
"""
from huffman import HuffmanNode
from min_pq import MinPQ

def cnt_freq(filename):
    """returns a Python list of 256 integers the frequencies of characters in file
    """
    list_of_freqs = [0] * 256
    with open(filename) as file:
        for line in file:
            for char in line:
                list_of_freqs[ord(char)] += 1
    return list_of_freqs

def create_huff_tree(list_of_freqs):
    """returns the root node of a Huffman Tree
    """
    tree = MinPQ()
    for idx, freq in enumerate(list_of_freqs):
        if freq != 0:
            new = HuffmanNode(freq, chr(idx))
            tree.insert(new)
    while tree.num_items > 1:
        left = tree.del_min()
        right = tree.del_min()
        freq_sum = left.freq + right.freq
        parent = HuffmanNode(freq_sum, min(left.char, right.char))
        parent.left = left
        parent.right = right
        tree.insert(parent)
    return tree.arr[0]

def create_code(root_node):
    """returns a Python list of 256 strings representing the code
    Return an array of size 256 whose idex corresponds to ascii code of a letter.
    """
    code_list = [None] * 256
    return create_code_helper(root_node, code_list, code='')

def create_code_helper(root_node, code_list, code):
    """helps traverse a huffman tree to create the huffman code for each
    character at the leaf node.
    Return an array of size 256 whose idex corresponds to ascii code of a letter.
    """
    if root_node is None:
        return None
    if root_node.left is None and root_node.right is None:
        idx = ord(root_node.char)
        code_list[idx] = code
        # print('char: ', chr(idx), '\tcode: ', code)
    create_code_helper(root_node.left, code_list, code + '0')
    create_code_helper(root_node.right, code_list, code + '1')
    return code_list


def huffman_encode(in_file, out_file):
    """encodes in_file and writes the it to out_file
    This function calls cnt_freq, create_huff_tree, and create_code functions.
    """
    freqlist = cnt_freq(in_file)
    huff_root = create_huff_tree(freqlist)
    code_list = create_code(huff_root)
    with open(in_file) as text, open(out_file, 'w') as out:
        for line in text:
            for char in line:
                idx = ord(char)
                code = code_list[idx]
                out.write(code)

def huffman_decode(list_of_freqs, encoded_file, decode_file):
    """decode encoded_file and write the decoded text to decode_file.
    This function calls create_huff_tree function.
    It is recommended to write a helper function which traverse the tree and
    find a character mapped to a code or None if the code does not map to any character.

    Args:
        list_of_freqs (list) : frequency occurence of characters list

    Reads:
        encoded_file (file) : Huffman encoded txt file in 0's and 1's

    Writes:
        decode_file (file) : Decoded encoded_file output. Text file
        of Huffman code as characters.
    """
    hufftree = create_huff_tree(list_of_freqs)
    with open(encoded_file) as in_file, open(decode_file, 'w') as out_file:
        for line in in_file:
            while line:
                huffchar, line = decode_traverser(hufftree, line)
                out_file.write(huffchar)

def decode_traverser(hufftree, line):
    """Traverses hufftree according to an encoded text file. Finds
    a character mapped to a Huffman code or None if mapping is invalid.

    Args:
        hufftree (HuffmanNode) : Node to traverse from

    Returns:
        chr : If mapping for Huffman code exists, None otherwise.
    """
    # 1) We start from root and do following until a leaf is found.
    # 2) If current bit is 0, we move to left node of the tree.
    # 3) If the bit is 1, we move to right node of the tree.
    # 4) If during traversal, we encounter a leaf node,
    # we print character of that particular leaf node
    # and then again continue the iteration of the encoded data
    # starting from step 1.
    if hufftree is None:
        return None
    if hufftree.left is None and hufftree.right is None:
        return hufftree.char, line
    if line[0] == '0':
        return decode_traverser(hufftree.left, line[1:])
    if line[0] == '1':
        return decode_traverser(hufftree.right, line[1:])
    return None
