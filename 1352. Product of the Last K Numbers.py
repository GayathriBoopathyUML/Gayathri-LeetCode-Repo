class ProductOfNumbers:
    def __init__(self):
        self.prefix_prod = [1]  # Start with 1 for easier division

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_prod = [1]  # Reset since 0 invalidates previous products
        else:
            self.prefix_prod.append(self.prefix_prod[-1] * num)  # Append cumulative product

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_prod):  # If k is greater than available numbers, return 0
            return 0
        return self.prefix_prod[-1] // self.prefix_prod[-k-1]  # Efficient division to get product

# import numpy
# class ProductOfNumbers:

#     def __init__(self):
#         self.arr = []

#     def add(self, num: int) -> None:
#         self.arr.append(num)
        

#     def getProduct(self, k: int) -> int:
#         # print(numpy.array(self.arr[-k:]))
#         if k > len(self.arr):
#             return 0
#         # return(int(numpy.array(self.arr[-k:]).prod()))
#         return int(numpy.prod(self.arr[-k:]))
#         # print(self.arr)
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)