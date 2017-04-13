# scrapy
一:for scrapy_example配置信息
1、需要配置settings的mysql connect,根据自己环境来配置
cd scrapy/scrapy_example/scrapy_example/
vi settings.py
# configure mysql connect
MYSQL_HOST = ''
MYSQL_PORT =
MYSQL_USER = ''
MYSQL_PASSWORD =''
MYSQL_DB = '' 

2、创建数据库和表(以下我环境的配置,数据库名字可以不一致，表名字建议一样，这样代码就不要修改)
> show create database scrapy;
+----------+--------------------------------------------------------------------+
| Database | Create Database                                                    |
+----------+--------------------------------------------------------------------+
| scrapy   | CREATE DATABASE `scrapy` /*!40100 DEFAULT CHARACTER SET utf8mb4 */ |
+----------+--------------------------------------------------------------------+
1 row in set (0.00 sec)

> show create table resource;
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table    | Create Table                                                                                                                                                                  |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| resource | CREATE TABLE `resource` (
  `title` varchar(200) DEFAULT NULL,
  `link` varchar(200) DEFAULT NULL,
  `desc` varchar(800) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)


二:for scrapy_doubantop250配置信息
1、需要配置settings的mysql connect,根据自己环境来配置
cd scrapy/scrapy_doubantop250/scrapy_doubantop250/
vi settings.py
# configure mysql connect
MYSQL_HOST = ''
MYSQL_PORT =
MYSQL_USER = ''
MYSQL_PASSWORD =''
MYSQL_DB = ''

2、创建数据库和表(以下我环境的配置,数据库名字可以不一致，表名字建议一样，这样代码就不要修改)
> show create database scrapy;
+----------+--------------------------------------------------------------------+
| Database | Create Database                                                    |
+----------+--------------------------------------------------------------------+
| scrapy   | CREATE DATABASE `scrapy` /*!40100 DEFAULT CHARACTER SET utf8mb4 */ |
+----------+--------------------------------------------------------------------+
1 row in set (0.00 sec)

> show create table movie;
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| movie | CREATE TABLE `movie` (
  `name` varchar(50) DEFAULT NULL,
  `rank` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+

