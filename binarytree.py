class Node:
    def __init__(self, value):
        self.value = value  
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left 
        return current_node

    def max_value_node(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node


if __name__ == '__main__':
    # Create BST
    bst = BST()
    
    # Insert nodes
    bst.insert(10) 
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)

    # Check contains 
    print(bst.contains(15)) # True
    
    # Get min and max
    min = bst.min_value_node(bst.root)
    print(min.value) # 3
    
    max = bst.max_value_node(bst.root) 
    print(max.value) # 15
