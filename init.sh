sudo rm /etc/nginx/sites-enabled/default #2> /dev/null
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
gunicorn --bind='0.0.0.0:8080' hello:divide_params -D
sudo /etc/init.d/nginx restart
