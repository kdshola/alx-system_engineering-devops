# set up your client SSH configuration file so that you can connect to a server
# without typing a password.

file_line {'refuse_password_authentication':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => '	PasswordAuthentication no',
}

file_line {'Use particular key':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => '     IdentityFile ~/.ssh/school',
}
