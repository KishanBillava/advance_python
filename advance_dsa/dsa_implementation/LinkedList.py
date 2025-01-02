

class Node:
	"""
	A class representing a node in a linked list 
	Attribute 
		value (int) : The value stored in the node 
		next (Node) :  A reference to the next node in linked list
	"""
	def __init__(self, value):
		self.value = value
		self.next  = None


class LinkedList:
	""" 
	A class representing a singly linked list 
	Attribtues:
		head
		tail 
		length
	"""
	def __init__(self, value: int ) -> None:
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length  = 1 
		
	def append(self, value :  int ) -> bool:
		new_node  = Node(value)
		if self.length == 0:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
		self.length +=1
		return True
	
	def pop(self):
		if self.length  == 0:
			return None
		pre = self.head
		temp = self.head
		if self.length == 1:
			self.head = None 
			self.tail = None 
		else:
			while(temp.next):
				pre = temp
				temp = temp.next
		self.tail = pre
		self.tail.next = None 
		self.length -= 1
		return temp
			
	def prepend(self, value):
		new_node  = Node(value)
		if self.length == 0:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head  = new_node
		self.length += 1 
		return True
		
	def pop_first(self):
		if self.length == 0 :
			return None
		# here temp and head are like pointer 
		# temp is pointing to node that head is point too that is a node 
		# once we move the head pointer to next the temp pointer is still pointing the previous node 
		temp = self.head
		self.head = self.head.next
		temp.next = None 
		self.length -=1
		if self.length == 0:
			self.tail = None
		return temp
		
	def get(self, index):
		if index < 0 or index >= self.length:
			return None 
		temp = self.head
		for _ in range(index):
			temp = temp.next
		return temp
	
	def set_value(self, index, value):
		new_node  = Node(value)
		temp = self.get(index)
		if temp:
			temp.value = value
			return True
		return False
		
	def insert(self, index, value):
		if index < 0 or index >= self.length:
			return False 
		if index == 0:
			return self.prepend(value)
		if index == self.length:
			return self.append(value)	
		new_node  = Node(value)
		temp = self.get(index -1)
		new_node.next = temp.next 
		temp.next = new_node
		self.length +=1
		return True
		
	def remove(self, index):
		if index < 0 or index >= self.length:
			return None 
		if index == 0:
			return self.pop_first()
		if index == self.length -1:
			return self.pop()
		prev = self.get(index -1)
		temp = prev.next
		prev.next = temp.next
		temp.next = None
		self.length -=1 
		return temp  
		
	def reverse(self):
		temp = self.head 
		self.head = self.tail
		self.tail = temp
		before  = None
		after = temp.next 
		for _ in range(self.length):
			after = temp.next
			temp.next = before
			before  = temp 
			temp = after
	
	# print Node value 
	def print_list(self) -> None:
		temp = self.head
		while(temp):
			print(temp.value)
			temp = temp.next


def main():
	mylinklist = LinkedList(4)
	# print(mylinklist.head.value) 
	mylinklist.append(5)
	mylinklist.append(9)
	mylinklist.append(3)
	mylinklist.pop()
	mylinklist.prepend(1)
	mylinklist.pop_first()
	print(mylinklist.get(2))
	print(mylinklist.set_value(1, 7))
	print(mylinklist.insert(1, 17))
	mylinklist.remove(1)
	mylinklist.reverse()
	print("------------------")
	mylinklist.print_list()
	print("------------------")
	
	

if __name__=="__main__":
	main()
	
	
	
