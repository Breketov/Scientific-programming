class graph_partition:
    def __init__(self, proc_id: int, num_procs: int):
        self.proc_id = proc_id
        self.num_procs = num_procs
        self.current = -1
        self.procs = []
        self.first = None
        self.second = None
        self.num_vertices = 0

    def fit(self, num_vertices: int):
        self.num_vertices = num_vertices
        self._calculate_partition_sizes()
        self._initialize_indices()
        return self

    def _calculate_partition_sizes(self):
        total_vertices = self.num_vertices * (self.num_vertices - 1) // 2
        div, mod = divmod(total_vertices, self.num_procs)
        self.procs = [div + (1 if i < mod else 0) for i in range(self.num_procs)]

    def _initialize_indices(self):
        sum_procs = sum(self.procs[:self.proc_id])
        remaining_vertices = self.num_vertices - 2
        
        for i in range(self.num_vertices - 1):
            if sum_procs - 1 <= remaining_vertices:
                self.first = i
                self.second = self.num_vertices - 1 - remaining_vertices + sum_procs - 1
                break
            remaining_vertices += self.num_vertices - 2 - i

    def __iter__(self):
        return self

    def __len__(self):
        return self.procs[self.proc_id]

    def __next__(self):
        self.current += 1
        
        if self.current >= len(self):
            raise StopIteration

        current_vertex = self.second + 1
        if current_vertex < self.num_vertices:
            self.second = current_vertex
        else:
            self.first += 1
            self.second = self.first + 1

        return self.first, self.second