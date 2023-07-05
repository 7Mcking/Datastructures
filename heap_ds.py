# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self, element):
        self.heap_array.append(element)
        self._heapify_up(len(self.heap_array) - 1)

    def extract_max(self):
        if not self.heap_array:
            raise IndexError("Heap is empty")

        max_element = self.heap_array[0]
        self.heap_array[0] = self.heap_array[-1]
        self.heap_array.pop()
        self._heapify_down(0)

        return max_element

    def _heapify_up(self, index):
        if index == 0:
            return

        parent_index = (index - 1) // 2

        if self.heap_array[parent_index] < self.heap_array[index]:
            self.heap_array[parent_index], self.heap_array[index] = (
                self.heap_array[index],
                self.heap_array[parent_index],
            )
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest_index = index

        if (
            left_child_index < len(self.heap_array)
            and self.heap_array[left_child_index] > self.heap_array[largest_index]
        ):
            largest_index = left_child_index

        if (
            right_child_index < len(self.heap_array)
            and self.heap_array[right_child_index] > self.heap_array[largest_index]
        ):
            largest_index = right_child_index

        if largest_index != index:
            self.heap_array[largest_index], self.heap_array[index] = (
                self.heap_array[index],
                self.heap_array[largest_index],
            )
            self._heapify_down(largest_index)

    def empty(self):
        return len(self.heap_array) == 0

    def size(self):
        return len(self.heap_array)


if __name__ == "__main__":
    heap = Heap()
    my_list = [12,10, -10, 100, 20, 200]
    for element in my_list:
        heap.insert(element)
        print(heap.heap_array)



    while not heap.empty():
        print(heap.heap_array)
        print(heap.extract_max())



    print(10//3)


