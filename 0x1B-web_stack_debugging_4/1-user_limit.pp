# Enable the user holberton to login and open files without error.

exec { 'hard-limit':
  command => 'sudo sed -i "s/nofile 5/nofile 35000/" /etc/security/limits.conf',
provider  => shell,
}

exec { 'soft-limit':
  command  => 'sudo sed -i "s/nofile 4/nofile 35000/" /etc/security/limits.conf',
  provider => shell,
}
