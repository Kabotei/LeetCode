--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
# Write your MySQL query statement below
Select name as Employee
From Employee E1
Where salary > (
    Select salary
    From Employee E2
    Where E2.id = E1.managerID);
-- @lc code=end

