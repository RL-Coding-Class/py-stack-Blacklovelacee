class Stack:
    """Provides stack container"""
    def __init__(self):
        self._items = []
        
    def push(self, data) -> None:
        self._items.append(data)
    
    def pop(self):
        if self._items == None:
            return None
        temp = self._items[-1]    
        del self._items[-1]
        return temp
    
    def get(self):
        if self._items == None:
            return None
        return self._items[-1]
    
    def length(self) -> int:
        return len(self._items)

    def __str__(self):
        pass

    def __repr__(self):
        pass
