0x09-web_infrastructure_design tasks.
Each task file contains links to the task images.

0-simple_web_stack
A one server web infrastructure that hosts the website that is reachable via www.foobar.com. Contains:
1 server
1 web server (Nginx)
1 application server
1 application files (your code base)
1 database (MySQL)
1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

1-distributed_web_infrastructure
A three server web infrastructure that hosts the website www.foobar.com.
Requirements:
2 servers
1 web server (Nginx)
1 application server
1 load-balancer (HAproxy)
1 set of application files (your code base)
1 database (MySQL)

2-secured_and_monitored_web_infrastructure
design a three server web infrastructure that hosts the website www.foobar.com, it is secured, serve encrypted traffic, and be monitored. Contains:
3 firewalls
1 SSL certificate to serve www.foobar.com over HTTPS
3 monitoring clients (data collector for Sumologic or other monitoring services)

3-scale_up
Improved based on previous design
Contains:
1 server
1 load-balancer (HAproxy) configured as cluster with the other one
Split components (web server, application server, database) with their own server.
