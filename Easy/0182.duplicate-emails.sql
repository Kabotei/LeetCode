# Write your MySQL query statement below
Select email as Email
from person
group by email
having count(Email) >1;