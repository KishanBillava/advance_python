

class Node:
	def __init__(self, value):
		self.value = value
		self.next  = None
		
class Queue:
	def __init__(self, value):
		new_node = Node(value)
		self.first  = new_node 
		self.last  = new_node 
		self.length = 1
		
	def enqueue(self, value : int ) -> None:
		""" 
		This function represent to add new node to the queue
		"""
		new_node = Node(value)
		
		if self.length == 0:
			self.first = new_node
			self.last  = new_node
		else:
			self.last.next = new_node
			self.last  = new_node
		self.length +=1
		
	def dequeue(self):
		if self.length == 0:
			return None
		temp = self.first
		if self.length == 1:
			self.first = None
			self.last = None
		else:
			self.first = self.first.next
			temp.next = None
		self.length -=1
		return temp
			
		
	def print_queue(self):
		temp = self.first 
		while temp:
			print(temp.value)
			temp = temp.next
		



def main():
	myqueue = Queue(7)
	myqueue.enqueue(5)
	myqueue.enqueue(3)
	myqueue.dequeue()
	print("--------------")
	myqueue.print_queue()

if __name__=="__main__":
	main()
	
	
	