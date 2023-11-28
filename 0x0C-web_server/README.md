0-transfer_file
A Bash script that transfers a file from our client to a server:
Accepts 4 parameters
1 The path to the file to be transferred
2 The IP of the server we want to transfer the file to
3 The username scp connects with
4 The path to the SSH private key that scp uses

1-install_nginx_web_server
Install and configure an Nginx server using Bash. Performsa 301 redirect when querying /redirect_me on my server. And return a page that contains the string Hello World! with a GET request (requesting a page) using curl on my sebserver.

2-setup_a_domain_name
contains my domain name.

3-redirection
Configure my Nginx server so that /redirect_me is redirecting to another page.

4-not_found_page_404
Configure my Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

7-puppet_install_nginx_web_server.pp
Install and configure an Nginx server using Puppet instead of Bash. Performsa 301 redirect when querying /redirect_me on my server. And return a page that contains the string Hello World! with a GET request (requesting a page) using curl.
