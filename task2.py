class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
       
def tree_insert( tree, value):
    if tree==None:
        tree=BinTreeNode(value)
    else:
        if(value < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(value)
            else:
                tree_insert(tree.left,value)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(value)
            else:
                tree_insert(tree.right,value)
    return tree


    
    
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)

        
def preorder(tree):
    print(tree.value)
    if(tree.left!=None):
        preorder(tree.left)
    if(tree.right!=None):
        preorder(tree.right)
        
        
def MinimumNodeValue(tree):
    currentnode = tree
    
    while(currentnode.left != None):
        currentnode = currentnode.left
        
    return currentnode    
        
        
        
def nodedeleter(tree, value):
    if(tree == None):
        return tree
    
    if(value < tree.value):
        tree.left = nodedeleter(tree.left, value)
        
    elif(value > tree.value):
        tree.right = nodedeleter(tree.right, value)
        
    else:
        if(tree.left == None):
            temporaryvalue = tree.right
            tree = None
            return temporaryvalue
        elif(tree.right == None):
            temporaryvalue = tree.left
            tree = None
            return temporaryvalue
        
        temporaryvalue = MinimumNodeValue(tree.right)
        
        tree.value = temporaryvalue.value
        
        tree.right = nodedeleter(tree.right, temporaryvalue.value)
        
    return tree    
            
            
 
if __name__ == '__main__':
    
    ######################################
    tree = None
    tree = tree_insert(tree, 10)
    tree = tree_insert(tree, 5)
    tree = tree_insert(tree, 2)
    tree = tree_insert(tree, 3)
    tree = tree_insert(tree, 4)
    tree = tree_insert(tree, 11)
    print("the in order traversal of the given tree is:")
    in_order(tree)
    ########################################
    
    print("\n now deleting 2: ")
    tree = nodedeleter(tree, int(input("please select a node to delete")))
    
    print("In order traversal with the 1st node removed is: ")
    in_order(tree)
    
    print("\n now deleting 3: ")
    tree = nodedeleter(tree, int(input("please select a node to delete")))
    print("In order traversal with the 2nd node removed is: ")
    in_order(tree) 
    
    print("\n now deleting 4: ")
    tree = nodedeleter(tree, int(input("please select a node to delete")))
    print("In order traversal with the 3rd node removed is: ")
    in_order(tree) 
    

   



#print("BST in postorder is: ")
#postorder(tree)


#print("BST in, in-order is: ")
#in_order(tree)
    
