sudo rm /etc/nginx/sites-enabled/default 2> /dev/null
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
