from typing import List


def surviving_ships(ships: List[int]) -> List[int]:
    """
    Problem 2: Spaceship collisions.

    Given a list of ship engine powers (sign = direction: positive is
    right, negative is left), resolve all collisions between ships
    moving toward each other and return the engine powers (with sign)
    of the ships that remain.

    Args:
        ships: list of signed engine powers.

    Returns:
        List of signed engine powers of surviving ships, left to right.
    """
    #i borrowed idea of using stacks(underlying storage is list ofcourse) from akshith
    r,l=[],[]
    for i in ships:
        flag=None
        if i>0:
            r.append(i)
        else:
            while r!=[]:
                if r[-1]>abs(i):
                    break
                elif r[-1]<abs(i):
                    del r[-1]
                else:
                    flag=True
                    break
            if flag:
                del r[-1]
            if r==[] and flag==None:
                l.append(i)
    return l+r


if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8, -8]))     # expected: []
    print(surviving_ships([3, 2, 1, -1, -2, -3, 7, -7, -1]))