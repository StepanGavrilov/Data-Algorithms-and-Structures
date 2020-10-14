import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """
        priority -> что будет на вершине.
        """
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Item {self.name}'


q = PriorityQueue()
q.push(Item('foo1'), 1)
q.push(Item('foo2'), 4)
q.push(Item('foo3'), 2)
q.push(Item('foo4'), 0)

print(q.pop())  # Возвращает элемент с наивысшим приоритетом
print(q.pop())
print(q.pop())
print(q.pop())