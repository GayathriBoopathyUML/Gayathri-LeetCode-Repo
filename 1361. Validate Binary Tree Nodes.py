class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # L = [i for i in leftChild if i != -1]
        # R = [i for i in rightChild if i != -1]
        # print(L,R)
        # return not len(list(set(L)&set(R)))>0
        node_count = n
        left_children = leftChild
        right_children = rightChild
        def find_root(x: int) -> int:
            if parents[x] != x:
                parents[x] = find_root(parents[x])
            return parents[x]

        parents = list(range(node_count))
        visited = [False] * node_count

        for i, (left_child, right_child) in enumerate(zip(left_children, right_children)):
            for child in (left_child, right_child):
                if child != -1:
                    if visited[child] or find_root(i) == find_root(child):
                        return False
                    parents[find_root(i)] = find_root(child)
                    visited[child] = True
                    node_count -= 1

        return node_count == 1