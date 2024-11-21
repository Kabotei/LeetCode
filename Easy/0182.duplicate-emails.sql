--
-- @lc app=leetcode id=182 lang=mysql
--
-- [182] Duplicate Emails
--

-- @lc code=start
# Write your MySQL query statement below
Select email as Email
from person
group by email
having count(Email) >1;

-- @lc code=end

