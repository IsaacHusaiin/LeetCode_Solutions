# Write your MySQL query statement below
select
    p.product_name , S.year, S.price
from sales S
join product p on s.product_id = p.product_id