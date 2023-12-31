def zero(f = None): return f(0) if f else 0
def one(f = None): return f(1) if f else 1
def two(f = None): return f(2) if f else 2
def three(f = None): return f(3) if f else 3
def four(f = None): return f(4) if f else 4
def five(f = None): return f(5) if f else 5
def six(f = None): return f(6) if f else 6
def seven(f = None): return f(7) if f else 7
def eight(f = None): return f(8) if f else 8
def nine(f = None): return f(9) if f else 9


def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y

# Test Cases

print(seven(times(five()))) # 35
print(four(plus(nine()))) # 13
print(eight(minus(three()))) # 5
