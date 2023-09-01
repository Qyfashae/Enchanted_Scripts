words = ["word", "words", "drow", "sdrow", "word"]  # Words in a list
word_counts = (
    {}
)  # Dict_function to count how many times the same word is used in the list

word_counts[
    "newword"
]  # "Normal" way of checking if 'newword' exists in the dictionary as a key or value ### REMOVE THIS ###

for word in words:  # Creating a loop to check for the items in the list
    word_counts[word] = (
        word_counts.get(word, 0) + 1
    )  # If the word is not yet a key, get() returns the default value of 0.

print(word_counts)  # Either way, we then add 1 to the count in the function above

"""
Using get function to check if "newword" is in the dictionary,
if its not in the dictonary it will return the default value of 0.
If it is in the dictionary it will return its current count:
"""

# Can be usefull for loops to avoid errors or trial and error in a safe enviorment.
