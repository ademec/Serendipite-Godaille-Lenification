def reverse_lookup(id_bits, model):
    id_bits = id_bits.copy()
    name = ''
    huffman_node = model[' ']
    i = 0
    
    # while there are bits to convert in the identifier
    while id_bits:
        bit = id_bits[i]
        huffman_node = huffman_node[bit]
        i += 1

        # if we found a Huffman leaf
        # add the character to the name
        # and go to the next character
        # (change the Huffman tree)
        if type(huffman_node) == str:
            char = huffman_node
            name += char
            id_bits = id_bits[i:]
            i = 0
            huffman_node = model[char]

        # if there are not enough bits to find the last Huffman leaf
        # choose the leftmost leaf from the current Huffman node and add it to the name
        elif i >= len(id_bits):
            while type(huffman_node) != str:
                huffman_node = huffman_node[0]
            char = huffman_node
            name += char
            id_bits.clear()
    
    return name
