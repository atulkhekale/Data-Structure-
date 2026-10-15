


class Node:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

 
    def hash_function(self, word):
        total = 0
        for char in word:
            total += ord(char)
        return total % self.size


    def insert(self, word, meaning):
        index = self.hash_function(word)
        current = self.table[index]

      
        while current is not None:
            if current.word == word:
                current.meaning = meaning
                print("Meaning updated successfully!")
                return
            current = current.next

        new_node = Node(word, meaning)
        new_node.next = self.table[index]
        self.table[index] = new_node
        print("Word added successfully!")

   
    def search(self, word):
        index = self.hash_function(word)
        current = self.table[index]

        while current is not None:
            if current.word == word:
                print(word, ":", current.meaning)
                return
            current = current.next

        print("Word not found!")

   
    def delete(self, word):
        index = self.hash_function(word)
        current = self.table[index]
        previous = None

        while current is not None:
            if current.word == word:
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next

                print("Word deleted successfully!")
                return

            previous = current
            current = current.next

        print("Word not found!")

    
    def display(self):
        print("\nDictionary Contents:")

        for i in range(self.size):
            current = self.table[i]

            if current is not None:
                print("Index", i, ":", end=" ")
                while current is not None:
                    print(current.word, "-", current.meaning, end=" -> ")
                    current = current.next
                print("NULL")


# Main program
dictionary = HashTable(10)

dictionary.insert("apple", "A fruit")
dictionary.insert("book", "A collection of pages")
dictionary.insert("cat", "A small domesticated animal")
dictionary.insert("dog", "A domesticated animal")


dictionary.insert("act", "To do something")

dictionary.display()

print("\nSearching words:")
dictionary.search("apple")
dictionary.search("dog")
dictionary.search("computer")

print("\nUpdating a meaning:")
dictionary.insert("apple", "A sweet edible fruit")
dictionary.search("apple")

print("\nDeleting a word:")
dictionary.delete("cat")
dictionary.search("cat")

dictionary.display()
