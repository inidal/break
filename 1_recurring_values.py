# Most Recurring Value

# Input of arrays to test
arrays = [
    [2,5,1,2,3,5,1,2,4],
    [3,1,1,2,1,5,2,1,4],
    [2,3,4,5]
]

class ReturnRecurrent:

    # Initial values
    def __init__(self):
        self.higher = 0
        self.tmp = {}

    # Returning the highest recurring value
    def getHigher(self, arr):
        for i in arr:
            if i > self.higher:
                self.higher = i
        return self.higher

    # Counting repeated values
    def countRecurr(self, arr):
        for i in arr:
            if self.tmp.get(i) is None:
                self.tmp[i] = 1
            else:
                self.tmp[i] = self.tmp.get(i) + 1

    # Return the result
    def result(self, arr):
        self.countRecurr(arr)

        # Get highest value and its index
        higher_val = self.getHigher(self.tmp.values())
        higher_index = list(self.tmp.values()).index(higher_val)
        higher_num = list(self.tmp.keys())[higher_index]

        # Filter if more than one recurring value
        if higher_val > 1:
            print(f"The most repeated number is {higher_num} with {higher_val} recurrence.")
        else:
            print("No recurring number!")

        # Reset initial values
        self.higher = 0
        self.tmp = {}

# Initiate class
reccur = ReturnRecurrent()

# Loop through arrays
for i in arrays:
    print(i)
    reccur.result(i)
    print()


# ===========================
# ========= OUTPUT ==========
# ===========================

# [2, 5, 1, 2, 3, 5, 1, 2, 4]
# The most repeated number is 2 with 3 recurrence.
#
# [3, 1, 1, 2, 1, 5, 2, 1, 4]
# The most repeated number is 1 with 4 recurrence.
#
# [2, 3, 4, 5]
# No recurring number!

# ===========================
