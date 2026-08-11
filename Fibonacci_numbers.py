n = 10

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

# Time Complexity: O(n)
# Space Complexity: O(1)
