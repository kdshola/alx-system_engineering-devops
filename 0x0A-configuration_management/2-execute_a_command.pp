# kills a process named killmenow with pkill.

exec { 'pkill':
command  => 'pkill killmenow',
provider => 'shell'
}
