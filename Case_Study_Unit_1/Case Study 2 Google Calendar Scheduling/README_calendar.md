# Case Study: Calendar Scheduling Using a Greedy Strategy

## Aim
To create a simple calendar-scheduling example that selects the maximum number of non-overlapping events using a **Greedy** strategy. This demonstrates a scheduling idea that can be used in a calendar application; it is not connected to the real Google Calendar service.

## Strategy Used: Activity Selection
The Greedy strategy chooses the event that finishes earliest, then chooses the next event that starts at or after the previous selected event ends.

### Steps
1. List calendar events with start and end times.
2. Sort the events by end time.
3. Select the first event (the one that ends earliest).
4. Move through the remaining events and select an event if it does not overlap the last selected event.
5. Display the selected schedule.

## Example
The program uses sample events such as:
- Team Meeting — 09:00 to 10:00
- Project Review — 09:30 to 10:30
- Design Discussion — 10:00 to 11:00
- Lunch Break — 11:00 to 12:00
- Study Session — 12:00 to 13:00

The selected events do not overlap. An event ending at 10:00 can be followed by one starting at 10:00.

## How to Run
Requires Python 3.

```bash
python calendar_greedy.py
```

## Time and Space Complexity
- **Time complexity:** O(n log n), because events are sorted by end time; selecting events then takes O(n).
- **Auxiliary space:** O(n) for the sorted list and selected events.
- `n` is the number of calendar events.

## Conclusion
The Greedy activity-selection algorithm creates a schedule with as many non-overlapping events as possible, assuming each event has a fixed start and end time and all events have equal priority.
