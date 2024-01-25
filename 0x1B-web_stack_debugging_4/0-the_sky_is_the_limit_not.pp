# Increases the amount of traffic an Nginx server can handle.

exec { 'set-limit':
  command  => 'sudo sed -i "s/15/4096/" /etc/default/nginx',
  provider => shell,
}

# Restart Nginx
-> exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
