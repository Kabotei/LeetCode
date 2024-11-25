#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.liste = []

    def push(self, x: int) -> None:
        self.liste.append(x)

    def pop(self) -> int:
        top = self.top()
        self.liste = self.liste[0:len(self.liste)-1]
        return top
        

    def top(self) -> int:
        return self.liste[-1]
        

    def empty(self) -> bool:
        return self.liste == []
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

