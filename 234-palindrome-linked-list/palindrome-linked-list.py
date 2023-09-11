# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.temp=head
        self.l=[]
        while self.temp is not None:
            self.l.append(self.temp.val)
            self.temp=self.temp.next
        self.rl=[]
        self.rl=self.l[::-1]
        self.temp2=head
        self.i=0
        self.c=0
        while self.temp2 is not None:
            if self.temp2.val==self.rl[self.i]:
                self.c+=1
            self.i+=1
            self.temp2=self.temp2.next
        if self.c==len(self.rl):
            return 1
        else: 
            return 0
        