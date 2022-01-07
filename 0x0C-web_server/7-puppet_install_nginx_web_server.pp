# Configure an Nginx server
exec { 'nginxinstall':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx; service nginx start; echo "Hello World" | sudo tee /var/www/html/index.html; redirect_to="server_name \/redirect_me;\n\treturn 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4; sed -i "s/server_name _;/$redirect_to/" /etc/nginx/sites-available/default; service nginx restart',
  provider => 'shell',
}
