import numpy as np

# Step 1: Create marks array
marks = np.array([50, 60, 70, 80, 90])

# Step 2: Print marks
print("Marks:", marks)

# Step 3: Total
print("Total:", marks.sum())

# Step 4: Average
print("Average:", marks.mean())

# Step 5: Highest & Lowest
print("Highest:", marks.max())
print("Lowest:", marks.min())


bonus_marks = marks + 5
print("After Bonus:", bonus_marks)