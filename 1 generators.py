# 1 generators
# fun to return list of squares of num

# normal method
def square_num(num):
    square = []
    for i in range(1, num+1):
        square.append(i*i)
    return square


s = square_num(10)
print(s)

# using generators


def sqnum_gen(n):
    s = []
    for i in range(1, n+1):
        yield i*i


print(sqnum_gen(10))  # returns the objects
squares = square_num(10)
for i in squares:
    print(i)
