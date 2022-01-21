# Configure an Nginx server
package { 'nginx':
  ensure => 'installed',
}

exec { 'config':
  command  => 'sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default',
  provider => 'shell',
}

exec { 'start':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
