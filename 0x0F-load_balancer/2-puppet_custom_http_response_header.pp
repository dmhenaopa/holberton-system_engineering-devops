#!/usr/bin/env bash
# Create a custom HTTP header response
exec { 'update':
  command  => 'sudo apt-get update; 
               sudo apt-get -y install nginx;
	       sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$HOSTNAME;/" /etc/nginx/sites-available/default;
	       sudo service nginx restart',
  provider => shell,
}
