
from collections import deque 

class Graph:
	def __init__(self):
		self.adj_list = {}
		
	def add_vertex(self, vertex):
		if vertex not in self.adj_list.keys():
			self.adj_list[vertex] = []
			return True
		return False
		
	def print_graph(self):
		for vertex in self.adj_list:
			print(vertex, " : ", self.adj_list[vertex])
	
	def add_edge(self, v1, v2):
		if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
			self.adj_list[v1].append(v2)
			self.adj_list[v2].append(v1)
			return True
		return False
		
	def remove_edge(self, v1, v2):
		if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
			try:
				self.adj_list[v1].remove(v2)
				self.adj_list[v2].remove(v1)
			except ValueError:
				pass
			return True
		return False
		
	def remove_vertex(self, vertex):
		if vertex in self.adj_list.keys():
			for other_vertex in self.adj_list[vertex]:
				self.adj_list[other_vertex].remove(vertex)
			del self.adj_list[vertex]
			return True
		return False 
			
	def bfs(self, vertex):
		visited = set()
		visited.add(vertex)
		#queue = []
		#queue.append(vertex)
		queue = deque([vertex])
		while queue:
			current_vertex = queue.popleft() #pop(0)
			print(current_vertex)
			for adj_vertex in self.adj_list[current_vertex]:
				if adj_vertex not in visited:
					visited.add(adj_vertex)
					queue.append(adj_vertex)
					
	def dfs(self, vertex):
		visited = set()
		stack = [vertex]
		while stack:
			current_vertex = stack.pop()
			if current_vertex not in visited:
				print(current_vertex)
				visited.add(current_vertex)
			for adj_vertex in self.adj_list[current_vertex]:
				if adj_vertex not in visited:
					stack.append(adj_vertex)
				
			
		
		

def main():
	mygraph = Graph()
	mygraph.add_vertex("A")
	mygraph.add_vertex("B")
	mygraph.add_vertex("C")
	mygraph.add_vertex("D")
	mygraph.add_vertex("E")
	mygraph.add_edge("A", "B")
	mygraph.add_edge("A", "C")
	mygraph.add_edge("B", "E")
	mygraph.add_edge("C", "D")
	mygraph.add_edge("D", "E")
	mygraph.print_graph()
	print("-----------------------")
	mygraph.bfs("A")
	print("-----------------------")
	mygraph.dfs("A")
	
	
	print("-----------------------")
	mygraph.remove_edge("B", "E")
	mygraph.remove_edge("D", "E")
	mygraph.remove_vertex("D")
	mygraph.print_graph()
	print("-----------------------")
	
	 


if __name__=="__main__":
	main()
	