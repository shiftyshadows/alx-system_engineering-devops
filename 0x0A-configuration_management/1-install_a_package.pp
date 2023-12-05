#!/usr/bin/pup
# Install a specific version of flask (2.1.0)

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

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.0.3',
  path    => ['/usr/bin'],
  require => [Package['python3-pip'], Package['libffi-dev'], Exec['install_dependencies']],
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  require => [Package['python3-pip'], Package['libffi-dev'], Exec['install_dependencies'], Exec['install_werkzeug']],
}
