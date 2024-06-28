import time

class SortableList:
    def __init__(self, data, algorithms):
        self.data = data
        self.algorithms = algorithms

    def __getattr__(self, name):
        if name in self.algorithms:
            def method():
                start_time = time.time()
                sorted_data = self.algorithms[name](self.data)
                elapsed_time = time.time() - start_time
                return (f"The sorted list using {name.replace('_', ' ')} is: {sorted_data} "
                        f"Time: {elapsed_time:.6f} seconds")
            return method
        raise AttributeError(f"'SortableList' object has no attribute '{name}'")

class SortingLibrary:
    def __init__(self):
        self.algorithms = {
            'quick_sort': self.quick_sort,
            'merge_sort': self.merge_sort,
            'bubble_sort': self.bubble_sort,
            'insertion_sort': self.insertion_sort,
            'selection_sort': self.selection_sort,
            'heap_sort': self.heap_sort,
            'shell_sort': self.shell_sort,
            'counting_sort': self.counting_sort,
            'radix_sort': self.radix_sort,
            'bucket_sort': self.bucket_sort
        }
    
    def sort(self, data, algorithm='quick_sort'):
        if algorithm in self.algorithms:
            return self.algorithms[algorithm](data)
        else:
            raise ValueError(f"Algorithm '{algorithm}' not found.")

    def get_sortable_list(self, data):
        return SortableList(data, self.algorithms)

    def quick_sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def merge_sort(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.merge_sort(data[:mid])
        right = self.merge_sort(data[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def bubble_sort(self, data):
        data = data[:]
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

    def insertion_sort(self, data):
        data = data[:]
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

    def selection_sort(self, data):
        data = data[:]
        for i in range(len(data)):
            min_idx = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
        return data

    def heap_sort(self, data):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[i] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        data = data[:]
        n = len(data)
        for i in range(n//2 - 1, -1, -1):
            heapify(data, n, i)
        for i in range(n-1, 0, -1):
            data[i], data[0] = data[0], data[i]
            heapify(data, i, 0)
        return data

    def shell_sort(self, data):
        data = data[:]
        n = len(data)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = data[i]
                j = i
                while j >= gap and data[j - gap] > temp:
                    data[j] = data[j - gap]
                    j -= gap
                data[j] = temp
            gap //= 2
        return data

    def counting_sort(self, data):
        if len(data) == 0:
            return data
        max_val = max(data)
        min_val = min(data)
        range_of_elements = max_val - min_val + 1
        count = [0] * range_of_elements
        output = [0] * len(data)
        for number in data:
            count[number - min_val] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        for i in range(len(data) - 1, -1, -1):
            output[count[data[i] - min_val] - 1] = data[i]
            count[data[i] - min_val] -= 1
        return output

    def radix_sort(self, data):
        def counting_sort_exp(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10
            for i in range(n):
                index = (arr[i] // exp)
                count[index % 10] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]
            i = n - 1
            while i >= 0:
                index = (arr[i] // exp)
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1
            for i in range(n):
                arr[i] = output[i]

        max1 = max(data)
        exp = 1
        while max1 // exp > 0:
            counting_sort_exp(data, exp)
            exp *= 10
        return data

    def bucket_sort(self, data):
        if len(data) == 0:
            return data
        bucket = []
        slot_num = 10
        for i in range(slot_num):
            bucket.append([])
        max_value = max(data)
        for j in data:
            index = int(slot_num * j / (max_value + 1))
            bucket[index].append(j)
        for i in range(slot_num):
            bucket[i] = self.insertion_sort(bucket[i])
        result = []
        for i in range(slot_num):
            result.extend(bucket[i])
        return result

