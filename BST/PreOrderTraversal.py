class Node :
  def __init__(self,val,left = None,right=None) :
    self.val = val
    self.right = right 
    self.left = left
    
    

root = Node(1)

l1 = Node(4)
l2 = Node(5)
l3 = Node(6)
l4 = Node(7)


p1 = Node(2)
p2 = Node(3)

root.left = p1  
root.right = p2
p1.left = l1
p1.right = l2


p2.left = l3
p2.right = l4

def preorder(head) :
  
  if not head :
    return
  
  print(head.val)
  
  preorder(head.left)
  preorder(head.right)
  
preorder(root)
  
  
  
  
  
  
  
  
  
  
  
  
  
  