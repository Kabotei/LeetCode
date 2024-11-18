Select name as Employee
From Employee E1
Where salary > (
    Select salary
    From Employee E2
    Where E2.id = E1.managerID);