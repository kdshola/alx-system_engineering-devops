
0-block_all_incoming_traffic_but
Bash script that Configures ufw so that it blocks all incoming traffic, except the following TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)

100-port_forwarding
Ufc confinguration file that configures web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
