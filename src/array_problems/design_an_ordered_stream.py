#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1656. Design an Ordered Stream
URL: https://leetcode.com/problems/design-an-ordered-stream/

Description:
There is a stream of n (id, value) pairs arriving in an arbitrary order,
where id is an integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs
by returning a chunk (list) of values after each insertion.
The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:

OrderedStream(int n) Constructs the stream to take n values.
String[] insert(int id, String value) Inserts the pair (id, value) into the stream,
then returns the largest possible chunk of currently inserted values that appear next in the order.

Example:
Input
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

Explanation
Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
OrderedStream os = new OrderedStream(5);
os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].

Concatentating all the chunks returned:
[] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
The resulting order is the same as the order above.

Constraints:

1 <= n <= 1000
1 <= id <= n
value.length == 5
value consists only of lowercase letters.
Each call to insert will have a unique id.
Exactly n calls will be made to insert.

Complexity:
Time: O(N)
Space: O(N)
"""
from typing import List


class OrderedStream:
    def __init__(self, n: int):
        # initialize the pointer and the array
        self.ptr, self.stream, self.n = 1, [""] * n, n

    def insert(self, idx: int, value: str) -> List[str]:
        # store the value on the given idx and store the current pointer
        self.stream[idx - 1], init = value, self.ptr - 1
        # move the pointer forward while the next value is not none and not at the end of the array
        while self.ptr <= self.n and self.stream[self.ptr - 1]:
            self.ptr += 1
        # return every value in between the starting pointer and the current pointer
        return self.stream[init : self.ptr - 1]


if __name__ == "__main__":
    solution = OrderedStream(5)
    assert not solution.insert(3, "ccccc")
    assert solution.insert(1, "aaaaa") == ["aaaaa"]
    assert solution.insert(2, "bbbbb") == ["bbbbb", "ccccc"]
    assert not solution.insert(5, "eeeee")
    assert solution.insert(4, "ddddd") == ["ddddd", "eeeee"]
