# Course: CS261 - Data Structures
# Student Name: Jonathon Stoddart
# Assignment: 4
# Description: Binary Search Tree Implementation


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds a new node of "value" to the tree, maintaining the BST property. Duplicates are placed in the right subtree.
        """
        if self.root is None:  # if empty BST
            self.root = TreeNode(value)

        else:
            parent = None
            cur = self.root
            while cur is not None:  # traverse
                parent = cur
                if value < cur.value:
                    cur = cur.left
                else:
                    cur = cur.right
            # create new node as the child of P        
            if value < parent.value:
                parent.left = TreeNode(value)
            else:
                parent.right = TreeNode(value)

    def contains(self, value: object) -> bool:
        """
        Returns True if the value parameter is in the BinaryTree or False if otherwise.
        """
        cur = self.root
        while cur is not None:
            if cur.value == value:
                return True
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def get_first(self) -> object:
        """
        Returns the value stored at the root node. Returns None if the BinaryTree is empty.
        """
        if self.root is not None:
            return self.root.value

    def remove_first(self) -> bool:
        """
        Removes the root node in the Binary Tree. Returns False if the tree is empty and there is no root node to remove, and True if the root is removed.
        """
        if self.root is None:
            return False
        
         # no children
        if self.root.left is None and self.root.right is None:
            self.root = None
            return True

        elif self.root.right is None:  # no right child
            self.root = self.root.left
            return True
        elif self.root.left is None:  # no left child
            self.root = self.root.right
            return True
        else:
            ios = self.root.right
        ios_parent = self.root
        while ios.left is not None:  # get in order sucessor
            ios_parent = ios
            ios = ios.left
        # give root's children to successor
        if ios is not self.root.left:
            ios.left = self.root.left
        if ios is not self.root.right:
            ios_parent.left = ios.right
            ios.right = self.root.right
        # update root
        self.root = ios

        return True

    def remove(self, value) -> bool:
        """
        Removes the first instance of "value" in the BinaryTree. Returns True if the value is removed, False otherwise.
        """
        cur, cur_parent, cur_direct = self.root, None, None

        while cur is not None and cur.value != value:  # find first instance
            if value < cur.value:
                cur_parent = cur
                cur = cur.left
                cur_direct = 'left'
            else:
                cur_parent = cur
                cur = cur.right
                cur_direct = 'right'
        
        if cur is None:  # did not find value
            return False

        if cur is self.root:  # value in root node
            self.remove_first()
            return True
        
        if cur.left is None and cur.right is None:  # node has no children
            if cur_direct == 'left':
                cur_parent.left = None
            else:
                cur_parent.right = None
        
        elif cur.left is not None and cur.right is not None: # node has two children
            # find node's in-order successor and its parent
            ios, ios_parent = cur.right, cur
            while ios.left is not None:
                ios_parent = ios
                ios = ios.left
            # give node's children to successor
            ios.left = cur.left
            if ios is not cur.right:
                ios_parent.left = ios.right
                ios.right = cur.right
            # update removed node's parent to point to successor
            if cur_direct == 'left':
                cur_parent.left = ios
            else:
                cur_parent.right = ios

        else:  # node has one child
            if cur.left is not None:
                if cur_direct == 'left':
                    cur_parent.left = cur.left
                else:
                    cur_parent.right = cur.left
            else:
                if cur_direct == 'left':
                    cur_parent.left = cur.right
                else:
                    cur_parent.right = cur.right
                    
        return True

    def pre_order_traversal(self) -> Queue:
        """
        Performs pre-order traversal of the tree, returning a Queue object that contains values of visited nodes in the order they were visited.
        If the tree is empty, returns an empty Queue.
        """
        pre_order = Queue()
        return self.rec_pre_order(self.root, pre_order)

    
    def rec_pre_order(self, node, queue):
        """
        Helper method for pre_order_traversal: Adds the value of visited nodes to the provided queue, in the order in which they are visited.
        """
        if node:
            queue.enqueue(node.value)  # enqueue on first pass
            self.rec_pre_order(node.left, queue)  # traverse left subtree
            self.rec_pre_order(node.right, queue)  # traverse right subtree
        
        return queue
        
    def in_order_traversal(self) -> Queue:
        """
        Performs in-order traversal of the tree, returning a Queue object that contains values of the visited nodes in the order they were visited.
        If the tree is empty, returns an empty Queue.
        """
        in_order = Queue()
        return self.rec_in_order(self.root, in_order)

    def rec_in_order(self, node, queue):
        """
        Helper method for in_order_traversal: Adds the value of visited nodes to the provided queue, in the order in which they are visited.
        """
        if node:
            self.rec_in_order(node.left, queue)  # traverse left subtree
            queue.enqueue(node.value)  # enqueue on second pass
            self.rec_in_order(node.right, queue)  # traverse right subtree

        return queue

    def post_order_traversal(self) -> Queue:
        """
        Performs post-order traversal of the tree, returning a Queue object that contains values of the visited nodes in the order they were visited.
        If the tree is empty, returns an empty Queue.
        """
        post_order = Queue()
        return self.rec_post_order(self.root, post_order)

    def rec_post_order(self, node, queue):
        """
        Helper method for post_order_traversal: Adds the value of visited nodes to the provided queue, in the order in which they are visited.
        """
        if node:
            self.rec_post_order(node.left, queue)  # traverse left subtree
            self.rec_post_order(node.right, queue)  # traverse right subtree
            queue.enqueue(node.value)  # enqueue on third pass

        return queue

    def by_level_traversal(self) -> Queue:
        """
        Performs by-level traversal of the tree, returning a Queue object that contains values of the visited nodes in the order they were visited.
        If the tree is empty, returns an empty Queue.
        """
        nodes = Queue()  # to store nodes in a level
        order = Queue()  # to store all values in by level order
        
        nodes.enqueue(self.root)
        while nodes.is_empty() is False:
            node = nodes.dequeue()  # dequeue a node in current level
            if node is not None:
                order.enqueue(node.value)  # store value of dequeued node
                nodes.enqueue(node.left)  # put dequeued node's children in line to be processed
                nodes.enqueue(node.right)

        return order

    def rec_by_level(self, node, queue):
        """
        Helper method for by_level_traversal: Adds the value of visited nodes to the provided queue, in the order in which they are visited.
        """
        queue.enqueue(node.value)
        self.rec_by_level(node.left)
        self.rec_by_level(node.right)
        
    def is_full(self) -> bool:
        """
        Returns True if the tree is a 'full binary tree'. Empty tree or just a single root node is considered full.
        (every node has 0 or 2 children)
        """
        if self.root is None or (self.root.left is None and self.root.right is None):
            return True

        return self.rec_full(self.root)

    def rec_full(self, node):
        """
        Traverses tree, if any interior node does not have exactly two children, returns False. Otherwise returns True.
        """
        if node.left and node.right:
            left_sub = self.rec_full(node.left)
            right_sub = self.rec_full(node.right)
            if left_sub is False or right_sub is False:
                return False

        if (node.left and not node.right) or (node.right and not node.left):
            return False
        
        return True

    def is_complete(self) -> bool:
        """
        Returns True if the tree is a 'complete binary tree'. Empty tree or just a single root node is complete.
        (perfect except for deepest level, where nodes are all as far left as possible)
        """
        # root index initialized to 0
        # left node = (index * 2) + 1
        # right node = (index * 2) + 2
        # if index >= BST size, not a complete tree  - from ed discussion #552
        
        if self.root is None or (self.root.left is None and self.root.right is None):
            return True

        return self.rec_complete(self.root, self.size())

    def rec_complete(self, node, size, index=0):
        """
        Helper method for is_complete - checks if any given index >= size - if so, return False
        """
        if node is None:  # no violations found
            return True

        if index >= size:  # violation found
            return False

        return self.rec_complete(node.left, size, (index*2)+1,) and self.rec_complete(node.right, size, (index*2)+2)   # recurse through left and right subtree

    def is_perfect(self) -> bool:
        """
        returns True if the tree is a 'perfect binary tree'. Empty tree or just a single root node is perfect.
        (full tree where all leaves are of the same depth)
        """
        if self.root is None or self.root.left is None and self.root.right is None:  # base cases of empty or single node
            return True

        height = self.height()
        return self.rec_perfect(self.root, height)

    def rec_perfect(self, node, height, n_depth=0):
        """
        Helper method for is_perfect. Traverses through tree - upon leaf node, if leaf depth is tree's maximum depth,
        returns True. False if not, or if an internal node has 1 child exactly (meaning it is not a full BST)
        """
        if node.left is None and node.right is None:  # leaf node - return True if node depth == tree height, false otherwise
            return n_depth == height

        if node.left is None or node.right is None:  # internal node has one child -not full
            return False

        return self.rec_perfect(node.left, height, n_depth+1) and self.rec_perfect(node.right, height, n_depth+1)  # recurse through left and right subtree - both must return True

    def size(self) -> int:
        """
        Returns the total number of nodes in the tree.
        """
        if self.root is None:
            return 0

        return self.rec_size(self.root)

    def rec_size(self, node, count=0):
        """
        Helper method for size: traverses left, then right subtree while incrementing count upon each node
        """
        if node:
            count += 1
            count = self.rec_size(node.left, count)
            count = self.rec_size(node.right, count)

        return count

    def height(self) -> int:
        """
        Returns the height of the binary tree. An empty tree has a height of -1, just a single root node has a height of 0.
        """
        return self.rec_height(self.root)

    def rec_height(self, node):
        """
        Helper method for height: gets the height of the left and right subtree with root "node", returning the greater height
        """
        if node is None:
            return -1

        left_height = self.rec_height(node.left)
        right_height = self.rec_height(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
    
    def count_leaves(self) -> int:
        """
        Returns the number of nodes in the tree that have no children. If the tree is empty, returns 0.
        """
        if self.root is None:
            return 0
        return self.rec_leaves(self.root)
        
    def rec_leaves(self, node, leaves=0):
        """
        Helper method for count_leaves - traverses through tree and increments "leaves" counter upon receiving a leaf node.
        """
        if node is not None:
            leaves = self.rec_leaves(node.left, leaves)
            leaves = self.rec_leaves(node.right, leaves)
            if node.left is None and node.right is None:
                leaves += 1

        return leaves

    def count_unique(self) -> int:
        """
        Returns the count of uniue values stored in the tree. If all values are distinct, returns the same result as size() (the total number of nodes)
        """
        if self.root is None:
            return 0
        if self.root.left is None and self.root.right is None:
            return 1

        vals = self.in_order_traversal()
        unique = 0
        prev = None
        cur = None

        while vals.is_empty() is False:
            prev = cur
            cur = vals.dequeue()
            if cur != prev:
                unique += 1

        return unique


# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

