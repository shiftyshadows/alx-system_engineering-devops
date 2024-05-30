#!/usr/bin/env bash

# Update package lists and upgrade installed packages
sudo apt update
sudo apt upgrade -y

# Install essential packages
sudo apt install -y \
    mysql-server \
    mysql-client

# Start MySQL service and enable it on boot
sudo systemctl start mysql
sudo systemctl enable mysql

# Secure MySQL installation (you will be prompted for these settings)
sudo mysql_secure_installation

# Optional: Create a MySQL user and database
read -p "Enter MySQL username: " mysql_user
read -p "Enter MySQL password: " mysql_password
read -p "Enter a name for the new database: " mysql_database

sudo mysql -e "CREATE DATABASE $mysql_database;"
sudo mysql -e "CREATE USER '$mysql_user'@'localhost' IDENTIFIED BY '$mysql_password';"
sudo mysql -e "GRANT ALL PRIVILEGES ON $mysql_database.* TO '$mysql_user'@'localhost';"
sudo mysql -e "FLUSH PRIVILEGES;"

# Display a message indicating the completion of the setup
echo "Linux machine setup with MySQL complete! Please restart your shell for changes to take effect."

# Optionally, you may want to add more configuration steps based on your needs.
