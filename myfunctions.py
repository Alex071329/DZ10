def simple_separator():
    return '*' * 10
print(simple_separator() == '**********')

def long_separator(count):
    return '*'* count
print(long_separator(3) == '***')
print(long_separator(4) == '****')

def separator(simbol, count):
    return simbol * count
print(separator('-', 10) == '----------')
print(separator('#', 5) == '#####')

def hello_world():
    print('*' * 10)
    print()
    print('Hello World!')
    print()
    print('#' * 10)
hello_world()

def hello_who(who='World'):
    print(separator('*',10))
    print()
    print('Hello',who,'!')
    print()
    print(separator('#',10))
hello_who()
hello_who('Max')
hello_who('Kate')

def pow_many(power, *args):
    result = 0
    for namber in args:
        result += namber
    return result ** power
print(pow_many(1, 1, 2) == 3)
print(pow_many(1, 2, 3) == 5)
print(pow_many(2, 1, 1) == 4)
print(pow_many(3, 2) == 8)
print(pow_many(2, 1, 2, 3, 4) == 100)

def print_key_val(**kwargs):
    for k,v in kwargs.items():
        print(k,'-->',v)

print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)

def my_filter(iterable, function):
    return list(filter(function,iterable))

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])


