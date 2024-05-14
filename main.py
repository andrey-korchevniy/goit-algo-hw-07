class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_max(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val

def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

def sum_tree(root):
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

# Пошук максимального значення
max_val = find_max(root)
print(f"Найбільше значення у дереві: {max_val}")

# Пошук мінімального значення
min_val = find_min(root)
print(f"Найменше значення у дереві: {min_val}")

# Обчислення суми всіх значень
total_sum = sum_tree(root)
print(f"Сума всіх значень у дереві: {total_sum}")