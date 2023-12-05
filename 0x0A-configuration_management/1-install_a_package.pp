#!/usr/bin/pup
# Install an especific version of flask (2.1.0)

package { 'python3-pip':
  ensure => installed,
}

package { 'libffi-dev':
  ensure => installed,
}

exec { 'install_dependencies':
  command => '/usr/bin/pip3 install -U setuptools wheel',
  path    => ['/usr/bin'],
  require => Package['python3-pip'],
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  require => [Package['python3-pip'], Package['libffi-dev'], Exec['install_dependencies']],
}
