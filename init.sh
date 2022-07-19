sudo rm /etc/nginx/sites-enabled/default #2> /dev/null
sudo ln -sf ./etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
gunicorn --bind='0.0.0.0:8080' hello:divide_params -D
gunicorn -c ./etc/qa_conf.py ask.wsgi:application -D
sudo /etc/init.d/nginx restart

#git clone https://github.com/<your_account>/stepic_web_2_1 /home/box/web
#bash /home/box/web/init.sh
