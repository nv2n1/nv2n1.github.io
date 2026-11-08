---
title: "Installing PHP on Apache with Fedora"
date: 2018-03-24 08:14:36 +0000
modified: 2026-04-12 14:18:55 +0000
author: "Q A"
layout: post
categories: [programming-languages]
canonical: /how-to-install-php-on-apache-on-fedora/
---

Setting up PHP with Apache on Fedora involves installing the PHP module, configuring Apache to process PHP files, and verifying the setup works correctly.

## Install PHP and Apache

```wp-block-code
sudo dnf install httpd php php-fpm

# Start and enable Apache
sudo systemctl enable --now httpd

# If using PHP-FPM (recommended for modern Fedora)
sudo systemctl enable --now php-fpm
```

## Configure Apache for PHP

On Fedora, Apache with PHP-FPM requires configuring the proxy:

```wp-block-code
# Create PHP-FPM configuration for Apache
sudo tee /etc/httpd/conf.d/php-fpm.conf > /dev/null << 'EOF'

    SetHandler "proxy:unix:/run/php-fpm/www.sock|fcgi://localhost"


# Enable directory index for PHP
DirectoryIndex index.php index.html
EOF

# Restart Apache
sudo systemctl restart httpd
```

## Configure Firewall

```wp-block-code
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

## Test PHP

```wp-block-code
echo '' | sudo tee /var/www/html/info.php
```

Open `http://localhost/info.php` in a browser. You should see the PHP information page. Remove it after testing:

```wp-block-code
sudo rm /var/www/html/info.php
```

## Install Common PHP Extensions

```wp-block-code
# Database drivers
sudo dnf install php-mysqlnd php-pgsql php-sqlite

# Image processing
sudo dnf install php-gd php-imagick

# XML and JSON
sudo dnf install php-xml php-json

# MBString (multibyte strings, needed by WordPress)
sudo dnf install php-mbstring

# cURL (needed by many APIs and CMS platforms)
sudo dnf install php-curl

# OPcache (performance)
sudo dnf install php-opcache

# Intl (internationalization)
sudo dnf install php-intl
```

Restart PHP-FPM after installing extensions:

```wp-block-code
sudo systemctl restart php-fpm
```

## PHP Configuration

Edit `/etc/php.ini` for common settings:

```wp-block-code
memory_limit = 256M
upload_max_filesize = 50M
post_max_size = 55M
max_execution_time = 300
date.timezone = Asia/Hong_Kong
display_errors = Off
error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT
```

## SELinux Configuration

Fedora enforces SELinux, which can block PHP from accessing files:

```wp-block-code
# Allow PHP to write to web directories
sudo setsebool -P httpd_unified on

# Allow PHP to connect to databases
sudo setsebool -P httpd_can_network_connect_db on

# Allow PHP to send email
sudo setsebool -P httpd_can_sendmail on

# Check SELinux context of web files
ls -laZ /var/www/html/
```

## Virtual Host Configuration

Create a virtual host for your PHP application:

```wp-block-code
sudo tee /etc/httpd/conf.d/mysite.conf > /dev/null << 'EOF'

    ServerName mysite.local
    DocumentRoot /var/www/mysite/public

    
        AllowOverride All
        Require all granted
    

    ErrorLog /var/log/httpd/mysite-error.log
    CustomLog /var/log/httpd/mysite-access.log combined

EOF

sudo systemctl restart httpd
```

## Quick Reference

- `sudo dnf install httpd php php-fpm` — Install
- `php -v` — Check PHP version
- `/etc/php.ini` — PHP configuration
- `/etc/httpd/conf.d/` — Apache site configs
- `sudo systemctl restart httpd php-fpm` — Apply changes

## PHP Version Management on Fedora

Fedora ships a single PHP version in the default repositories. To run multiple PHP versions:

```wp-block-code
# Install Remi repository for multiple PHP versions
sudo dnf install https://rpms.remirepo.net/fedora/remi-release-latest.rpm
sudo dnf module reset php
sudo dnf module install php:remi-8.3
php -v
```

## PHP-FPM Pool Configuration

For production, tune PHP-FPM pool settings in the configuration file:

```wp-block-code
[www]
pm = dynamic
pm.max_children = 50
pm.start_servers = 5
pm.min_spare_servers = 3
pm.max_spare_servers = 35
pm.max_requests = 500
```

Use pm = dynamic for most sites, or pm = ondemand for low-traffic sites to save memory.

## Enable HTTPS with Let Encrypt

```wp-block-code
sudo dnf install certbot python3-certbot-apache
sudo certbot --apache -d yourdomain.com
```

Certbot automatically configures Apache with SSL and sets up automatic renewal. PHP works identically over HTTP and HTTPS without configuration changes.
