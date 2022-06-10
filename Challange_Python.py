# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:55:19 2022

@author: Jose Pablo Castillo
test for python engineer
"""



    
##Data Structure that manages search eficiently    
class BSTNode:
    #Countet that manage cuantity and lenght of the tree (without empty nodes)
    public_counter=0
    def __init__(self, val=None):
        """
        __init__ does the initial declaration.
    
        :param val: is just incase the BST starts with a number
        """ 
        self.counter=0
        self.left = None
        self.right = None
        self.val = val
        #the middle node counter
        BSTNode.public_counter+=1  
    
    def add(self, val):
        """
        add public funtion that add itself instances to right and left as next orderd value.
            take into consideration self.counter, that if the value reats itself, it registry an
            internal count so the binary tree doesnt expands
    
        :param val: is the start value in whicht will validate if needs to be count as a same node counter,
            or if it is less, goes to the left, or right if the value is bigger.
        """ 
        #Initial instance of the tree
        if not self.val:
            self.val = val
            return
        ##Need to have the all the records
        #just need to count if repeated
        if self.val == val:
            self.counter +=1
            BSTNode.public_counter+=1
            return
        #if its less
        if val <= self.val:
            if self.left:
                self.left.add(val)
                return
            self.left = BSTNode(val)
            return
        #if it is bigger
        if self.right:
            self.right.add(val)
            return
        self.right = BSTNode(val)
    
    def _get_min(self):
        """
        _get_min  private funtion that get the minimum value of the whole tree, athe the most left leaf 
        """ 
        current = self
        while current.left is not None:
            current = current.left
        return current.val
    
    def _get_max(self):
        """
        _get_max  private funtion that get the maximun value of the whole tree, athe the most left leaf 

        """ 
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    
    def delete(self, val):
        """
        delete  public funtion that deletes the node if the value matches nodes value. 
            the O(logn) search is efficient. 
            the counter is also modifued,in which this case is the BSTNode.Public_counter so you know
            the value of the treee nodes and counters that the tree has.
    
        :param val: value that need to be search and deleted from the tree.
        """ 
        BSTNode.public_counter-=(1+self.counter)
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self
    
    def exists(self, val):
        """
        exists public funtion that searchs if value exists in tree. the complexity is O9logn)
    
        param val:  the value thatyou need to search in the tree.
        """
        if val == self.val:
            return True
        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)
        if self.right == None:
            return False
        return self.right.exists(val)
    
    
    def preorder(self, vals):
        """
        preorder public funtion that order the values. Complexity O(n) always, since it shows the order currently
        thy were ingested. YOu could uncomment the Print values so you can look how the tree goes around
    
        param vals:  empty array/list in order to deliver you the tree sorted 
        """
        if self.val is not None:
            print("O ",self.val)
            vals.append(self.val)
        if self.left is not None:
            print("l ",self.val)
            self.left.preorder(vals)
        if self.right is not None:
            print("R ",self.val)
            self.right.preorder(vals)
        return vals
    
    def inorder(self, vals):
        """
        inorder public funtion that order the values. Complexity O(n) always, since it shows the order asc
        YOu could uncomment the Print values so you can look how the tree goes around
    
        param vals:  empty array/list in order to deliver you the tree sorted 
        """
        if self.left is not None:
            #print("L ",self.val)
            self.left.inorder(vals)
        if self.val is not None:
            #print("O ",self.val)
            vals.append(self.val)
        if self.right is not None:
            #print("R ",self.val)
            self.right.inorder(vals)
        return vals
    
    def _greater(self,compare):
        """
        _greater private funtion that iterates over the leafs so could deliver the amount of values 
        bigger thatn the compare value
    
        param compare:  a value in which you want to compare to the whole tree values. 
        
        Return big_count: value of the quantity of the numbers bigger thatn the compare param value
        """
        big_count=0
        if self.val > compare:
            big_count+= 1 + self.counter
        if self.left is not None:
            big_count+=self.left._greater(compare)
        if self.right is not None:
            big_count+=self.right._greater(compare)
        return big_count
    
    def _less(self,compare):
        """
        _less private funtion that iterates over the leafs so could deliver the amount of values 
        less than the compare value
    
        param compare:  a value in which you want to compare to the whole tree values. 
        
        Return big_count: value of the quantity of the numbers less thatn the compare param value
        """
        big_count=0
        if self.val < compare:
            big_count+= 1 + self.counter
        if self.left is not None:
            big_count+=self.left._less(compare)
        if self.right is not None:
            big_count+=self.right._less(compare)
        return big_count
    
    def _less_or_equal(self,compare):
        """
        _less_or_equal private funtion that iterates over the leafs so could deliver the amount of values 
        less or equal than the compare value
    
        param compare:  a value in which you want to compare to the whole tree values. 
        
        Return big_count: value of the quantity of the numbers less thatn the compare param value, 
            includin selfrepeting quantity value
        """
        big_count=0
        if self.val <= compare:
            big_count+= 1 + self.counter
        if self.left is not None:
            big_count+=self.left._less_or_equal(compare)
        if self.right is not None:
            big_count+=self.right._less_or_equal(compare)
        return big_count
    
    def _between (self,inf,sup):
        """
        _between private funtion that iterates over the leafs so could deliver the quantity of values 
        in bettween the inf and sup parameter. It doesnt matter the order of the inf,sup values, since 
        it willalways take the difference quantity between them. 
    
        param1 inf:  One limit of the between  interval
        param2 sup:  One limit of the between  interval
        
        Return big_count: value of the quantity of the numbers in betweent the param values 
            includin selfrepeting quantity value
        """
        if inf > sup:
            inf,sup = sup,inf
        return abs(self._less_or_equal(sup)-self._less(inf))
            
    
    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
    def build_stats(self):
        innerStatisticsAccess = StaticsAccess()
        innerStatisticsAccess.bigger=self._greater
        innerStatisticsAccess.less=self._less
        innerStatisticsAccess.between=self._between
        return innerStatisticsAccess

class StaticsAccess():
    """
    This is the access object that delivers the information required from the tree. 
    """
    innerBSTNodeRefference=0
    def bigger(self,compare=0):
        pass
    def less(self,selfcompare=0):
        pass

    
def main():
    print("ORIGINAL ")
    nums = [12,6,18,3,5,4,24,22,21,25,18,19,18,46,78,12,24,35,6,78,1,3,262,34,21,11,45,9]
    print(nums)
    bst = BSTNode()
    for num in nums:
        bst.add(num)
    
    variable=4
    stats=bst.build_stats()
    print("Quantity bigger than: ")
    print(stats.bigger(variable))
    print("Quantity less than: ")
    print(stats.less(variable))
    print("Quantity in between than: ")
    print(stats.between(variable+5,variable))
    
    
    
if __name__ == "__main__":
    main()
