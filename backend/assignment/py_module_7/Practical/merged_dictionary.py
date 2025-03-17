# Creating two lists
keys = ["name", "age", "city", "study"]
values = ["rakib", 30, "ahmedabad", "Engineer"]

# Merging the two lists into a dictionary using a loop
merged_dict = {}

for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

# Printing the merged dictionary
print("Merged Dictionary:", merged_dict)

