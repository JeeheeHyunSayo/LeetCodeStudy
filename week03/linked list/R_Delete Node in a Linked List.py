'''
Q. single-linked list에서 주어진 노드 삭제하기
A.
    1. 이전 노드의 next변경 2. 현재 노드를 현재.next로 변경 두 가지 방법이 있으나 이 문제에서는 현재노드의 head를 모르므로 2번 방법 사용
    -> 현재 노드가 가진 값을 현재.next로 변경하여 자동으로 건너뛰게 됨
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next
        