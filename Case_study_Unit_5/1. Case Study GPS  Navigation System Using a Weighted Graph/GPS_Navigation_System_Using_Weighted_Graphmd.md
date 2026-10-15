# GPS / Navigation System Using a Weighted Graph

## 1. Aim
To develop a simple GPS navigation system that represents a city map as a weighted graph and finds the shortest route between two locations.

## 2. Introduction
A GPS navigation system helps people travel from one place to another. In this application, places such as homes, schools, markets, hospitals, and railway stations are represented as vertices (nodes). Roads between these places are represented as edges. The distance of each road is its weight.

The system uses Dijkstra’s algorithm to calculate the shortest route from the starting location to the destination.

## 3. Graph Representation
- **Vertices:** Locations in the city.
- **Edges:** Roads connecting the locations.
- **Weights:** Distances of the roads in kilometres.
- **Algorithm:** Dijkstra’s shortest-path algorithm.

## 4. Algorithm
1. Create a weighted graph of the city.
2. Add locations and roads with their distances.
3. Set the starting location’s distance to zero.
4. Set all other distances to infinity.
5. Select the unvisited location with the smallest known distance.
6. Update the distances of its neighbouring locations.
7. Repeat until the destination is reached or no route is available.
8. Display the shortest route and its total distance.

## 5. Sample Output
Shortest Route: Home → School → Market → Hospital → Station

Total Distance: 8 km

## 6. Time and Space Complexity
- **Time complexity:** O(V² + E) for the basic implementation, where V is the number of locations and E is the number of roads.
- **Space complexity:** O(V + E) for storing the graph and route information.

## 7. Advantages
- Finds a shortest route based on distance.
- Represents real-world roads and locations.
- Can be extended to support more locations and roads.
- Helps users understand how navigation systems select routes.

## 8. Limitations
- The example considers distance only, not traffic or road conditions.
- The basic implementation is less efficient for very large maps.
- Real GPS systems require additional map and location data.

## 9. Applications
- GPS navigation systems.
- Route planning.
- Delivery services.
- Public transport planning.
- Finding routes between buildings or cities.

## 10. Conclusion
This case study demonstrates how a weighted graph can represent a city map and how Dijkstra’s algorithm can find the shortest route between two places. It provides a basic model of how navigation systems plan journeys.