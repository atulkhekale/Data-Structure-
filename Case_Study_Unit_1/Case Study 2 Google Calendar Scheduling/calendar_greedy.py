
def time_to_minutes(time):
    hour = int(time[0:2])
    minute = int(time[3:5])
    return hour * 60 + minute


def greedy_sort(events):
    n = len(events)

    # Manual sorting by ending time (Bubble Sort)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if time_to_minutes(events[j][2]) > time_to_minutes(events[j + 1][2]):
                temp = events[j]
                events[j] = events[j + 1]
                events[j + 1] = temp


def select_events(events):
    greedy_sort(events)

    selected = []
    last_end = -1

    for event in events:
        start = time_to_minutes(event[1])
        end = time_to_minutes(event[2])

        if start < end and start >= last_end:
            selected.append(event)
            last_end = end

    return selected


events = [
    ["Meeting", "09:00", "10:00"],
    ["Project Review", "09:30", "10:30"],
    ["Study", "10:00", "11:00"],
    ["Lunch", "11:00", "12:00"],
    ["Presentation", "11:30", "12:30"],
    ["Assignment", "12:00", "13:00"]
]

schedule = select_events(events)

print("Selected Calendar Events:")
for event in schedule:
    print(event[0], "-", event[1], "to", event[2])

print("Total events selected:", len(schedule))
