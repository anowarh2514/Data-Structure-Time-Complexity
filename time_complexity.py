# this programs time complexity is n*n or n^2

i=0;j=0;n=0

n = input("Enter n number value: ")
count = 0
for i in range(int(n)):
    for j in range(int(n)):
        count = int(count) + 1

print(n)
print(count)