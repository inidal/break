class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):

        # If tree is empty
        if self.root is None:
            new_node = Node(value)
            self.root = new_node
            new_node.value = value

        else:
            tmp = self.root # Current node

            # While not found
            while tmp.value != value:

                # If less, then go left
                if value < tmp.value:
                    if tmp.left is None:
                        new_node = Node(value)
                        tmp.left = new_node
                        break
                    else:
                        # Progress left in the tree
                        tmp = tmp.left

                # If bigger, then go right
                elif value > tmp.value:
                    if tmp.right is None:
                        new_node = Node(value)
                        tmp.right = new_node
                        break
                    else:
                        # Progress right in the tree
                        tmp = tmp.right


            # Print message if value inserted already exists in the tree
            if value == tmp.value:
                print(f"Value {value} already exists in the tree.")

    def lookup(self, value):
        tmp = self.root  # Current node

        # Nodes road
        road = []

        # While not found
        while tmp.value != value:
                if value < tmp.value:
                    if tmp.left is None:
                        break
                    else:
                        # Progress left in the tree
                        tmp = tmp.left
                        road.append('left')

                # If bigger, then go right
                elif value > tmp.value:
                    if tmp.right is None:
                        break
                    else:
                        # Progress right in the tree
                        tmp = tmp.right
                        road.append('right')


        # Print message if value inserted already exists in the tree
        if value == tmp.value:
            print(f"Value {value} do exists in the tree.")
            print(f"How to get there? You only need to go {road if len(road) > 0 else 'to the root'}.")
        else:
            print("Sorry, value not found.")


t = BinarySearchTree()

lst = [45, 77, 50, 12, 7, 29, 26, 6, 85]
for i in lst:
    t.insert(i)

t.lookup(85)
