sudo rm /etc/nginx/sites-enabled/default #2> /dev/null
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
gunicorn --bind='0.0.0.0:8080' hello:divide_params -D
gunicorn -c /home/box/web/etc/qa_conf.py ask.wsgi:application -D
sudo /etc/init.d/nginx restart

#sudo pip3 install django==2.0
#git clone https://github.com/<your_account>/stepic_web_project /home/box/web
#cd /home/box/web/ask/
#bash /home/box/web/init.sh
