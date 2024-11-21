--
-- @lc app=leetcode id=196 lang=mysql
--
-- [196] Delete Duplicate Emails
--

-- @lc code=start
# Write your MySQL query statement below
Delete p1
from Person p1, Person p2
where p1.id>p2.id AND p1.email=p2.email
-- @lc code=end

