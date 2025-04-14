last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# Step 1: Create a list called subjects
subjects = ["physics", "calculus", "poetry", "history"]

# Step 2: Create a list called grades
grades = [98, 97, 85, 88]

# Step 3: Manually create a two-dimensional list combining subjects and grades
gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88]
]

# Step 4: Print gradebook
print("Initial Gradebook:", gradebook)

# Step 5: Add "computer science" with a score of 100
gradebook.append(["computer science", 100])

# Step 6: Add "visual arts" with a score of 93
gradebook.append(["visual arts", 93])

# Step 7: Modify "visual arts" grade to add 5 points
gradebook[-1][1] += 5

# Step 8: Remove numerical grade for "poetry"
for subject in gradebook:
    if subject[0] == "poetry":
        subject.remove(85)

# Step 9: Add "Pass" value for "poetry"
for subject in gradebook:
    if subject[0] == "poetry":
        subject.append("Pass")

# Step 10: Combine last_semester_gradebook with gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = last_semester_gradebook + gradebook

# Print the final gradebook
print("Full Gradebook:", full_gradebook)
