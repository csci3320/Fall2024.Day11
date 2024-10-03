class ArrayList:
    def __init__(self):
        self.size = 0
        self.array = [None, None]

    def add(self, value):
        if len(self.array) == self.size: # 1
            new_size = self.size*2
            new_list = []
            for index in range(new_size):
                new_list.append(None)
            for index in range(self.size):
                new_list[index] = self.array[index]
            self.array = new_list
        self.array[self.size] = value # 1
        self.size += 1 # 1
        #Without changing size: O(1)
        #With change: O(N)

    def contains(self, value):
        # if N is the size of my array list
        # O(N)
        for index in range(self.size):
            if self.array[index] == value:
                return True
        return False

    def remove(self, value):
        # if N is the size of my list....
        # Best Case: O(N)
        # Worst Case: O(N^2)
        for index in range(self.size):
            if self.array[index]==value:
                for index2 in range(index, self.size-1):
                    self.array[index2] = self.array[index2+1]
                self.size -= 1

    def as_list(self):
        to_return = []
        for index in range(self.size):
            to_return.append(self.array[index])
        return to_return

    def size(self):
        return self.size
    
al = ArrayList()
al.add("Burrito")
al.add("Fries")
print(al.as_list())
print(al.contains("Pizza"))
print(al.contains("Fries"))
al.remove("Fries")
print(al.as_list())
al.add("Pizza")
al.add("Fried Chicken")
print(al.as_list())
