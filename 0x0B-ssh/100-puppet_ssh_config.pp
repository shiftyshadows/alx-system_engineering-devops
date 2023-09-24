# ssh_config.pp

file { '/home/ubuntu/.ssh/config':
  ensure => present,
  mode   => '0600',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  content => "\
Host 52.205.222.84
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
"
}
