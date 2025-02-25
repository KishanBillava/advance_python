import unittest

class Node:
	def __init__(self, value):
		self.value  = value 
		self.next  = None
		

class Stack:
	def __init__(self, value):
		new_node = Node(value)
		self.top  = new_node 
		self.bottom = new_node
		self.height = 1
	
	def print_stack(self):
		temp = self.top
		while temp:
			print(temp.value)
			temp = temp.next 
		
	def push(self, value):
		new_node = Node(value)
		if self.height == 0:
			self.top = new_node 
		else:
			new_node.next = self.top 
			self.top = new_node 
		self.height += 1
		
	def pop(self):
		if self.height == 0:
			return None
		else:
			temp = self.top 
			self.top = self.top.next
			temp.next = None 
		self.height -=1
		return temp 
		
class TestStack(unittest.TestCase):
	def test_basic_operation(self):
		stack = Stack(10) 
		self.assertEqual(stack.top.value, 10)

		stack.push(20)
		self.assertEqual(stack.top.value, 20)
		
		popped = stack.pop()
		self.assertEqual(popped.value, 20)
		self.assertEqual(stack.top.value, 10)

def main():
	mystack = Stack(4)
	mystack.push(7)
	mystack.push(9)
	mystack.pop()
	print("---------------")
	mystack.print_stack()

if __name__=="__main__":
	main()
	
	
	