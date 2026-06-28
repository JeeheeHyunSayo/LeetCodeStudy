'''
Q. 뒤에서 n번째 노드 삭제하기
A. 투 포인터 사용하여 뒤에서 n번째 위치 찾기
    1. head를 가리키는 dummy 생성
    2. fast를 slow보다 n만큼 먼저 이동
    3. fast가 끝에 도달할 때 slow.next가 삭제해야하는 노드
    4. slow.next를 변경
    5. dummy.next 반환 (head가 삭제되는 경우 대비)

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast, slow = dummy, dummy
        while n:
            fast = fast.next
            n -= 1
        
        while fast.next:
            fast, slow = fast.next, slow.next
            
        slow.next = slow.next.next

        return dummy.next