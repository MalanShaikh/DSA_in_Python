'''Python program to search, update, reverse Linked list'''

class Node:
	def __init__(self, data=None, next=None):
		self.data=data
		self.next=next

class LinkedList:
	def __init__(self, Node=None):
		self.length=0
		self.head=Node

	def insert(self, data):
		newNode= Node()
		newNode.data=data

		newNode.next=self.head
		self.head=newNode
		print("Inserted Successfully!")
		self.length+=1

	def delete(self):
		if(self.length==0):
			print("Cannot delete..List is Empty")	
		else:
			self.head =self.head.next
			print("Deleted Successfully!")
			self.length-=1

	def search(self, data):
		current=self.head
		while current!=None:
			if(current.data==data):
				print("Data Found!")
				return True
			else:
				current=current.next
		
		print("Data not found")
		return False

	def update(self, curr_data, new_data):
		current=self.head
		while current!=None:
			if(current.data==curr_data):
				current.data=new_data
				print("Updated Successfully!")
				return True
			else:
				current=current.next

		print("{} is not present in Linked list".format(curr_data))
		return False	
		
	def reverse(self):
		if(self.length==0):
			print("Linked list is empty!")
		elif(self.head!=None and self.head.next==None):
			print("Only one node is present")
		else:
			temp=None
			nextNode= None
			while self.head!=None:
				nextNode=self.head.next
				self.head.next=temp
				temp=self.head
				self.head=nextNode
			if(self.head==None):
				self.head=temp
					
	
	def display(self):
		if(self.length==0):
			print("Linked list empty!")
		else:	
			print("Printing Linked list: ")
			temp= self.head
			while temp!=None:
				print(temp.data, end="->")
				temp=temp.next
			print("NULL")

mylist= LinkedList()
mylist.insert(0)
mylist.insert(1)
mylist.insert(2)
mylist.insert(3)
mylist.insert(4)
mylist.insert(5)
mylist.display()
mylist.delete()
mylist.display()
mylist.search(2)
mylist.update(4,6)
mylist.display()
mylist.reverse()
mylist.display()