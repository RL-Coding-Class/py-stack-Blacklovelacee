class Stack:
    """Provides stack container"""
    def __init__(self, _stack_type = None):
        self._items = []
        self._stack_type = _stack_type

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
        return str(self._items)

    def __repr__(self):
        return f"Stack({self._items}, {self._stack_type})"
