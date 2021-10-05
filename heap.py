class heap:
    def __init__(self, heap_list=None):
        self.heap_list = []
        if heap_list is not None:
            self.heap_list = heap_list
            self.build_heap()

    def build_heap(self):
        for i in range(len(self.heap_list) // 2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(self.heap_list) and self.heap_list[left] > self.heap_list[largest]:
            largest = left
        if right < len(self.heap_list) and self.heap_list[right] > self.heap_list[largest]:
            largest = right
        if largest != i:
            self.heap_list[i], self.heap_list[largest] = self.heap_list[largest], self.heap_list[i]
            self.heapify(largest)

    def insert(self, value):
        self.heap_list.append(value)
        self.heapify(len(self.heap_list) - 1)

    def delete(self):
        self.heap_list[0], self.heap_list[-1] = self.heap_list[-1], self.heap_list[0]
        value = self.heap_list.pop()
        self.heapify(0)
        return value

    def __str__(self):
        return str(self.heap_list)

if __name__ == "__main__":
    h = heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(h)
    h.insert(10)
    print(h)
    h.delete()
    print(h)