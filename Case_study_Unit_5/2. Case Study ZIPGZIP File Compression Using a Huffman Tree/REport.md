# ZIP/GZIP File Compression Using a Huffman Tree

## 1. Aim
To implement a simple text compression and decompression program using Huffman coding and a Huffman tree.

## 2. Introduction
File compression reduces the size of data so that it requires less storage space and can be transferred more efficiently.

Huffman coding is a lossless compression technique that assigns binary codes to characters according to their frequencies. Characters that appear frequently generally receive shorter codes, while less frequent characters receive longer codes.

Huffman coding is used as a component of compression methods, including DEFLATE, which is used in ZIP and GZIP formats.

## 3. Huffman Tree
A Huffman tree is a binary tree used to generate codes for characters.

- Each leaf node represents a character.
- Each character has a frequency based on how often it appears.
- The two nodes with the lowest frequencies are repeatedly combined.
- The left branch represents `0`, and the right branch represents `1`.
- The path from the root to a character produces its binary code.

## 4. Algorithm
1. Take the input text.
2. Count the frequency of each character.
3. Create a leaf node for each character.
4. Insert the nodes into a priority queue.
5. Remove the two nodes with the lowest frequencies.
6. Combine them into a new parent node.
7. Repeat until one tree remains.
8. Generate binary codes by traversing the tree.
9. Encode the original text using these codes.
10. Decode the encoded data to recover the original text.

## 5. Sample Output
Original Text: BANANA

Character Frequencies:
- B: 1
- A: 3
- N: 2

Huffman Codes:
- A: 0
- B: 10
- N: 11

Encoded Data: 100110110

Original Size: 48 bits

Compressed Size: 9 bits

Decoded Text: BANANA

## 6. Time and Space Complexity
Let n be the number of characters in the input text and k be the number of distinct characters.

- **Frequency counting:** O(n)
- **Building the Huffman tree:** O(k log k)
- **Generating codes:** O(k)
- **Encoding and decoding:** O(n), assuming the generated codes are treated as bounded-length strings for this basic example.
- **Space complexity:** O(n + k) for the stored text, encoded data, tree, and codes.

## 7. Advantages
- Reduces the number of bits required for suitable input data.
- Uses lossless compression, so the original data can be recovered.
- Assigns shorter codes to more frequent characters.
- Demonstrates an important compression technique.

## 8. Limitations
- This program demonstrates Huffman coding on text; it does not create a valid ZIP or GZIP file.
- The example does not include file headers or other format-specific information.
- Very small inputs may not become smaller after real compression overhead is included.
- The simple program stores the encoded bits as a string, which is less space-efficient than packing them into bytes.

## 9. Applications
- File compression.
- Data transmission.
- Image and multimedia compression systems.
- Archiving utilities.
- Compression algorithms such as DEFLATE, used by ZIP and GZIP.

## 10. Conclusion
This case study demonstrates how Huffman coding uses character frequencies and a binary tree to encode and decode data. Frequent characters receive shorter codes, which can reduce the size of suitable data. Huffman coding is an important component of practical compression systems, although this program is an educational demonstration rather than a complete ZIP/GZIP implementation.