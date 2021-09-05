import time

class fibonacci:
    def __init__(self, n):
        self.n = n
        self.timeout = time.time() + 10 # 1 minute for each iteration
       

    def __details__(self, n):
        self.__init__(n)
        print("""The nth fib functions have different ways of solving it. \n
        Dynamic programming is the best way of getting fib of n in O(n) time. \n
        The folling are the different ways of solving fib and their complexities.


        """)

    

    def fib_recursive(self, n):
        if n <= 2:
            return 1

        return self.fib_recursive(n - 2) + self.fib_recursive(n - 1)
        
    

n = [4, 5, 6, 10, 1000]
i = 0
while i < len(n):
    num = n[i]
    fib = fibonacci(num)
    print(" -> Calculating {} th fib number Recursively..........".format(num), fib.fib_recursive(num))
    i += 1