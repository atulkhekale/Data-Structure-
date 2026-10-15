
def create_matrix(n):
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)

    return matrix


def add_friendship(matrix, user1, user2):
    matrix[user1][user2] = 1
    matrix[user2][user1] = 1
    print("Friendship added successfully!")


def remove_friendship(matrix, user1, user2):
    matrix[user1][user2] = 0
    matrix[user2][user1] = 0
    print("Friendship removed successfully!")


def check_friendship(matrix, user1, user2):
    if matrix[user1][user2] == 1:
        print("Users are friends.")
    else:
        print("Users are not friends.")


def display_matrix(matrix):
    print("\nAdjacency Matrix:")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()


def display_friends(matrix, user):
    print("Friends of User", user, ":", end=" ")
    found = False

    for i in range(len(matrix)):
        if matrix[user][i] == 1:
            print(i, end=" ")
            found = True

    if not found:
        print("No friends", end="")

    print()


# Main program
n = 5
matrix = create_matrix(n)

add_friendship(matrix, 0, 1)
add_friendship(matrix, 0, 2)
add_friendship(matrix, 1, 3)
add_friendship(matrix, 2, 3)
add_friendship(matrix, 3, 4)

display_matrix(matrix)

display_friends(matrix, 0)
display_friends(matrix, 3)

check_friendship(matrix, 0, 1)
check_friendship(matrix, 0, 4)

remove_friendship(matrix, 0, 1)

check_friendship(matrix, 0, 1)
display_matrix(matrix)
