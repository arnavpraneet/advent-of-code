def input_per_line(file):
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]

locations = input_per_line("numbers.txt")

left_side = []
right_side = []
for line in locations:
    entries = line.split()
    left_side.append(int(entries[0]))
    right_side.append(int(entries[1]))

print("Initial left side:", left_side[:10])  # First 10 elements
print("Initial right side:", right_side[:10])  # First 10 elements

left_side.sort()
right_side.sort()

print("\nSorted left side:", left_side[:10])
print("Sorted right side:", right_side[:10])

distances = [abs(right_side[number] - left_item) for number, left_item in enumerate(left_side)]

print("\nFirst 10 distances:", distances[:10])
total_distance = sum(distances)
print(f"The total distance between the lists is {total_distance}")

from collections import Counter
right_side_count = Counter(right_side)
similarity_list = [item * right_side_count[item] for item in left_side]
similarity_score = sum(similarity_list)
print(f"The similarity score is {similarity_score}")