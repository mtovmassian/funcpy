def coroutine(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper

@coroutine
def my_generator():
    x = 0
    fn = lambda x: x + 1
    while True:
        sent = yield x
        if sent and callable(sent):
            fn = sent
        x = fn(x)

gen = my_generator()
for i in range(5): print(next(gen))
print(gen.send(lambda x: x - 1))
for i in range(3): print(next(gen))