class sort:
    def __init__(self, list):
        self.list = list
        self.length = len(list)
    
    def bubble_sort(self):
        for i in range(self.length):
            for j in range(self.length-1):
                if self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
        return self.list
    
    def selection_sort(self):
        for i in range(self.length):
            min_index = i
            for j in range(i+1, self.length):
                if self.list[j] < self.list[min_index]:
                    min_index = j
            self.list[i], self.list[min_index] = self.list[min_index], self.list[i]
        return self.list
    
    def insertion_sort(self):
        for i in range(1, self.length):
            for j in range(i, 0, -1):
                if self.list[j] < self.list[j-1]:
                    self.list[j], self.list[j-1] = self.list[j-1], self.list[j]
        return self.list
    
    def merge_sort(self):
        if self.length <= 1:
            return self.list
        mid = self.length // 2
        left = self.list[:mid]
        right = self.list[mid:]
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if left:
            result.extend(left)
        if right:
            result.extend(right)
        return result
    
    def quick_sort(self):
        if self.length <= 1:
            return self.list
        pivot = self.list[0]
        left = []
        right = []
        for i in range(1, self.length):
            if self.list[i] < pivot:
                left.append(self.list[i])
            else:
                right.append(self.list[i])
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)
    
    def heap_sort(self):
        for i in range(self.length//2-1, -1, -1):
            self.heapify(i)
        for i in range(self.length-1, 0, -1):
            self.list[0], self.list[i] = self.list[i], self.list[0]
            self.heapify(0, i)
        return self.list
    def heapify(self, i, length=None):
        length = length or self.length
        left = 2*i+1
        right = 2*i+2
        largest = i
        if left < length and self.list[left] > self.list[largest]:
            largest = left
        if right < length and self.list[right] > self.list[largest]:
            largest = right
        if largest != i:
            self.list[i], self.list[largest] = self.list[largest], self.list[i]
            self.heapify(largest, length)
    
    def counting_sort(self):
        max_num = max(self.list)
        min_num = min(self.list)
        bucket = [0] * (max_num - min_num + 1)
        for i in range(self.length):
            bucket[self.list[i] - min_num] += 1
        index = 0
        for i in range(len(bucket)):
            while bucket[i] > 0:
                self.list[index] = i + min_num
                index += 1
                bucket[i] -= 1
        return self.list
    
    def radix_sort(self):
        max_num = max(self.list)
        for i in range(len(str(max_num))):
            bucket = [[] for _ in range(10)]
            for num in self.list:
                bucket[num // (10**i) % 10].append(num)
            self.list = [num for bucket_ in bucket for num in bucket_]
        return self.list
    
    def bucket_sort(self):
        max_num = max(self.list)
        min_num = min(self.list)
        bucket_size = (max_num - min_num) // self.length + 1
        bucket = [[] for _ in range(self.length)]
        for num in self.list:
            bucket[(num - min_num) // bucket_size].append(num)
        self.list = [num for bucket_ in bucket for num in bucket_]
        return self.list
    
    def shell_sort(self):
        gap = self.length // 2
        while gap > 0:
            for i in range(gap, self.length):
                for j in range(i, 0, -gap):
                    if self.list[j] < self.list[j-gap]:
                        self.list[j], self.list[j-gap] = self.list[j-gap], self.list[j]
            gap //= 2
        return self.list
    
    def bucket_sort_2(self):
        max_num = max(self.list)
        min_num = min(self.list)
        bucket_size = (max_num - min_num) // self.length + 1
        bucket = [[] for _ in range(self.length)]
        for num in self.list:
            bucket[(num - min_num) // bucket_size].append(num)
        self.list = [num for bucket_ in bucket for num in bucket_]
        return self.list


if __name__ == "__main__":
    test = sort([1,2,5,4,3,6,8,7,10,9])
    print(test.bubble_sort())
    print(test.selection_sort())
    print(test.insertion_sort())
    print(test.merge_sort())
    print(test.quick_sort())
    print(test.heap_sort())
    print(test.counting_sort())
    print(test.radix_sort())
    print(test.bucket_sort())
    print(test.shell_sort())
    print(test.bucket_sort_2())