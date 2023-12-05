#!/usr/bin/pup
# Define a class for configuring the custom HTTP header
class custom_http_response_header {
  
  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Create custom Nginx configuration file
  file { '/etc/nginx/sites-available/0-custom_http_response_header':
    content => '
server {
    listen 80;
    server_name _;

    location / {
        add_header X-Served-By $host;
        # Additional configuration if needed
    }

    # Additional server blocks or configuration if needed
}
',
    notify  => Service['nginx'],
  }

  # Create a symbolic link
  file { '/etc/nginx/sites-enabled/0-custom_http_response_header':
    ensure => link,
    target => '/etc/nginx/sites-available/0-custom_http_response_header',
  }

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => File['/etc/nginx/sites-available/0-custom_http_response_header'],
  }
}

# Include the custom_http_response_header class
include custom_http_response_header
