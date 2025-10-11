import heapq

# Creating Huffman tree node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq            # frequency of symbol
        self.symbol = symbol        # symbol name (character)
        self.left = left            # left child
        self.right = right          # right child
        self.huff = ''              # tree direction (0/1)

    def __lt__(self, nxt):
        # Compare nodes based on frequency for heap sorting
        return self.freq < nxt.freq

# Function to print Huffman codes
def print_nodes(node, val=''):
    new_val = val + str(node.huff)
    # Traverse left
    if node.left:
        print_nodes(node.left, new_val)
    # Traverse right
    if node.right:
        print_nodes(node.right, new_val)
    # If leaf node -> print symbol and code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")

# Main function
if __name__ == "__main__":
    n = int(input("Enter number of characters: "))

    chars = []
    freq = []

    print("\nEnter characters and their frequencies:")
    for i in range(n):
        ch = input(f"Character {i+1}: ")
        f = int(input(f"Frequency of '{ch}': "))
        chars.append(ch)
        freq.append(f)

    nodes = []

    # Convert characters and frequencies into Huffman tree nodes
    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freq[i], chars[i]))

    # Combine nodes until only root remains
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    print("\nHuffman Codes:")
    print("----------------")
    print_nodes(nodes[0])