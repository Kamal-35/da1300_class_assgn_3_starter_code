from typing import Optional


class TreeNode:
    """Binary tree node for the org chart."""
    def __init__(self, salary=0, left=None, right=None):
        self.salary = salary
        self.left = left
        self.right = right

    def soan(self):
        if self.left==None and self.right!=None:
            return self.salary + self.right.soan()
        elif self.left!=None and self.right==None:
            return self.salary + self.left.soan()
        elif self.left==None and self.right==None:
            return self.salary
        else:
            return self.salary+self.left.soan()+self.right.soan()

    def nu(self):
        if self.left==None and self.right!=None:
            return 1 + self.right.nu()
        elif self.left!=None and self.right==None:
            return 1 + self.left.nu()
        elif self.left==None and self.right==None:
            return 1
        else:
            return 1+self.left.nu()+self.right.nu()

    def averager(self):
        return self.soan()//self.nu()


def count_fair_managers(root: Optional[TreeNode]) -> int:
    """
    Problem 3: Fair managers in an org chart.

    Given the root of a binary tree where each node has a `salary`,
    count the number of nodes whose salary equals the floor-division
    average salary of their entire subtree (including themselves).

    Args:
        root: root TreeNode of the org chart (or None for empty chart).

    Returns:
        Number of fair managers in the tree.
    """
    if root.salary==root.averager():
        rc=1
    else:
        rc=0
    if root.left==None and root.right!=None:
        return rc + count_fair_managers(root.right)
    elif root.left!=None and root.right==None:
        return rc+count_fair_managers(root.left)
    elif root.left==None and root.right==None:
        return rc
    else:
        return rc+count_fair_managers(root.left)+count_fair_managers(root.right)


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    # root = [1] -> a single employee is trivially a fair manager
    root = TreeNode(1)
    print(count_fair_managers(root))  # expected: 1
