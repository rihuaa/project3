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
            # line = line.split()
            # for word in line:
            for char in line:
                list_of_freqs[ord(char)] += 1
    return list_of_freqs

def create_huff_tree(list_of_freqs):
    """returns the root node of a Huffman Tree
    """
    hufflist = []
    tree = MinPQ()
    for i in range(len(list_of_freqs)):
        if list_of_freqs[i] != 0:
            new = HuffmanNode(list_of_freqs[i], chr(i))
            tree.insert(new)
            # hufflist.append(new)
    # hufflist.sort()
    # print(hufflist)
    # tree = MinPQ(hufflist)
    # print('TREE AFTER INSERTION:\n', tree)
    while tree.num_items > 1:
        left = tree.del_min()
        right = tree.del_min()
        freq_sum = left.freq + right.freq
        parent = HuffmanNode(freq_sum, min(left.char, right.char))
        # if left.char < right.char:
        #     parent = HuffmanNode(freq_sum, left.char)
        # else: # right.char < left.char:
        #     parent = HuffmanNode(freq_sum, right.char)
        parent.left = left
        parent.right = right
        tree.insert(parent)
    print('dlafjdls;f', tree.arr[0])
    # print('Tree before return: ', tree)
    return tree.arr[0]
    # i = 0
    # while i < len(tree.arr) - 1:
    #     if tree.arr[i + 1] is None:
    #         i += 1
    #         continue
    #     if tree.arr[i + 1] < tree.arr[i]:
    #         tree.arr[i + 1], tree.arr[i] = tree.swap(tree.arr[i + 1], tree.arr[i])
    #     i += 1


    # print('TREE AFTER SORT:\n', tree)


    #
    # # huff_tree = MinPQ(huff_list)
    # for i in range(tree.capacity):
    #     if 2*i + 1 < tree.capacity:
    #         tree.arr[i].left = tree.arr[2*i + 1]
    #     if 2*i + 2 < tree.capacity:
    #         tree.arr[i].right = tree.arr[2*i + 2]
    # tree.heapify()
    # print(tree)

def create_code(root_node):
    """returns a Python list of 256 strings representing the code
    Return an array of size 256 whose idex corresponds to ascii code of a letter.
    """
    code_list = [None] * 256
    return create_code_helper(root_node, code_list, code='')
    # if root_node is None:
    #     return
    # if root_node.left is None and root_node.right is None:
    #     idx = ord(root_node.char)
    #     code_list[idx] = code
    #     return
    # create_code(root_node.left, code + '0')
    # create_code(root_node.right, code + '1')
    # print(code_list)
    # return code_list

def create_code_helper(root_node, code_list, code):
    if root_node is None:
        return
    if root_node.left is None and root_node.right is None:
        idx = ord(root_node.char)
        code_list[idx] = code
        print('char: ', chr(idx), '\tcode: ', code)
        return code_list #go back to root with modded list
    create_code_helper(root_node.left, code_list, code + '0')
    create_code_helper(root_node.right, code_list, code + '1')
    return code_list


def huffman_encode(in_file, out_file):
    """encodes in_file and writes the it to out_file
    This function calls cnt_freq, create_huff_tree, and create_code functions.
    """
    freqlist = cnt_freq(in_file)
    huff_root = create_huff_tree(freqlist)
    print('before calling create code')
    code_list = create_code(huff_root)
    with open(in_file) as text, open(out_file, 'w') as out:
        # uniques = []
        for line in text:
            # print('line', line)
            # line = line.split()
            # for word in line:
                # print('word', word)
            for char in line:
                idx = ord(char)
                # print('char', char)
                # print(idx)
                # print('index', idx)
                s = code_list[idx]
                # print('code', s)
                out.write(s)
                # print('char', char)
                # if char not in uniques:
                #     uniques.append(char)
        # if ' ' in uniques:
        #     uniques.remove(' ')
        # if '\n' in uniques:
        #     uniques.remove('\n')
        # print(uniques)
        # for char in uniques:
        #     idx = ord(char)
        #     # print('index', idx)
        #     s = code_list[idx] * freqlist[idx]
        #     out.write(s)

def huffman_decode(list_of_freqs, encoded_file, decode_file):
    """decode encoded_file and write the decoded text to decode_file.
    This function calls create_huff_tree function.
    It is recommended to write a helper function which traverse the tree and
    find a character mapped to a code or None if the code does not map to any character.
    """
    pass
