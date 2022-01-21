# Create a custom HTTP header response
exec { 'update':
  command  => 'apt-get update',
  provider => shell,
}

exec { 'nginx':
  command  => 'apt-get -y install nginx',
  provider => shell,
}

exec { 'header':
  command  => 'sed -i "/server_name _;/server_name _;\n\tadd_header X-Served-By "\$HOSTNAME";/" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'start':
  command  => 'service nginx restart',
  provider => shell,
}
