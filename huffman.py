from collections import Counter
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

if __name__ == '__main__':
    file = open("spring.txt",'r')
    string = file.readline()
    file.close
    frq=dict(Counter(string))
    frq=sorted(frq.items(), key=lambda x: x[1], reverse=True)
    node= make_tree(frq)
    encode= huffman_tree(node)
    for i in encode:
        print(f'{i} : {encode[i]}')