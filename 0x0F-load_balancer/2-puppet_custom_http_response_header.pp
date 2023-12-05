# Define a class for nginx installation and configuration
class nginx_install {
  
  # Install Nginx if not already installed
  package { 'nginx':
    ensure => installed,
  }

  # Update source list
  file { '/etc/apt/sources.list.d/nginx.list':
    ensure  => present,
    content => "deb [arch=amd64 signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] https://nginx.org/packages/ubuntu/ focal nginx\n
                deb-src [arch=amd64 signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] https://nginx.org/packages/ubuntu/ focal nginx\n",
  }

  # Receive signing keys
  exec { 'receive_nginx_keys':
    command     => "sudo gpg --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62",
    refreshonly => true,
  }

  # Export and dearmor keys
  exec { 'export_and_dearmor_keys':
    command => "sudo gpg --export --armor ABF5BD827BD9BF62 | sudo gpg --dearmor -o /usr/share/keyrings/nginx-archive-keyring.gpg",
    require => Exec['receive_nginx_keys'],
  }

  # Update package list
  exec { 'apt_update':
    command => 'sudo apt-get update',
    path    => '/usr/bin',
  }

  # Install nginx
  exec { 'install_nginx':
    command => 'sudo apt-get install -y nginx',
    unless  => 'command -v nginx',
    require => [Exec['export_and_dearmor_keys'], Exec['apt_update']],
  }
}

# Define a class for nginx directory and file creation
class nginx_configure {

  # Make directories with appropriate permission
  file { ['/var/run/nginx', '/var/www/html', '/etc/nginx/sites-available/', '/etc/nginx/sites-enabled/']:
    ensure => directory,
    mode   => '0755',
  }

  # Change ownership of /var/log/nginx
  file { '/var/log/nginx':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    recurse => true,
  }

  # Create a default HTML page with "Hello World!"
  file { '/var/www/html/index.html':
    ensure  => present,
    content => 'Hello World!',
  }

  # Create a custom 404 page
  file { '/var/www/html/404.html':
    ensure  => present,
    content => "Ceci n'est pas une page",
  }

  # Ensure nginx is listening on port 80
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    source  => 'puppet:///modules/nginx_configure/default_custom_http_header',
    notify  => Exec['reload_nginx'],
  }

  # Create a symbolic link
  file { '/etc/nginx/sites-enabled/default':
    ensure => link,
    target => '/etc/nginx/sites-available/default',
    notify => Exec['reload_nginx'],
  }

  # Reload nginx configuration
  exec { 'reload_nginx':
    command => 'sudo nginx -s reload',
    refreshonly => true,
  }
}

# Include the classes in the main manifest
class { 'nginx_install': }
class { 'nginx_configure': }
