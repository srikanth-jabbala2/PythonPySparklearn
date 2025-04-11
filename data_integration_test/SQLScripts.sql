use sqlpractice;

create table target_table (
    id int,
    name varchar(50),
    age int,
    city varchar(50)
)

insert into target_table (id, name, age, city) values
(1, 'Alice', 30, 'New York'),
(2, 'Bob', 25, 'Los Angeles'),
(3, 'Charlie', 35, 'Chicago'),
(4, 'Diana', 28, 'Houston')


select * from target_table

select * from employee
