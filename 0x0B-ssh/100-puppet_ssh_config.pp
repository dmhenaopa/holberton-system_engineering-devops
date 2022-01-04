# Manifest to set up client SSH configuration
class { 'ssh::server':
  options                    => {
    'PasswordAuthentication' => 'no',
    'IdentityFile'           => '~/.ssh/school',
  },
}
