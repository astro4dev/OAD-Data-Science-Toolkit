# SQL

Below is a short and very basic introduction on how to create and populate a SQL database.

SQL is a declarative computer language aimed at querying a relational database. MySQL is relational database managment system, in other words, a piece of software used to submit SQL queries (such as create, modify and delete data).

First we need to open up a terminal and install MySQL:

```sh
sudo apt-get install mysql-server
```

Choose a password (ideally a new password you've not used before)

<p align="center"><img src="img/configuration.png"/></p>

Confirm the password.

Now we launch MySQL

```sh
user@machine:~$ mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 43
Server version: 5.5.54-0+deb8u1 (Debian)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

Let's create the database

```sql
/* Comments in SQL are written like this
for multi line comments */
-- For single line comments the double dash is used.
-- To create a database we type
CREATE DATABASE bd_database;
-- TO tell the server we want to use our new database we write
USE bd_database;
```
Say you want to delete the database. To do this you would DROP it.

```sql
DROP DATABASE bd_database;
```

Databases are made up of tables. So next we have to create a table. We give the entire table a name, then proceed to give the columns names and specify the datatype. You can find a list of datatypes <a href="https://www.w3schools.com/Sql/sql_datatypes_general.asp" target="_blank">here</a>.
```sql
CREATE TABLE brown_dwarfs(
bd_name VARCHAR(255),
bd_spectral_type VARCHAR(255),
temperature REAL
);
```

Now that the table has been created we need to add some data (it would be empty otherwise).
```sql
INSERT INTO brown_dwarfs(
bd_name, bd_spectral_type, temperature)
VALUES(
'Hot BD','L','1800');
```


Let's make sure we have an entry in our database now.
```sql
SELECT * FROM brown_dwarfs;
```
Let's go ahead an add a few more entries:
```sql
INSERT INTO brown_dwarfs(
bd_name, bd_spectral_type, temperature)
VALUES(
'Temperate BD','T','1400');
INSERT INTO brown_dwarfs(
bd_name, bd_spectral_type, temperature)
VALUES(
'Cold BD','Y','800');
INSERT INTO brown_dwarfs(
bd_name, bd_spectral_type, temperature)
VALUES(
'Not a BD','A5','5600');
```

Let's look at the table now:
```sql
SELECT * FROM brown_dwarfs;
```
We notice that an A-type star has been added to our table. Let's get rid of it!
```sql
DELETE FROM brown_dwarfs WHERE temperature > '1800';
```
If we really want to unleash havoc and start deleting columns we would write:
```sql
ALTER TABLE brown_dwarfs DROP COLUMN bd_spectral_type;
```
To add it back we would write:
```sql
ALTER TABLE brown_dwarfs ADD COLUMN bd_spectral_type VARCHAR(255);
```

Notice however, that we have a table filled with NULL values:
```sh
mysql> SELECT * FROM brown_dwarfs;
+--------------+-------------+------------------+
| bd_name      | temperature | bd_spectral_type |
+--------------+-------------+------------------+
| Hot BD       |        1800 | NULL             |
| Temperate BD |        1400 | NULL             |
| Cold BD      |         800 | NULL             |
+--------------+-------------+------------------+
3 rows in set (0.00 sec)
```

So we have to add in the values again:
```sql
UPDATE brown_dwarfs SET bd_spectral_type = 'L' WHERE bd_name = 'Hot BD';
UPDATE brown_dwarfs SET bd_spectral_type = 'T' WHERE bd_name = 'Temperate BD';
UPDATE brown_dwarfs SET bd_spectral_type = 'Y' WHERE bd_name = 'Cold BD';
```

The <a href="https://www.w3schools.com/sql/default.asp" target="_blank">w3schools website</a> is a good reference for further building and editing your table.