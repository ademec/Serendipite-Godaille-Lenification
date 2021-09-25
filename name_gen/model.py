import json


# the names dataset must only contain lowercase latin letters
def create_model(names):
    # create the matrix of frequencies for every pair of successive characters
    freq_matrix = {' ': {}}
    for name in names:
        prev_char = ' '
        for char in name:
            if char not in freq_matrix[prev_char]:
                freq_matrix[prev_char][char] = 0
            freq_matrix[prev_char][char] += 1
            prev_char = char
            if prev_char not in freq_matrix:
                freq_matrix[prev_char] = {}
        if ' ' not in freq_matrix[prev_char]:
            freq_matrix[prev_char][' '] = 0
        freq_matrix[prev_char][' '] += 1
    
    model = {}
    for prev_char in freq_matrix:
        huffman_nodes = list(freq_matrix[prev_char].items())
        huffman_nodes.sort(key=lambda char_freq_tuple: char_freq_tuple[1])

        while len(huffman_nodes) > 1:
            new_huffman_node = [huffman_nodes.pop(0), huffman_nodes.pop(0)]
            weight = huffman_weight(new_huffman_node)
            idx = binary_search(huffman_nodes, weight, 0, len(huffman_nodes) - 1)
            huffman_nodes.insert(idx, new_huffman_node)
        
        huffman_tree = clean_huffman_leaves(huffman_nodes[0])
        model[prev_char] = huffman_tree
    
    return model


def huffman_weight(huffman_node):
    if type(huffman_node) is tuple:
        return huffman_node[1]
    return huffman_weight(huffman_node[0]) + huffman_weight(huffman_node[1])


def binary_search(huffman_nodes, weight, low, high):
    if low > high:
        return -1
    
    if weight > huffman_weight(huffman_nodes[high]):
        return high + 1
    
    if high - low <= 1:
        return high

    middle = (low + high) // 2
    middle_weight = huffman_weight(huffman_nodes[middle])

    if weight < middle_weight:
        return binary_search(huffman_nodes, weight, low, middle - 1)

    return binary_search(huffman_nodes, weight, middle, high)


def clean_huffman_leaves(huffman_node):
    if type(huffman_node) is tuple:
        return huffman_node[0]
    return [clean_huffman_leaves(huffman_node[0]), clean_huffman_leaves(huffman_node[1])]
