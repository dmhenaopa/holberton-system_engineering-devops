# Manifest to set up client SSH configuration
exec { 'change authentication':
  command  => 'echo "    PasswordAuthentication no\n    IdentityFile ~/.ssh/school/" >> /etc/ssh/ssh_config',
  provider => 'shell'
}
