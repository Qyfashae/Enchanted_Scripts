events = ["x", "y", "z", "a", "b", "c", "i", "q"]  # list

last_event = events[-1]  # negative indexing
print("Last event is:", last_event)  # will print the "q"

all_except_last_event = events[:-1]  # inhibitation indexing
print(
    "All except last event is:", all_except_last_event
)  # will print all except the "q"

reversed_event = events[::-1]  # reversed indexing
print(
    "Events in reverse order:", reversed_event
)  # will print everything in reversed from 'q' to 'x'
