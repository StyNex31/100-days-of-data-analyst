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


# gay 16


# SELECT name, grade,
#        RANK() OVER (ORDER BY grade DESC) AS rank
# FROM students;

# SELECT name, grade,
#        ROW_NUMBER() OVER (ORDER BY grade DESC) AS row_num
# FROM students;

# SELECT name, city, grade,
#        RANK() OVER (PARTITION BY city ORDER BY grade DESC) AS rank
# FROM students;

# day 17

# SELECT name, grade,
#        LEAD(grade) OVER (ORDER BY grade DESC) AS next_grade
# FROM students;

# SELECT name, grade,
#        grade - LAG(grade) OVER (ORDER BY grade DESC) AS grade_difference
# FROM students;
#
# SELECT name, city, grade,
#        SUM(grade) OVER (PARTITION BY city ORDER BY grade DESC) AS running_total_by_city
# FROM students;

# day 18

# SELECT
#     strftime('%Y-%m', date) AS month,
#     SUM(qty * price) AS total_revenue
# FROM sales
# GROUP BY month
# ORDER BY month;

# SELECT
#     strftime('%Y-%m', date) AS month,
#     branch,
#     SUM(qty * price) AS total_revenue
# FROM sales
# GROUP BY month, branch
# ORDER BY month, total_revenue DESC;

# 2026-09	Центр	139000   # Спад зароботка спал в филлиале центр на 48,8%(67,800). Упал инетерес к филлиалу или
# 2026-09	Север	109100   # Упало качество работы нужна проверка месяца качества работы и соцсетей можно провести опрос
# 2026-10	Север	97000    # либо начать небольшой ивент или акцию для привлечения новых клиетов или вернуть старых
# 2026-10	Центр	71200    # для более точного или обширного решения необходимо больше данных и вводных деталий

# SELECT
#     strftime('%Y-%m', date) AS month,
#     product,
#     SUM(qty * price) AS product_revenue
# FROM sales
# WHERE branch = 'Центр'
# GROUP BY month, product
# ORDER BY month, product_revenue DESC;

# 2026-09	Латте	48000      # Падение на -45,0%
# 2026-09	Капучино	38500  # Падение на -42,9%
# 2026-09	Чизкейк	30000      # Падение на -60,0%
# 2026-09	Круассан	22500  # падение на -52,0%
# 2026-10	Латте	26400      #
# 2026-10	Капучино	22000  #
# 2026-10	Чизкейк	12000      #
# 2026-10	Круассан	10800  #
# Итого упало на 67800 (48.8% выручка)

# 2026-09	Латте	36000      # Рост на 3,3%
# 2026-09	Капучино	30800  # Рост на 3,6%
# 2026-09	Чизкейк	22500      # Падение на 4,5%
# 2026-09	Круассан	19800  # Падение на 60,0%
# 2026-10	Латте	37200      #
# 2026-10	Капучино	31900  #
# 2026-10	Круассан	18900  #
# 2026-10	Чизкейк	9000       #
# Итого упало на 12100 (11.1% выручка)



























