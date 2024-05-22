# Linked list implementation in Python 
class Node: 
	# Creating a node 
	def __init__(self, item): 
		self.item = item 
		self.next = None
		# self.back = None

# BUATKAN NODENYA DULU
node1 = Node("JANAPRIA")
node2 = Node("MATARAM")
node3 = Node("SENGGIGI")
node4 = Node ("praya")
node5 = Node("ampenan")
node6 = Node("narmada")

# HUBUNGKAN SETIAP NODENYA
node1.next = node4
node4.next = node2
node2.next = node5
node5.next = node3
node3.next = node6
node6.next = node1


# node3.back = node2
# node2.back = node1

# Print Maju (Forward)
currentNode = node2

finish = node1

while currentNode:
	
	print(currentNode.item, end=" -> ")
	currentNode = currentNode.next
	if(currentNode == finish):
		print(currentNode.item)
		break
	

# Print Mundur (Backward)
#  cn = node3
# while cn:
	# print(cn.item, end=" -> ")
	# cn = cn.back
