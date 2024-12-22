def cmp_to_key(comparator):
    class CastClass:
        def __init__(self, val):
            self.val = val
        
        def __lt__(self, other):
            return comparator(self.val, other.val) == -1
    
    return CastClass