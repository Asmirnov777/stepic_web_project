mysql -uroot -p -e "create database ask_db;" # На виртуальной машине - без -p!
mysql -uroot -p -e "create user 'box' identified by 'box';" # На виртуальной машине - без -p!
mysql -uroot -p -e "grant all privileges on ask_db.* to 'box';" # На виртуальной машине - без -p!
mysql -uroot -p -e "flush privileges;" # На виртуальной машине - без -p!

sudo apt-get install libmysqlclient-dev #только на локальной машине!
sudo pip3 install mysqlclient #только на локальной машине!

sudo python3 -m pip install django==2.0 #только на виртуальной машине!

sudo /etc/init.d/mysql start
python3 ./manage.py makemigrations qa
python3 ./manage.py migrate
