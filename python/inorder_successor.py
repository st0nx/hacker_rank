class Node:
    def __init__(self, parent, left, right, val):
        self.parent = parent
        self.left = left
        self.right = right
        self.val = val


def generate_tree(arr):
    root = None
    for i in arr:
        if root is None:
            root = Node(None, None, None, i)
        else:
            add_to_tree(root, Node(None, None, None, i))
    return root
        
def add_to_tree(root, node):
    if root.val > node.val:
        if root.left is None:
            node.parent = root
            root.left = node
        else:
            add_to_tree(root.left, node)
    
    if root.val < node.val:
        if root.right is None:
            node.parent = root
            root.right = node
        else:
            add_to_tree(root.right, node)
            
            
def inorder_sucsessor(node):
    if node.right is not None:
        return find_in_right_subtree(node.right)
    else:
        return find_close_left_in_parent(node)
        
def find_close_left_in_parent(node):
    if node.parent is None:
        return None
    if node.parent.val > node.val:
        return node.parent
    else:
        return find_close_left_in_parent(node.parent)
    
def find_in_right_subtree(node):
    if node.left is not None:
        return find_in_right_subtree(node.left)
    else:
        return node
        
root_tree = generate_tree((4,5,8,5,9,1,2,3,6))
print(root_tree.left.val)
print(inorder_sucsessor(root_tree.left).val)
