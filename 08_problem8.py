class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
        print(f"The item {item} is added in the queue")
    def dequeue(self):
        if not self.is_empty():
            removed_item = self.queue.pop(0)
            print(f"Dequeued item {removed_item}")
            return removed_item