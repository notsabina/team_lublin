import time

#decorator
def measure_time(func):
    def time_wrapper(*args, **kwargs):
        beginning = time.time()
        func(*args, **kwargs)
        ex_time = time.time() - beginning
        print("The execution time is: " + str(ex_time))
    return time_wrapper

#example 1
@measure_time
def hello():
    k = 0
    for i in range(10000):
        k += 1
    print(k)

#example 2
@measure_time
def long_hello(x):
    for i in range(10000):
        x *= i
    print(x)


def main():
    hello()
    long_hello(10)

if __name__ == '__main__':
    main()



