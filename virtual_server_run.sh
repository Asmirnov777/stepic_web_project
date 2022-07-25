git clone https://github.com/<your_account>/stepic_web_project /home/box/web
cd /home/box/web/

sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf ./etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo /etc/init.d/mysql start
mysql -uroot -e "create database ask_db;"
mysql -uroot -e "create user 'box' identified by 'box';" 
mysql -uroot -e "grant all privileges on ask_db.* to 'box';" 
mysql -uroot -e "flush privileges;" 
sudo python3 -m pip install django==2.0
gunicorn --bind='0.0.0.0:8080' hello:divide_params -D 

python3 ./ask/manage.py makemigrations qa
python3 ./ask/manage.py migrate
sudo python3 ./ask/manage.py runserver 0.0.0.0:80

