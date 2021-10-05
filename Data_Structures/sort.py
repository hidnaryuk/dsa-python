class sort:
    def __init__(self, list):
        self.list = list
        self.length = len(list)

    def bubble_sort(self):
        """## Bubble Sort Function

        Bubble sort makes multiple passes through a list.
        It compares adjacent items and exchanges those that are out of order. 
        Each pass through the list places the next largest value in its proper place. 
        In essence, each item “bubbles” up to the location where it belongs.

        Time complexity:
            worst-case: n^2
            average: n^2 
            best-case: n

        Space complexity: 1

        Parameters: 
            list: unsorted list

        Returns:
            list: Sorted list
        """
        for i in range(self.length):
            for j in range(self.length-1):
                if self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
        return self.list

    def selection_sort(self):
        """## Selection Sort Function

        The selection sort improves on the bubble sort by making only one exchange for every pass through the list. 
        In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location.

        Time complexity:
            worst-case: n^2
            average: n^2 
            best-case: n^2

        Space complexity: 1

        Parameters: 
            list: unsorted list

        Returns:
            list: Sorted list
        """
        for i in range(self.length):
            min_index = i
            for j in range(i+1, self.length):
                if self.list[j] < self.list[min_index]:
                    min_index = j
            self.list[i], self.list[min_index] = self.list[min_index], self.list[i]
        return self.list

    def insertion_sort(self):
        """## Insertion Sort Function

        The insertion sort, although still O(n^2), works in a slightly different way. 
        It always maintains a sorted sublist in the lower positions of the list. 
        Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger.

        Time complexity:
            worst-case: n^2
            average: n^2 
            best-case: n

        Space complexity: 1

        Parameters: 
            list: unsorted list

        Returns:
            list: Sorted list
        """
        for i in range(1, self.length):
            for j in range(i, 0, -1):
                if self.list[j] < self.list[j-1]:
                    self.list[j], self.list[j-1] = self.list[j-1], self.list[j]
        return self.list

    def merge_sort(self):
        """## Merge Sort Function

        Merge sort is a recursive algorithm that continually splits a list in half. 
        If the list is empty or has one item, it is sorted by definition (the base case). 
        If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. 
        Once the two halves are sorted, the fundamental operation, called a merge, is performed.

        Time complexity:
            worst-case: n*log(n)
            average: n*log(n)
            best-case: n*log(n)

        Space complexity: n

        Parameters: 
            list: unsorted list

        Returns:
            list: Sorted list
        """
        if self.length <= 1:
            return self.list
        mid = self.length // 2
        left = self.list[:mid]
        right = self.list[mid:]
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return self.merge(left, right)

    def merge(self, left, right):
        """## Merge Function

        This function takes two lists and merges them together into a single list.

        Parameters: 
            list: list 1
            list: list 2

        Returns:
            list: merged list
        """
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
        """## Quick Sort Function

        The quick sort uses divide and conquer to gain the same advantages as the merge sort, while not using additional storage. 
        As a trade-off, however, it is possible that the list may not be divided in half. 
        When this happens, we will see that performance is diminished.

        A quick sort first selects a value, which is called the pivot value. 
        The role of the pivot value is to assist with splitting the list. 
        The actual position where the pivot value belongs in the final sorted list, commonly called the split point, will be used to divide the list for subsequent calls to the quick sort.

        Time complexity:
            worst-case: n^2
            average: n*log(n)
            best-case: n*log(n)

        Space complexity: log(n)

        Parameters: 
            list: unsorted list

        Returns:
            list: Sorted list
        """
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
        """## Heap Sort Function

        The heap sort is quite the same as the selection sort, where we find the maximum element and put it at the end. 
        It is based on a comparison sorting algorithm which works on Binary heap data structure.
        ITs concept is to "eliminate" the element from the heap part of the list one-by-one and insert them to the sorted part of the list.

        Time complexity:
            worst-case: n*log(n)
            average: n*log(n)
            best-case: n*log(n)

        Space complexity: 1

        Parameters: 
            list: unsorted list

        Returns:
            list: Sorted list
        """
        for i in range(self.length//2-1, -1, -1):
            self.heapify(i)
        for i in range(self.length-1, 0, -1):
            self.list[0], self.list[i] = self.list[i], self.list[0]
            self.heapify(0, i)
        return self.list

    def heapify(self, i, length=None):
        """## Heapify Function

        This function is used by the heap_sort() function to heapify the subtree rooted at index i.

        Parameters: 
            int: index
            length: size of heap
        """

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
        """## Counting Sort Function

        The counting sort algorithm sorts the elements of an array by counting the number of occurrences of each unique element in the array.
        The count is stored in an auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.

        Time complexity:
            n+k 
                n: Number of elements in the array; 
                k: Range of the elements (largest element - smallest element)

        Space complexity: k

        Parameters: 
            list: unsorted list

        Returns:
            list: Sorted list
        """
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
        """## Radix Sort Function

        Radix sort sorts the elements by first grouping the individual digits of the same place value. 
        Then, sort the elements according to their increasing/decreasing order.

        Time complexity:
            worst-case: nk
            average: nk
            best-case: nk

        Space complexity: n+k

        Parameters: 
            list: unsorted list

        Returns:
            list: Sorted list
        """
        max_num = max(self.list)
        for i in range(len(str(max_num))):
            bucket = [[] for _ in range(10)]
            for num in self.list:
                bucket[num // (10**i) % 10].append(num)
            self.list = [num for bucket_ in bucket for num in bucket_]
        return self.list

    def bucket_sort(self):
        """## Bukket Sort Function

        Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an array into a number of buckets. 
        Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting.

        Time complexity:
            worst-case: n²
            average: n+k
            best-case: n+k

        Space complexity: n+k

        Parameters: 
            list: unsorted list

        Returns:
            list: Sorted list
        """
        max_num = max(self.list)
        min_num = min(self.list)
        bucket_size = (max_num - min_num) // self.length + 1
        bucket = [[] for _ in range(self.length)]
        for num in self.list:
            bucket[(num - min_num) // bucket_size].append(num)
        self.list = [num for bucket_ in bucket for num in bucket_]
        return self.list

    def shell_sort(self):
        """## Shell Sort Function

        Shell sort is a generalized version of the insertion sort algorithm. 
        It first sorts elements that are far apart from each other and successively reduces the interval between the elements to be sorted.
        The interval between the elements is reduced based on the sequence used. 

        Time complexity:
            worst-case: n²
            average: n*log(n)
            best-case: n*log(n)

        Space complexity: 1

        Parameters: 
            list: unsorted list

        Returns:
            list: Sorted list
        """
        gap = self.length // 2
        while gap > 0:
            for i in range(gap, self.length):
                for j in range(i, 0, -gap):
                    if self.list[j] < self.list[j-gap]:
                        self.list[j], self.list[j -
                                                gap] = self.list[j-gap], self.list[j]
            gap //= 2
        return self.list

    def bucket_sort_2(self):
        """ Identical to bucket_sort() """
        max_num = max(self.list)
        min_num = min(self.list)
        bucket_size = (max_num - min_num) // self.length + 1
        bucket = [[] for _ in range(self.length)]
        for num in self.list:
            bucket[(num - min_num) // bucket_size].append(num)
        self.list = [num for bucket_ in bucket for num in bucket_]
        return self.list


if __name__ == "__main__":
    test = sort([1, 2, 5, 4, 3, 6, 8, 7, 10, 9])
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
