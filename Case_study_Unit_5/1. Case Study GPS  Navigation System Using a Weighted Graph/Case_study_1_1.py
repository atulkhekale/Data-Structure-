
class Graph:
    def __init__(self):
        self.graph = {}

    def add_road(self, place1, place2, distance):
        if place1 not in self.graph:
            self.graph[place1] = []
        if place2 not in self.graph:
            self.graph[place2] = []

        self.graph[place1].append((place2, distance))
        self.graph[place2].append((place1, distance))

    def shortest_path(self, start, end):
        distances = {}
        previous = {}
        unvisited = list(self.graph)

        for place in self.graph:
            distances[place] = float("inf")

        distances[start] = 0

        while unvisited:
            current = min(
                unvisited,
                key=lambda place: distances[place]
            )

            if distances[current] == float("inf"):
                break

            unvisited.remove(current)

            if current == end:
                break

            for neighbor, distance in self.graph[current]:
                new_distance = distances[current] + distance

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current

        if distances[end] == float("inf"):
            print("No route found!")
            return

        path = []
        current = end

        while current != start:
            path.append(current)
            current = previous[current]

        path.append(start)
        path.reverse()

        print("Shortest Route:", " -> ".join(path))
        print("Total Distance:", distances[end], "km")


city = Graph()

city.add_road("Home", "Market", 4)
city.add_road("Home", "School", 2)
city.add_road("School", "Market", 1)
city.add_road("School", "Hospital", 7)
city.add_road("Market", "Hospital", 3)
city.add_road("Market", "Station", 5)
city.add_road("Hospital", "Station", 2)

city.shortest_path("Home", "Station")
