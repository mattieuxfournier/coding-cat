def check_id(l1, l2, target) -> bool:
    """
    Bug: Only checks target in first list
    """
    for i, value in enumerate(l1):
        if value == target:
            return True
    return False
