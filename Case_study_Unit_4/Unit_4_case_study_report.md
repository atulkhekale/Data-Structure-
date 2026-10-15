# Case Study: Dictionary Application Using Hash Tables

## 1. Aim
To implement a dictionary application using a hash table to store words and their meanings, retrieve meanings efficiently, and handle collisions.

## 2. Introduction
A dictionary application stores words and their meanings. Users can add new words, search for meanings, update existing meanings, and delete words.

A hash table is a data structure that stores information using a hash function. The hash function converts a word into an array index, helping the program locate the word quickly.

## 3. Hash Table
A hash table contains an array of slots. Each word is assigned an index using a hash function.

In this program, the hash function adds the character codes of a word and takes the remainder after dividing by the table size.

For example:

`Index = Sum of character codes % Table Size`

The resulting index tells the program where to store or search for the word.

## 4. Collision Resolution
A collision occurs when two different words produce the same hash-table index.

This program uses **Separate Chaining** to resolve collisions. Each array slot can hold a linked list of words that map to the same index.

When a collision occurs, the new word is added to the linked list at that index. The program searches the linked list to find a word or its meaning.

## 5. Operations Performed

1. **Insert:** Adds a new word and its meaning.
2. **Search:** Finds a word and displays its meaning.
3. **Update:** Changes the meaning of an existing word.
4. **Delete:** Removes a word from the dictionary.
5. **Display:** Shows all stored words and meanings.

## 6. Algorithm

1. Start.
2. Create a hash table of a fixed size.
3. Calculate the hash index for the given word.
4. Insert the word and meaning at that index.
5. If another word already occupies the same index, use separate chaining.
6. Search the linked list at the index to find a word.
7. Update or delete the word when required.
8. Display the dictionary contents.
9. Stop.

## 7. Output

The program demonstrates the following results:

- Words and meanings are inserted into the hash table.
- Searching for an existing word displays its meaning.
- Searching for a missing word displays “Word not found!”
- Updating a word changes its stored meaning.
- Deleting a word removes it from the dictionary.
- Displaying the table shows words grouped by hash index.

## 8. Time and Space Complexity

Let n be the number of words and m be the hash-table size.

| Operation | Average Time | Worst-Case Time |
|---|---|---|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Update | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Display all words | O(n + m) | O(n + m) |

The average time is O(1) when words are distributed reasonably evenly. In the worst case, many words may collide at the same index, requiring a linked-list traversal.

**Space Complexity:** O(n + m), because the hash table has m slots and stores n word nodes.

## 9. Advantages

- Fast average searching and insertion.
- Supports adding, updating, and deleting words.
- Separate chaining handles collisions.
- The hash table can store many words.

## 10. Limitations

- Collisions can reduce performance.
- A poor hash function may distribute words unevenly.
- The table size affects performance.
- The program uses a simple hash function and is intended for learning, not a production dictionary.

## 11. Applications

- Dictionary and thesaurus applications.
- Contact lookup systems.
- Symbol tables in compilers.
- Word lookup and indexing.
- Caching and data retrieval systems.

## 12. Conclusion

A hash table provides an efficient way to store and retrieve words and meanings. The program uses a hash function to calculate indexes and separate chaining to handle collisions. It supports insertion, searching, updating, deleting, and displaying dictionary entries. With a good hash function and well-distributed entries, these operations can be performed in constant average time.