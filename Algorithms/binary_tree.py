class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = node(data)
            else:
                self._insert(data, cur_node.left)
        else:
            if cur_node.right == None:
                cur_node.right = node(data)
            else:
                self._insert(data, cur_node.right)

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(str(cur_node.data))
            self._print_tree(cur_node.right)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height+1)
        right_height = self._height(cur_node.right, cur_height+1)
        return max(left_height, right_height)

    def search(self, data):
        if self.root != None:
            return self._search(data, self.root)
        else:
            return None

    def _search(self, data, cur_node):
        if data == cur_node.data:
            return cur_node
        elif data < cur_node.data and cur_node.left != None:
            return self._search(data, cur_node.left)
        elif data > cur_node.data and cur_node.right != None:
            return self._search(data, cur_node.right)
        else:
            return None
    
    def preorder(self):
        if self.root != None:
            self._preorder(self.root)
        else:
            return None
    
    def _preorder(self, cur_node):
        if cur_node != None:
            print(str(cur_node.data))
            self._preorder(cur_node.left)
            self._preorder(cur_node.right)
        else:
            return None
    
    def postorder(self):
        if self.root != None:
            self._postorder(self.root)
        else:
            return None
    def _postorder(self, cur_node):
        if cur_node != None:
            self._postorder(cur_node.left)
            self._postorder(cur_node.right)
            print(str(cur_node.data))
        else:
            return None
    
    def inorder(self):
        if self.root != None:
            self._inorder(self.root)
        else:
            return None
    def _inorder(self, cur_node):
        if cur_node != None:
            self._inorder(cur_node.left)
            print(str(cur_node.data))
            self._inorder(cur_node.right)
        else:
            return None

if __name__ == 'main':
    my_tree = tree()
    my_tree.insert(10)
    my_tree.insert(5)
    my_tree.insert(15)
    my_tree.insert(3)
    my_tree.insert(7)
    my_tree.insert(13)
    my_tree.insert(17)
    my_tree.print_tree()
    print(my_tree.height())
    print(my_tree.search(17))
    print(my_tree.search(11))
    my_tree.preorder()
    my_tree.postorder()
    my_tree.inorder()