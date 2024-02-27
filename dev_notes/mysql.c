MySQL

brew services start mysql
mysql_secure_installation


password Seagull221@

Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.
Y

did not remove test db

login
mysql -u root -p

# pji_dev_shop_db
mysql> CREATE DATABASE pji_dev_shop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
