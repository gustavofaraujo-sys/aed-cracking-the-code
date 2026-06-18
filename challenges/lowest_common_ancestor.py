from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:
    if root is None:
        return None
    
    if root.value == value1 or root.value == value2:
        return root.value
    
    left = lowest_common_ancestor(root.leftm value1, value2)

    right = lowest_common_ancestor(root.right, value1, value2)

    if left is not None and right is not None:
        return root.value
    
    if left is not None:
        return left
    
    return right
