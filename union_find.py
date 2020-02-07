class union_find:


    # Getters
    def get_num_components(self):
         return self.num_components
	
    def print_parents(self):
        for i in range(self.n):
            print("%d -> %d\n" % (i, self.parent[i]))

    # Constructor
    def __init__(self, n):
        # initialize your arrays here
        # And maybe helpful to make them of size "n + 1"...one larger than n
        self.parent =  [0]*(n) # parent[i] = parent of i
        self.rank =  [0]*(n)   # rank[i] = rank of subtree rooted at i
        self.num_components = n  # number of components
        self.n = n

        for i in range(len(self.parent)):
            self.parent[i] = i
         

	# This method should return the value of the "root" of the
	# tree that "number" is found inside.
    def find(self, calculated_idx):
        if calculated_idx != self.parent[calculated_idx]:
            self.parent[calculated_idx] = self.find(self.parent[calculated_idx])

        return self.parent[calculated_idx]

	# This method should union the two components that "a" and "b" belong to.
    def union(self, from_vertex, to_vertex):
        A = self.find(from_vertex)
        B = self.find(to_vertex)

        if (self.rank[A] == self.rank[B]):
            self.parent[B] = A
            self.rank[A]+=1

        elif (self.rank[A] < self.rank[B]):
			# stay rank of B
            self.parent[A] = B

        else:
			# stay rank of A
            self.parent[B] = A

        self.num_components -= 1

	# boolean areInSameComponent(a, b)::
	#    This method should return "true" if values "a" and "b" belong
	#    to the same component. Otherwise, "false" should be returned.
    def are_in_same_component(self, a, b):
        return self.find(a) == self.find(b)
	
