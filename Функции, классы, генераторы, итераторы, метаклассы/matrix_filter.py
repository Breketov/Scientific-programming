import numpy as np

class score_filter:
    def __init__(self, min_score, max_score):
        self.min_score = min_score
        self.max_score = max_score
        self.results = []
        self.current_index = 0


    def fit(self, x, y, iterable):
        self.iterable = iterable
        self.x_cumsum = np.cumsum(x, dtype=np.float32)
        self.y_cumsum = np.cumsum(y, dtype=np.float32)
        total_sum = self.x_cumsum[-1] * self.y_cumsum[-1]
        
        for idx, jdx in self.iterable:
            condition_value = self.x_cumsum[idx] * self.y_cumsum[jdx] / total_sum
            if self.min_score < condition_value < self.max_score:
                self.results.append((idx, jdx))


    def __len__(self):
        return len(self.results)


    def __iter__(self):
        self.current_index = 0
        return self


    def __next__(self):
        if self.current_index >= len(self.results):
            raise StopIteration
        result = self.results[self.current_index]
        self.current_index += 1
        return result