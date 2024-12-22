class list_divider(list):
    def __truediv__(self, n):
        if n <= 0:
            raise ValueError()
        if type(n) is not int:
            raise TypeError()
        a, b = divmod(len(self), n)
        return [self[i * a  +  min(i, b) : (i + 1) * a  
                     +  min(i + 1, b)] for i in range(n)]