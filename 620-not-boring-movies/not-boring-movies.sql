# Write your MySQL query statement below

-- select * from cinema where id % 2 <> 0 and description <> "boring" order by rating desc;


/* Write your PL/SQL query statement below */
-- SELECT * FROM Cinema WHERE MOD( id, 2) = 1 AND 

-- description <> 'boring' ORDER BY rating DESC

-- select * from cinema c
-- where c.id mod 2 > 0 and c.description not in ('boring')
-- order by c.rating desc


select id,movie ,description,rating from cinema WHERE id%2 <> 0 AND description NOT LIKE 'boring'
ORDER BY rating DESC;

