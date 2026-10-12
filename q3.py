from typing import Optional


class TreeNode:
    """Binary tree node for the org chart."""
    def __init__(self, salary=0, left=None, right=None):
        self.salary = salary
        self.left = left
        self.right = right

    def ur(self):
        if self.left==None and self.right!=None:
            r=self.right.ur()
            if self.salary==(self.salary+r[0])//(1+r[1]):
                return (self.salary + r[0],1 + r[1],1+r[2])
            else:
                return (self.salary + r[0],1 + r[1],r[2])
        elif self.left!=None and self.right==None:
            l=self.left.ur()
            if self.salary==(self.salary+l[0])//(1+l[1]):
                return (self.salary + l[0],1 + l[1],1+l[2])
            else:
                return (self.salary + l[0],1 + l[1],l[2])
        elif self.left==None and self.right==None:
            return (self.salary,1,1)
        else:
            r=self.right.ur()
            l=self.left.ur()
            if self.salary==(self.salary+l[0]+r[0])//(1+l[1]+r[1]):
                return (self.salary+l[0]+r[0],1+l[1]+r[1],1+l[2]+r[2])
            else:
                return (self.salary+l[0]+r[0],1+l[1]+r[1],l[2]+r[2])


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
    if root in [None,[]]:
        return 0
    else:
        return root.ur()[2]


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    # root = [1] -> a single employee is trivially a fair manager
    root = TreeNode(1)
    print(count_fair_managers(root))  # expected: 1
