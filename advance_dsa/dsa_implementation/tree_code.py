
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
	 


if __name__=="__main__":
	main()