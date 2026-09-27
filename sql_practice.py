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