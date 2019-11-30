# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#reverse integer
def roman(string):
    s=len(string)
    w=[]*s
    w=list(string)
    if w[0]=='m':
        num=1000
    if w[0]=='i':
        num=1
    if w[0]=='c':
        num=100
    if w[0]=='x':
        num=10
    if w[1]=='i':
        num=num+1
    if w[1]=='x':
        num=num+10
    if w[1]=='c':
        num=num+100
    if w[1]=='m':
        num=num+1000
    
        
    return(num)
    
    
    