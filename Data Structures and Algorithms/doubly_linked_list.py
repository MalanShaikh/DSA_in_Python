'''Python program to creating Doubly Linked List, inserting and deleting data in DLL'''
class Node:
	def __init__(self,prev=None, data=None, next=None):
		self.prev=prev
		self.data=data
		self.next=next
class DoublyLinkedList:
	def __init__(self, Node=None):
		self.length=0
		self.head=Node

	def insertAtStart(self, data):
		newNode=Node()
		newNode.data=data
		if(self.length==0):
			self.head=newNode
		else:
			self.head.prev=newNode
			newNode.next=self.head
			self.head=newNode
		print("Inserted Successfully!")
		self.length+=1

	def insertAtLast(self, data):
		newNode= Node()
		newNode.data=data
		
		if(self.length==0):
			self.head=newNode
		else:
			temp=self.head
			while temp.next!=None:
				temp=temp.next
			temp.next=newNode
			newNode.prev=temp
		print("Inserted Successfully!")
		self.length+=1
	
	def insertAtPos(self, data, pos):
		newNode= Node()
		newNode.data=data
		
		if(pos<=0 or pos>self.length+1):
			print("Cannot insert..enter valid position")
			return None
		else:
			if(pos==1):
				self.insertAtStart(data)
			elif(pos==self.length+1):
				self.insertAtLast(data)
			else:
				current=self.head
				temp=None
				count=1
				while count!=pos:
					temp=current
					current=current.next
					count+=1
				newNode.next=current
				current.prev=newNode
				temp.next=newNode
				newNode.prev=temp
				print("Inserted Successfully!")
			self.length+=1
					
	def deleteAtStart(self):
		self.head=self.head.next
		self.head.prev=None
		print("Deleted Successfully!")
		self.length-=1

	def deleteAtLast(self):
		current=self.head
		while current.next!=None:
			temp=current
			current=current.next
		temp.next=None
		print("Deleted Successfully!")
		self.length-=1

	def deleteAtPos(self, pos):
		if(pos<=0 or pos>self.length):
			print("Cannot delete..enter valid position")
		else:
			if(pos==1):
				self.deleteAtStart()
			elif(pos==self.length):
				self.deleteAtLast()
			else:
				current=self.head
				temp=None
				count=1
				while count!=pos:
					temp=current
					current=current.next
					count+=1
				temp.next=current.next
				current.next.prev=temp
				print("Deleted Successfully!")
				self.length-=1								
			
	def display(self):
		if(self.length==0):
			print("Linked list is empty!")
		else:
			temp=self.head
			while temp!=None:
				print(temp.data, end="<=>")
				temp=temp.next
			print("NULL")
	

dll=DoublyLinkedList()
dll.insertAtStart(1)
dll.display()
dll.insertAtLast(3)
dll.display()
dll.insertAtPos(2,2)
dll.display()
dll.insertAtPos(1.2,2)
dll.insertAtPos(1.4,2)
dll.display()
print("Length of Linked list is {}".format(dll.length))
dll.deleteAtStart()
dll.display()
dll.deleteAtLast()
dll.display()
dll.deleteAtPos(2)
dll.display()