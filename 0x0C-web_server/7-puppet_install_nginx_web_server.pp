# Install and confiture an Nginx server

exec { 'install and configure':
command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; sudo ufw allow 'Nginx HTTP'; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html; sudo sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/ permanent;" /etc/nginx/sites-available/default; sudo service nginx start',
provider => shell
}
