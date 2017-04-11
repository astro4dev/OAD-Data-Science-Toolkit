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
CREATE DATABASE my_database;
```
