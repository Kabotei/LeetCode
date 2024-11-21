--
-- @lc app=leetcode id=183 lang=mysql
--
-- [183] Customers Who Never Order
--

-- @lc code=start
# Write your MySQL query statement below
SELECT Customers.name AS Customers
FROM Customers
LEFT OUTER JOIN Orders ON Customers.id=Orders.customerId
WHERE Orders.customerId IS NULL

-- @lc code=end

