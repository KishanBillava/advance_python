
class Node:
	def __init__(self, value):
		self.value = value 
		self.left = None
		self.right  = None 
		
class BinarySearchTree():
	def __init__(self):
		self.root  = None

	def insert(self, value):
		new_node  = Node(value)
		if self.root is None:
			self.root = new_node
			return True
		temp = self.root
		while(True):
			if new_node.value == temp.value:
				return False 
			if new_node.value <  temp.value:
				if temp.left is None:
					temp.left  = new_node 
					return True
				temp = temp.left
			else:
				if temp.right is None:
					temp.right = new_node
					return True
				temp = temp.right
	
	def contains(self, value):
		if self.root == None:
			return False 
		temp = self.root
		while(temp is not None):
			if temp.value == value:
				return True
			if  value <  temp.value:
				temp = temp.left
			else:
				temp = temp.right 
		return False
	
	def BFS(self):
		current_node  = self.root
		queue = []
		results = []
		queue.append(current_node)
		while(len(queue) > 0):
			current_node = queue.pop(0)
			results.append(current_node.value)
			if current_node.left is not None:
				queue.append(current_node.left)
			if current_node.right is not None:
				queue.append(current_node.right)
		return results 
			
	# preorder 	
	def dfs_preorder(self):
		results = []
		
		def traverse(current_node):
			results.append(current_node.value)
			if current_node.left is not None:
				traverse(current_node.left)
			if current_node.right is not None:
				traverse(current_node.right)
			
		traverse(self.root)
		return results
	
	# postorder
	def dfs_postorder(self):
		results = []
		
		def traverse(current_node):
			if current_node.left is not None:
				traverse(current_node.left)
			if current_node.right is not None:
				traverse(current_node.right)
			results.append(current_node.value) 
			
		traverse(self.root)
		return results
	
	# inorder
	def dfs_inorder(self):
		results = []
		
		def traverse(current_node):
			if current_node.left is not None:
				traverse(current_node.left)
			results.append(current_node.value)
			if current_node.right is not None:
				traverse(current_node.right)
			
		traverse(self.root)
		return results
		
		

def main():
	mybst = BinarySearchTree()
	mybst.insert(47)
	mybst.insert(21)
	mybst.insert(76)
	mybst.insert(18)
	mybst.insert(27)
	mybst.insert(52)
	mybst.insert(82)
	print("-------------")
	print(mybst.contains(17))
	print(mybst.BFS())
	print("-------------")
	print(mybst.dfs_preorder())
	print("-------------")
	print(mybst.dfs_postorder())
	print("-------------")
	print(mybst.dfs_inorder())


if __name__=="__main__":
	main()
	
	
	
	