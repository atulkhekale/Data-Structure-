
import heapq
from collections import Counter

class Node:
    def __init__(self, char=None, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right

def build_huffman_tree(text):
    frequencies = Counter(text)
    heap = []
    order = 0

    for char, frequency in frequencies.items():
        node = Node(char)
        heapq.heappush(heap, (frequency, order, node))
        order += 1

    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)

        parent = Node(None, left, right)
        heapq.heappush(heap, (freq1 + freq2, order, parent))
        order += 1

    return heap[0][2], frequencies

def generate_codes(node, code, codes):
    if node.char is not None:
        codes[node.char] = code if code else "0"
        return

    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)

def encode_text(text, codes):
    encoded = ""

    for char in text:
        encoded += codes[char]

    return encoded

def decode_text(encoded, root):
    decoded = ""
    current = root

    if root.char is not None:
        return root.char * len(encoded)

    for bit in encoded:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded += current.char
            current = root

    return decoded

text = "BANANA"

root, frequencies = build_huffman_tree(text)
codes = {}
generate_codes(root, "", codes)

encoded = encode_text(text, codes)
decoded = decode_text(encoded, root)

print("Original Text:", text)
print("Character Frequencies:")

for char, frequency in frequencies.items():
    print(char, ":", frequency)

print("Huffman Codes:")

for char, code in codes.items():
    print(char, ":", code)

print("Encoded Data:", encoded)
print("Original Size:", len(text) * 8, "bits")
print("Compressed Size:", len(encoded), "bits")
print("Decoded Text:", decoded)
