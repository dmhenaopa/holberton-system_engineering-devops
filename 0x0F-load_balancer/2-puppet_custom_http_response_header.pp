# Create a custom HTTP header response
package { 'nginx':
  ensure => 'installed',
}

exec { 'response':
  command  => 'sed -i "s/server_name _;/server_name _;\n\n\tadd_header X-Served-By "$HOSTNAME" always;/" /etc/nginx/sites-available/default',
  provider => 'shell',
}

exec { 'start':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
