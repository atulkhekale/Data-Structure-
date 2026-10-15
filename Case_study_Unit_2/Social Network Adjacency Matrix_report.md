# Case Study: Social Network Adjacency Matrix

## 1. Aim
To represent friendship connections among users in a social network using an adjacency matrix and perform basic friendship operations.

## 2. Introduction
A social network allows users to connect with each other as friends. These connections can be represented using a graph. In a graph, users are called vertices, and friendships are called edges.

An adjacency matrix is a two-dimensional array used to represent connections between users.

- **1** represents a friendship.
- **0** represents no friendship.

Since friendship is mutual, the matrix is symmetric.

## 3. Example
Consider five users with IDs 0, 1, 2, 3, and 4.

The friendships are:
- User 0 is friends with users 1 and 2.
- User 1 is friends with users 0 and 3.
- User 2 is friends with users 0 and 3.
- User 3 is friends with users 1, 2, and 4.
- User 4 is friends with user 3.

The adjacency matrix is:

| User | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 | 0 |
| 2 | 1 | 0 | 0 | 1 | 0 |
| 3 | 0 | 1 | 1 | 0 | 1 |
| 4 | 0 | 0 | 0 | 1 | 0 |

## 4. Operations Performed

1. **Create Matrix:** Creates a matrix initialized with zeros.
2. **Add Friendship:** Adds a connection between two users.
3. **Remove Friendship:** Removes a connection between two users.
4. **Check Friendship:** Checks whether two users are friends.
5. **Display Matrix:** Displays all friendship connections.
6. **Display Friends:** Displays all friends of a particular user.

## 5. Algorithm

1. Start.
2. Create an adjacency matrix of size N × N and initialize it with zeros.
3. Add friendship connections by changing the corresponding matrix entries to 1.
4. Display the adjacency matrix.
5. Check friendship between two users.
6. Remove a friendship when required.
7. Display the updated matrix.
8. Stop.

## 6. Output

```text
Friendship added successfully!
Friendship added successfully!
Friendship added successfully!
Friendship added successfully!
Friendship added successfully!

Adjacency Matrix:
0 1 1 0 0
1 0 0 1 0
1 0 0 1 0
0 1 1 0 1
0 0 0 1 0

Friends of User 0 : 1 2
Friends of User 3 : 1 2 4
Users are friends.
Users are not friends.
Friendship removed successfully!
Users are not friends.
```

The output shows the initial friendship connections, the friends of selected users, and the result of checking and removing a friendship.

## 7. Time and Space Complexity

Let N be the number of users.

| Operation | Complexity |
|---|---|
| Create matrix | O(N²) |
| Add friendship | O(1) |
| Remove friendship | O(1) |
| Check friendship | O(1) |
| Display friends | O(N) |
| Display matrix | O(N²) |
| Space required | O(N²) |

## 8. Advantages

- Easy to understand and implement.
- Checking whether two users are friends takes constant time.
- Suitable for small or dense networks.
- Represents mutual friendship clearly.

## 9. Limitations

- Requires a large amount of memory for many users.
- Most entries may be zero when users have relatively few friends.
- Creating a matrix for millions of users is impractical.

For example, one million users require one trillion matrix entries. Real social networks usually use adjacency lists or other sparse graph representations to reduce memory usage.

## 10. Applications

- Social networking websites.
- Friendship connection analysis.
- Graph-based network analysis.
- Finding direct connections between users.

## 11. Conclusion

An adjacency matrix is a simple way to represent friendship connections in a social network. It supports fast friendship checks and easy connection updates. However, it requires O(N²) space, so adjacency lists are generally more suitable for social networks containing millions of users.