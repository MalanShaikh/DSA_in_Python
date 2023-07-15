'''Python Program to create Linked list, inserting and deleting elements in Linked list with menu function'''

class Node:
	def __init__(self, data=None, next=None):
		self.data=data
		self.next=next

class LinkedList:
	def __init__(self, Node=None):
		self.length=0
		self.head=Node

	def length_func(self):
		current=self.head
		count=0
		while current!=None:
			count+=1
			current=current.next
		print(count)
	
	def insertAtStart(self, data):
		newNode= Node()
		newNode.data=data
		if(self.head==None):
			self.head=newNode
			print("Inserted Successfully!")
		else:
			newNode.next=self.head
			self.head=newNode
			print("Inserted Successfully!")
		self.length+=1
	
	def insertAtLast(self, data):
		newNode= Node()
		newNode.data= data
		if(self.head==None):
			self.head=newNode
		elif(self.head.next==None):
			self.head.next=newNode
		else:
			temp=self.head
			while temp.next!=None:
				temp=temp.next
				
			temp.next=newNode
		print("Inserted Successfully!")
		self.length+=1	
		
	def insertAtPos(self, data, pos):
		if(pos<=0 or pos>self.length+1):	
			print("Please..enter valid position!")
			return None
		else:
			if(pos==1):
				self.insertAtStart(data)
			elif(pos==self.length+1):
				self.insertAtLast(data)
			else:	
				newNode= Node()
				newNode.data=data
				
				temp=self.head
				count=1
				while count!=pos-1:
					count+=1
					temp=temp.next
				newNode.next=temp.next
				temp.next=newNode
				print("Inserted Successfully at Position {}!".format(pos))
				self.length+=1
					
	def deleteAtStart(self):
		if(self.length==0):
			print("Cannot delete..List is Empty")	
		else:
			self.head =self.head.next
			print("Deleted Successfully!")
			self.length-=1
	def deleteAtLast(self):
		if(self.length==0):
			print("Cannot delete..List is Empty")	
		else:
			current=self.head
			prev=self.head
			while current.next!=None:
				prev=current
				current=current.next
			prev.next=None
			print("Deleted Successfully!")
			self.length-=1

	def deleteAtPos(self, pos):
		if(pos<=0 or pos>self.length):
			print("Wrong Position..Enter valid Position")
			return None
		else:
			if(pos==1):
				self.deleteAtStart()
			elif(pos==self.length):
				self.deleteAtLast()
			else:
				temp= self.head
				count=1
				while count!=pos-1:
					temp=temp.next
					count+=1
				temp.next=temp.next.next
				print("Deleted Successfully at Position {}!".format(pos))
				self.length-=1
							

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


def menu():
	print("0. Create empty Linked List")
	print("1. Insert at the Beginning of Linked list")
	print("2. Insert at the Last of Linked list")
	print("3. Insert at the certain position in linked list")
	print("4. Delete from the Beginning of Linked list")
	print("5. Delete from the Last of Linked list")
	print("6. Delete from the certain position in linked list")
	print("7. Display Linked list")
	print("8. Display length of Linked list")
	print("9. Exit")
	choice= int(input("Enter your choice: "))
	return choice

def main():
	while True:
		choice=menu()
		if(choice==0):
			mylist= LinkedList()
		elif(choice==1):
			mylist= LinkedList()
			data=int(input("Enter data: "))
			mylist.insertAtStart(data)
		elif(choice==2):
			data=int(input("Enter data: "))
			mylist.insertAtLast(data)
		elif(choice==3):
			data=int(input("Enter data: "))
			pos=int(input("Enter position: "))
			mylist.insertAtPos(data, pos)
		elif(choice==4):
			mylist.deleteAtStart()
		elif(choice==5):
			mylist.deleteAtLast()
		elif(choice==6):
			pos=int(input("Enter position: "))
			mylist.deleteAtPos(pos)
		elif(choice==7):
			mylist.display()
		elif(choice==8):
			mylist.length_func()
		elif(choice==9):
			break
		else:
			print("Please enter valid choice!")

if __name__== "__main__":
	main()



	
		