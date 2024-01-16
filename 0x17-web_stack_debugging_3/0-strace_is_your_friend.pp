# Fis server error on apache LAMP server

exec { 'fix get error':
provider => shell,
command  => 'sudo sed -i s/phpp/php/g /var/www/html/wp-settings.php'
}
