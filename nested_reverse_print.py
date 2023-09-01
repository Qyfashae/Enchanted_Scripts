numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Default print:")
print(*numbers)

print("\nPrint with seperator:")
print(*numbers, sep="-")

print("\nPrint with endcharacters:")
print(*numbers, end=" <--- end")

print("\n\nPrint with sep and end:")
print(*numbers, sep="-.-", end=" <-- end")
