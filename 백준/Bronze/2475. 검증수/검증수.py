li = list(map(int, input().split()))
print(sum(x**2 for x in li) % 10)
