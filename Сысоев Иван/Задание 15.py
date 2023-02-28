n = int(input())
a = [int(input()) for i in range(n)]
b = [elem for elem in a if elem % 4 == 0 and elem % 7 != 0]
print(len(b))
