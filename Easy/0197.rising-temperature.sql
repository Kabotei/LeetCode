--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--

-- @lc code=start
# Write your MySQL query statement below
select w1.id
from Weather w1, Weather w2
where w1.temperature > w2.temperature
    AND DATEDIFF(w1.recordDate ,w2.recordDate) = 1;
-- @lc code=end

