n = 5
marks = [0,0,0,0,0]

marks[0] = int(input("Enter the marks of java:"))
marks[1] = int(input("Enter the marks of python:"))
marks[2] = int(input("Enter the marks of c:"))
marks[3] = int(input("Enter the marks of javascript:"))
marks[4] = int(input("Enter the marks of go:"))

n = 5

sum = 0
for i in range(0, n):
    print(marks[i], end=" ")
    sum += marks[i]

avg = sum/n
print(avg)

if avg > 75:
    print(f"Distinction {avg}")
elif avg > 65 and avg < 75:
    print(f"A {avg}")
elif avg > 55 and avg < 65:
    print(f"B {avg}")
elif avg > 45 and avg < 35:
    print(f"C {avg}")
elif avg < 35:
    print(f"Tumse na ho payega")

for i in range(0, n):
    if i == 0 and marks[i] <= 35:
        print(f"Failed in java {marks[i]}")
    elif i == 1 and marks[i] <= 35:
        print(f"Failed in python {marks[i]}")
    elif i == 2 and marks[i] <= 35:
            print(f"Failed in c {marks[i]}")
    elif i == 3 and marks[i] <= 35:
            print(f"Failed in javascript {marks[i]}")
    elif i == 4 and marks[i] <= 35:
            print(f"Failed in go {marks[i]}")


