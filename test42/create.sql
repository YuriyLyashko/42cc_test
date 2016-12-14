create database test42  CHARACTER SET utf8 COLLATE utf8_general_ci;
create user 'test42'@'localhost' identified by 'q';
grant all privileges on test42.* to 'test42'@'localhost';