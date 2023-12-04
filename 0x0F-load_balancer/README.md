This task is to install and configure an HAproxy server for load balancing

0-custom_http_response_header
configures a brand new Ubuntu machine to the requirements
that its HTTP response contains a custom header
The name of the custom HTTP header must be X-Served-By
The value of the custom HTTP header must be the hostname of the server Nginx is running on

1-install_load_balancer
Installs and configure HAproxy on my lb-01 server.
It  sends traffic to web-01 and web-02
Distribute requests using a roundrobin algorithm
Make sure that HAproxy can be managed via an init script

2-puppet_custom_http_response_header.pp
Automate the task of creating a custom HTTP header response, but with Puppet.
