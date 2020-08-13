class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
	if(node):
		return (node.val + ' ' + serialize(node.left) + ' ' + serialize(node.right))
	else:
		return "null"


def deserialize(stringT):
    stringList = stringT.split(' ')

    def decode(value):
        del stringList[0]
        if (value == 'null'):
            return None
        else:
            n = Node(value)
            n.left = decode(stringList[0])
            n.right = decode(stringList[0])
            return n
            
            
    return decode(stringList[0])

node = Node('root', Node('left', Node('left.left')), Node('right'))

assert deserialize(serialize(node)).left.left.val == 'left.left'
