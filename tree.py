class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self._insert(self.root,data)
        #print(self.root.data)
        return self.root is not None
    def _insert(self,node,val):
        if node is None:#노드가 완전 비어 있을 때
            node=Node(val)#처음 들어온 값이 root가 됨.
        else:
            if val<=node.data:
                node.left=self._insert(node.left,val)
            else:
                node.right=self._insert(node.right,val)
        return node
    def find(self,key):
        return self._find(self.root,key)
    def _find(self,node,key):
        if node is None or node.data==key:
            return node is not None
        elif key<node.data:
            return self._find(node.left,key)
        else:
            return self._find(node.right,key)
    def delete(self,key):
        self.root,deleted=self._delete(self.root,key)
        return deleted
    def _delete(self,node,key):
        if node is None:
            return node,False
        deleted=False
        if key==node.data:#지우려는 값과 일치하는 노드를 찾았다면 지우기 시작.
            deleted=True
            if node.left and node.right:#지우려는 노드의 양쪽에 자식이 있다면
                parent,child=node,node.right#노드의 오른쪽 중에서
                while child.left is not None:#가장 작은 값이 나올 때까지
                    parent,child=child,child.left#왼쪽 자식으로 쭉 이동
                child.left=node.left#가장 작은 값의 왼쪽 자식으로 지우려는 노드의 왼쪽 서브트리 붙이기
                if parent!=node:#가장 작은 값의 부모와 지우려는 값이 다를 때
                    parent.left=child.right#부모의 왼쪽 자식으로 가장 작은 값의 오른쪽 서브트리 붙이기
                    child.right=node.right#가장 작은 값의 오른쪽 서브트리로 지우려는 노드의 오른쪽 서브트리 붙이기
                node=child#지우려는 노드의 자리에 가장 작은 값으로 대체하기
            elif node.left or node.right:#왼쪽 또는 오른쪽 자식만 있는 경우
                node=node.left or node.right#왼쪽만 있으면 지우려는 노드의 자식을 지우려는 노드의 자리로 이동
            else:#자식이 양쪽 다 없다면
                node=None#지우려는 노드를 None으로
        elif key<node.data:#지우려는 값이 현재 노드보다 작다면
            node.left,deleted=self._delete(node.left,key)#노드의 왼쪽으로 이동
        else:#지우려는 값이 현재 노드보다 크다면
            node.right,deleted=self._delete(node.right,key)#노드의 오른쪽으로 이동
        return node,deleted
bst=BST()
arr=[27,14,35,10,19,31,42,31,40,45,36,37,38]
for i in arr:
    bst.insert(i)

print(bst.find(35))
print(bst.delete(35))#True가 나오면 지우려는 값이 트리에 있다는 뜻
print(bst.find(35))