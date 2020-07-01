class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        depth = 0
        result = 0
        
        while(l1 != None):
            l1_number = l1.val * 10 ** depth
            l2_number = l2.val * 10 ** depth
            l1 = l1.next
            l2 = l2.next
            depth += 1
            result += l1_number + l2_number
        
        resultList = []
        
        for i in range(depth):
            value = result % 10
            result -= value
            result //= 10
            resultList.insert(0,value)
            
        nodeList = ListNode(resultList.pop(0))
        
        for num in resultList:
            nodeListNew = ListNode(num)
            nodeListNew.next = nodeList
            nodeList = nodeListNew
            
        return nodeList
            
