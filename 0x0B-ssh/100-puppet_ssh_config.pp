# Manifest to set up client SSH configuration
exec { 'change authentication':
  command  => 'sed -i "s/#   PasswordAuthentication yes/PasswordAuthentication no\nIdentityFile ~/.ssh/school/" /etc/ssh/ssh_config',
  provider => 'shell'
}
