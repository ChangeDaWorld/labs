class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    
    def children(self):
        return self.left, self.right
    
    def __str__(self):
        return self.left, self.right
def huffman_tree(node, binString=''):
    if type(node) is str:
        return {node: binString}
    (l,r) = node.children()
    d=dict()
    d.update(huffman_tree(l, binString + '0'))
    d.update(huffman_tree(r, binString + '1'))
    return d
def make_tree(nodes):
    while len(nodes)>1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = Node(key1,key2)
        nodes.append((node, c1+ c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]

def huffman_encode(string, mapping):
    translation = str.maketrans(mapping)
    translated_string = string.translate(translation)
    return translated_string

def huffman_decode(encoded_data, huffman_codes):
    inverted_codes = {code: char for char, code in huffman_codes.items()}    
    decoded_data = ""
    code = ""
    
    for bit in encoded_data:
        code += bit
        if code in inverted_codes:
            decoded_data += inverted_codes[code]
            code = ""
    
    return decoded_data
if __name__ == '__main__':
    file = open("string.txt",'r')
    string = file.readline()
    file.close
    frq={}
    for c in string:
        if c in frq:
            frq[c]+=1
        else:
            frq[c]=1
    frq=sorted(frq.items(), key=lambda x: x[1], reverse=True)
    node= make_tree(frq)
    encode= huffman_tree(node)
    for (char, frequency) in frq:
        print(char,'=', encode[char])
    coded_string=huffman_encode(string,encode)
    encoded_string=huffman_decode(coded_string, encode)
    print("Закодированная строка -",coded_string,'Декодированная строка', encoded_string)