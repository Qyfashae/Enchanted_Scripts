user_ids = {}

cookie_id = user_ids.get(
    "13", {}
)  # trying to add an id for 'cookie' for the 'user' 13 with .get()
cookie_id["cookie"] = 9870398402  # just random for the example
print(user_ids)  # prints: {}

request_id = user_ids.setdefault(
    "1", {}
)  # same as above but using 'setdefault()' instead of .get()
request_id["request"] = 1  # same as above
print(user_ids)  # Prints: {'1': {'request': 1}}
