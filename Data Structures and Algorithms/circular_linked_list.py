'''Python program to create circular linked list, inserting and deleting elements in circular linked list'''

class Node:
	def __init__(self, data=None, next=None):
		self.data=data
		self.next=next

class CircularLinkedList:
	def __init__(self, Node=None):
		self.length=0
		self.head=Node
	
	def insertAtBeg(self, data):
		newNode=Node()
		newNode.data=data
		current=self.head
		
		if(self.head==None):
			self.head=newNode
			newNode.next=self.head
			print("Node inserted Successfully!")
		else:
			while current.next!=self.head:
				current=current.next
			newNode.next=self.head
			current.next=newNode
			self.head=newNode
			print("Node inserted Successfully!")
		self.length+=1

	def insertAtEnd(self, data):
		newNode=Node()
		newNode.data=data
		current=self.head

		if(self.head==None):
			self.head=newNode
			newNode.next=self.head
			print("Node inserted Successfully!")
		else:
			while current.next!=self.head:
				current=current.next
			current.next=newNode
			newNode.next=self.head
			print("Node inserted Successfully!")
		self.length+=1	

	def deleteAtBeg(self):
		if(self.head==None):
			print("Circular Linked list is empty!")

		elif(self.head.next==self.head):
			self.head=None
			self.length-=1
		else:
			temp=self.head
			while temp.next!=self.head:
				temp=temp.next
			temp.next=self.head.next
			self.head=self.head.next
			print("Deleted from Beginning Successfully!")
			self.length-=1
	def deleteAtEnd(self):
		if(self.head==None):
			print("Circular Linked list is Empty")

		elif(self.head.next==self.head):
			self.head=None
			self.length-=1
		else:
			current=self.head
			prev=None
			while current.next!=self.head:
				prev=current
				current=current.next
			prev.next=self.head
			print("Deleted from last Successfully!")
			self.length-=1

	def print_cll(self):
		if(self.head==None):
			print("Circular Linked list is Empty!")
		else:
			current=self.head
			print(current.data, end="->")
			current=current.next
			while current!=self.head:
				print(current.data, end="->")
				current=current.next
			print("Head")

cll=CircularLinkedList()
cll.insertAtBeg(50)
cll.insertAtBeg(20)
cll.insertAtEnd(60)
cll.insertAtEnd(80)
cll.print_cll()
cll.deleteAtBeg()
cll.deleteAtEnd()
cll.print_cll()
cll.deleteAtBeg()
cll.deleteAtEnd()
cll.print_cll()