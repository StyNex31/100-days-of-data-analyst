# -- День 9: создание таблицы и добавление данных
# CREATE TABLE students (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     grade INTEGER
# );
#
# INSERT INTO students (name, grade) VALUES ('Тимур', 85);
# INSERT INTO students (name, grade) VALUES ('Алина', 92);
# INSERT INTO students (name, grade) VALUES ('Данияр', 67);
#
# -- фильтр по оценке
# SELECT name FROM students WHERE grade > 80;
#
# -- сортировка
# SELECT * FROM students ORDER BY grade DESC;
#
# -- добавление колонки и обновление данных
# ALTER TABLE students ADD COLUMN city TEXT;
# UPDATE students SET city = 'Алматы' WHERE name = 'Тимур';
# UPDATE students SET city = 'Астана' WHERE name = 'Алина';
# UPDATE students SET city = 'Талдыкорган' WHERE name = 'Данияр';
#
# -- группировка по городу
# SELECT city, AVG(grade) FROM students GROUP BY city;




# -- День 12: сортировка результата группировки
#
# SELECT city, AVG(grade) FROM students GROUP BY city
# ORDER BY AVG(grade) DESC;





# -- День 12: создание таблицы cities и JOIN со students
#
# CREATE TABLE cities (
#     city TEXT,
#     population INTEGER
# );
#
# INSERT INTO cities (city, population) VALUES ('Алматы', 2000000);
# INSERT INTO cities (city, population) VALUES ('Астана', 1200000);
# INSERT INTO cities (city, population) VALUES ('Талдыкорган', 300000);
#
# -- JOIN: имя студента, оценка, население его города
# SELECT students.name, students.grade, cities.population
# FROM students
# JOIN cities ON students.city = cities.city;
#
# -- JOIN + GROUP BY: средняя оценка по городу + население города
# SELECT students.city, AVG(students.grade), cities.population
# FROM students
# JOIN cities ON students.city = cities.city
# GROUP BY students.city;



# День 13

# SELECT students.name, cities.city
# FROM students
# JOIN cities ON students.city = cities.city
# WHERE cities.population > 1000000;

# SELECT
#     cities.city,
#     cities.population,
#     COUNT(students.id) AS student_count
# FROM cities
# JOIN students ON cities.city = students.city
# GROUP BY cities.city, cities.population;




# ДЕНЬ 14

# SELECT name FROM students
# WHERE grade > (SELECT AVG(grade) FROM students);


# SELECT city, population
# FROM cities
# WHERE population > (SELECT AVG(population) FROM cities);



# День 15

# SELECT city FROM cities
# WHERE city IN (SELECT city FROM students WHERE grade > 90);

# SELECT city FROM cities
# WHERE city IN (SELECT city FROM students WHERE grade < 70);

# SELECT name, grade
# FROM students
# WHERE grade = (SELECT MAX(grade) FROM students);

# SELECT city
# FROM cities
# WHERE population = (SELECT MAX(population) FROM cities);






