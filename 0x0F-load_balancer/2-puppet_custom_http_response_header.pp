# Create a custom HTTP header response
exec { 'update':
  command => 'sudo apt-get update',
  provider => 'shell',
}

package { 'nginx':
  ensure => 'installed',
}

file { 'index.nginx-debian.html':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World',
}

exec { 'config':
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default',
  provider => 'shell',
}

exec { 'header':
  command  => 'sudo sed -i "22i add_header X-Served-By "\$HOSTNAME" always;" /etc/nginx/nginx.conf',
  provider => 'shell',
}

exec { 'start':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
