"""Huffman Coding
CPE202

Author:
    Put your name here
"""
from huffman import HuffmanNode
from min_pq import MinPQ

def cnt_freq(filename):
    """returns a Python list of 256 integers the frequencies of characters in file
    """
    list_of_freqs = [0] * 256
    with open(filename) as file:
        for line in file:
            line = line.split()
            for word in line:
                for char in word:
                    list_of_freqs[ord(char)] += 1
    return list_of_freqs

def create_huff_tree(list_of_freqs):
    """returns the root node of a Huffman Tree
    """
    tree = MinPQ()
    for i in range(len(list_of_freqs)):
        if list_of_freqs[i] != 0:
            new = HuffmanNode(list_of_freqs[i], chr(i))
            tree.insert(new)

    while tree.num_items > 1:
        left = tree.del_min()
        right = tree.del_min()
        freq_sum = left.freq + right.freq
        if left.char < right.char:
            parent = HuffmanNode(freq_sum, left.char)
        else: # right.char < left.char:
            parent = HuffmanNode(freq_sum, right.char)
        parent.left = left
        parent.right = right
        tree.insert(parent)
    #
    # # huff_tree = MinPQ(huff_list)
    # for i in range(tree.capacity):
    #     if 2*i + 1 < tree.capacity:
    #         tree.arr[i].left = tree.arr[2*i + 1]
    #     if 2*i + 2 < tree.capacity:
    #         tree.arr[i].right = tree.arr[2*i + 2]
    # tree.heapify()
    # print(tree)
    return tree.arr[0]

def create_code(root_node):
    """returns a Python list of 256 strings representing the code
    Return an array of size 256 whose idex corresponds to ascii code of a letter.
    """
    pass

def huffman_encode(in_file, out_file):
    """encodes in_file and writes the it to out_file
    This function calls cnt_freq, create_huff_tree, and create_code functions.
    """
    pass

def huffman_decode(list_of_freqs, encoded_file, decode_file):
    """decode encoded_file and write the decoded text to decode_file.
    This function calls create_huff_tree function.
    It is recommended to write a helper function which traverse the tree and
    find a character mapped to a code or None if the code does not map to any character.
    """
    pass
