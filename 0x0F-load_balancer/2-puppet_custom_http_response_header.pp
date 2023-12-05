#!/usr/bin/pup
# Define a class for configuring the custom HTTP header
class custom_http_response_header {
  
    # Install Nginx package
    package { 'nginx':
        ensure => installed,
    }

    # Create custom Nginx configuration file
    file { '/etc/nginx/sites-available/default':
        content => 'error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;

events {
    # Default event-related configurations
}

http {
    server {
        listen 80;
        server_name 100.26.220.1;

        location /redirect_me {
            return 301 https://www.example.com/;
        }

        location / {
            root /var/www/html/;
            index index.html;
            add_header X-Served-By $host;
        }

        error_page 404 /404.html;
        location = /404.html {
            root /var/www/html;
            internal;
        }
    }
}
',
        notify  => Service['nginx'],
    }

    # Create a symbolic link
    file { '/etc/nginx/sites-enabled/default':
        ensure => link,
        target => '/etc/nginx/sites-available/default',
    }

    # Ensure Nginx service is running and enabled
    service { 'nginx':
        ensure  => running,
        enable  => true,
        require => File['/etc/nginx/sites-available/default'],
    }
}

# Include the custom_http_response_header class
include custom_http_response_header
