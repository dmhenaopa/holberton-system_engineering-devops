#!/usr/bin/env bash
# Create a custom HTTP header response
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

exec { 'nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'header':
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$HOSTNAME;/" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'start':
  command  => 'sudo service nginx restart',
  provider => shell,
}
