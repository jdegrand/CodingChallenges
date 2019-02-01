"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def main():
    nums = input("Input numbers to include in list (separated by spaces): ").split()
    k = int(input("Input sum to find if two numbers are in list make it: "))
    nums = [int(i) for i in nums]
    temp = set()
    for i in nums:
        if (k - i) in temp:
             print([i, k - i])
             return
        else:
            temp.add(i)
    print("No two numbers found in", nums, "that add up to", k, "...")
            
if __name__ == '__main__':
    main()
