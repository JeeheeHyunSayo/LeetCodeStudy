'''
Q. 주어진 single-linked list 순서 뒤집기
A. 임시 메모리 tmp 사용! cur.next.next = cur로 변환해주기
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        cur, nxt = head, head.next
        head.next = None
        
        while nxt is not None:
            tmp = nxt.next
            nxt.next = cur
            cur, nxt = nxt, tmp
            
        return cur
    
        # 다른 솔루션 참고. 더 간단한 버전!
        # prev, cur = None, head
        
        # while cur is not None:
        #     tmp = cur.next
        #     cur.next = prev
        #     prev, cur = cur, tmp
            
        # return prev