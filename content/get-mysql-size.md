Title: Получить размер базы данных в MySQL
Date: 2017-03-15 15:16
Tags: mysql, sql
Slug: get-mysql-size
Lang: ru
Category: Tips
Authors: shamcode
Summary: SQL запрос для получния размера базы данных в MySQL

SQL запрос для получния размера базы данных в MySQL
```SQL
SELECT
    table_schema "DB Name",
    Round(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB"
FROM
    information_schema.tables
GROUP BY
    table_schema;
```