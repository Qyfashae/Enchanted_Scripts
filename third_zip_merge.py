# Example of 'zip' function

users = ["user_one", "user_two", "user_three", "user_four"]
ids = [1, 2, 3, 4]
cookies = ["cookie_one", "cookie_two", "cookie_three", "cookie_four"]

for user, id, cookie in zip(users, ids, cookies):
    print(
        f"{user}: {id}: {cookie}"
    )  # This will output it as a new line for every next step

print(list(zip(users, ids, cookies)))  # for printing the output in a tuple format

# I use the zip function to pair the users, ids and cookies together
