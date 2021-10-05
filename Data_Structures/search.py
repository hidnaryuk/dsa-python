class search:

    def __init__(arr,k):

        array_to_be_searched = arr
        key = k

    def linear(self):        
        for i in range(len(self.array_to_be_searched)):
            if self.array_to_be_searched[i] == self.key:
                return i
        return -1

    def binary(self):
        low = 0
        high = len(self.array_to_be_searched) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array_to_be_searched[mid] == self.key:
                return mid
            elif self.array_to_be_searched[mid] < self.key:
                low = mid + 1
            else:
                high = mid - 1
        return -1

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    k = 10
    s = search(arr,k)
    print(s.linear())
    print(s.binary())                                                   