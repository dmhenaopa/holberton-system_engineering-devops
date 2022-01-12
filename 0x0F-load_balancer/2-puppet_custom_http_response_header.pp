# Creating a custom HTTP header response
package { 'ngnix':
  ensure => 'present',
}

exec { 'sed':
  command => "sed -i 's/server_name _;/server_name _;\n\n\tadd_header X-Served-By '${HOSTNAME}' always;/'",
  path    => '/etc/nginx/sites-available/default',
}

exec { 'restart':
  command => 'sudo service nginx restart',
}
