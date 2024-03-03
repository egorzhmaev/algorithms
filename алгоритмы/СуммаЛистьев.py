class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Выводит родителя до всех его потомков
def sum_leafs(tree):
    if tree is None:
        return 0

    if tree.right and tree.left:
        sum_leafs(tree.right)
        sum_leafs(tree.left)

    elif tree.right or tree.left:
        if tree.right:
            sum_leafs(tree.right)
        elif tree.left:
            sum_leafs(tree.left)

    elif not tree.right and not tree.left:
        return tree.value

    return sum_leafs(tree.right) + sum_leafs(tree.left)

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

print(sum_leafs(tree))

#Прямой, Обратный и Центрированный