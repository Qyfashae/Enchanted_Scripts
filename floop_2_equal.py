numbers = [1, 3, 6, 9, 11, 43, 67]
find = 4

for num in numbers:
    if num == find:
        print(f"Found {find} in the list.")
        break
else:
    # This block will execute only uf the loop completed without encountering the 'break' wich it will not duo to number '4' is not in the list
    print(f"{find} was not found in the list.")
