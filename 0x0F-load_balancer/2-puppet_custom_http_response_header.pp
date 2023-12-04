# Automates the task of creating a custom HTTP header response.
exec { 'custom HTTP header':
command  => 'sudo apt-get -y update;
sudo apt-get -y install nginx;
sudo sed -i "/listen [::]:80 default_server;/a \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
sudo service nginx restart',
provider => shell,
}
