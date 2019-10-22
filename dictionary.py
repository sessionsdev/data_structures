

class Dictionairy:

    def __init__(self, size):
        self._size = size
        self._data = [None] * (size)
        self._item_count = 0



    def set(self, key, value):
        self.expand()
        i = self.get_index(key)
        if self.contains(key) == True:
            return
        if not self._data[i]:
            self._data[i] = []
        self._data[i].append((key, value))
        self._item_count += 1



    def get(self, key):
        i = self.get_index(key)
        if self._data[i] == None:
            return None
        else:
            for pair in self._data[i]:
                if pair[0] == key:
                    return pair[1]



    def contains(self, key):
        i = self.get_index(key)
        if self._data[i] == None:
            return False
        for pair in self._data[i]:
            if pair[0] == key:
                return True


    def delete(self, key):
        i = self.get_index(key)
        if self.contains(key) == False:
            return
        for pair in self._data[i]:
            if pair[0] == key:
                self._data[i].remove(pair)
                self._item_count -= 1
        
    

    def get_index(self, key):
        i = hash(key) % (self._size)
        return abs(i)


    def __repr__(self):
        d = []
        for i in self._data:
            if i is not None:
                for pair in i:
                    p = ": ".join(pair)
                    d.append(p)
        return "{" + "; ".join(d) + "}"

    
    def expand(self):
        if self._item_count == (self._size / 1.5):
            place_holder = []
            for item in self._data:
                for pair in item:
                    place_holder.append(pair)
            self._data.clear()
            self._data.extend([None] * self._size)
            self._size += len(self._data)
            for item in place_holder:
                i = self.get_index(item[0])
                if not self._data[i]:
                    self._data[i] = []
                self._data[i].append((item[0], item[1]))
                

    
    # def expand(self):
    #     if self._item_count == (self._size / 1.5):
    #         place_holder = [None] *(self._size * 2)
    #         for item in self._data:
    #             for pair in item:
    #                 place_holder.append(pair)
    #         for item in place_holder:
    #             i = self.get_index(item[0])
    #             if not self._data[i]:
    #                 self._data[i] = []
    #             self._data[i].append((item[0], item[1]))
    #         # self._data.clear()
    #         # self._data.extend([None] * self._size)
    #         self._data = place_holder
    #         self._size += len(self._data)

