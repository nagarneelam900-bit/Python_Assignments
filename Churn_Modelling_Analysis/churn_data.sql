CREATE DATABASE Churn_Modeling;
Use Churn_Modeling;
Create Table churn_data(
rnum Int Primary Key auto_increment,
cid Int ,
sname varchar(100),
cscore Int,
geography varchar(100),
gender varchar(100),
age Int,
tenure Int,
balance decimal(10,2),
no_products Int,
hascrcard Int,
isactivemember Int,
estimated_Salary decimal(10,2),
exited Int
);
Select * from churn_data;

Select count(*) from churn_modeling.churn_data;

Select Distinct count(*) from churn_modeling.churn_data;

Select Distinct * from churn_modeling.churn_data;

SELECT * FROM churn_data WHERE rnum = 1;

SELECT CustomerID, COUNT(*)
FROM churn_data
GROUP BY CustomerID
HAVING COUNT(*) > 1;

Drop Table churn_data;

TRUNCATE TABLE churn_data;