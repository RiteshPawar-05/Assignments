arr = [10,20,30,40,50]
n = 5
new_arr = [0,0,0,0]

for i in range(1, n):
    new_arr[i-1] = arr[i]

print("Array after insertion:")

for i in range(0, n-1):
    print(new_arr[i], end=" ")

