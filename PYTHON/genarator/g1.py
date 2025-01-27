def ganarator(n):
    for i in range(n):
        yield i;

values=ganarator(10);

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))