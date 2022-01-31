create table X as select 20 as X;
with ints(n) as (select 1 union select n+1 from ints, X where n < X)
select n, (X - n) / n from ints, X
    where ((X - n) / n) >= 3;

create table reviews as
    select "Barney's" as restaurant, "Albert" as user, 4 as stars, "Used to like it" as review union
    select "Chipotle"       "Robert"    5   "BOGO! BOGO!"           union
    select "Eureka"         "Albert"    5   "My favorite!"          union
    select "Bongo Burger"   "Albert"    2   "When I'm desperate"    union
    select "Umami Burger"   "Albert"    5   "I love truffle fries!";
 
select stars, count(*) as "number of reviews" from reviews
    where user = "Albert"
    group by stars;