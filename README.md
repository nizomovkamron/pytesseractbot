"# pytesseractbot" 
commands for install mysql in Ubuntu:

sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
mysql_install_db
mysqld –initialize
sudo mysql
SELECT user,authentication_string,plugin,host FROM mysql.user;
ALTER USER
'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
SELECT user,authentication_string,plugin,host FROM mysql.user;
exit
