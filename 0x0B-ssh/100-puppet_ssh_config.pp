# Manifest to set up client SSH configuration
class { 'ssh':
  server_options => {
    'Match User ubuntu' => {
      'PasswordAuthentication' => 'no',
      'IdentityFile'           => '~/.ssh/school',
    }
  }
}
