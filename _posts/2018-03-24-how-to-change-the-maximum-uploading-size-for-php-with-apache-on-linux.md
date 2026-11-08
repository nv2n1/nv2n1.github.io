---
title: "Configuring PHP Upload Size Limits on Linux Apache"
date: 2018-03-24 11:53:38 +0000
layout: post
canonical: https://www.systutorials.com/how-to-change-the-maximum-uploading-size-for-php-with-apache-on-linux/
---

\[md\]\
PHP upload limits are controlled through the `php.ini` configuration file. On Ubuntu/Debian systems, the file location depends on your PHP version:

```wp-block-code
/etc/php/8.3/apache2/php.ini          # PHP 8.3
/etc/php/8.2/apache2/php.ini          # PHP 8.2
/etc/php/8.1/apache2/php.ini          # PHP 8.1
```

To find your actual PHP version and configuration path:

```wp-block-code
php -i | grep "Loaded Configuration File"
```

\## Key Configuration Directives

Three settings control upload behavior. Edit your `php.ini` file:

\*\*Maximum upload file size:\*\*

```wp-block-code
upload_max_filesize = 50M
```

\*\*Maximum POST data size (must be \>= upload_max_filesize):\*\*

```wp-block-code
post_max_size = 55M
```

\*\*Maximum script memory consumption:\*\*

```wp-block-code
memory_limit = 128M
```

\*\*Maximum execution time for uploads:\*\*

```wp-block-code
max_execution_time = 300
max_input_time = 300
```

The relationship is: `memory_limit > post_max_size > upload_max_filesize`

\## Apply Changes

After editing php.ini, restart Apache:

```wp-block-code
sudo systemctl restart apache2        # Ubuntu/Debian
sudo systemctl restart httpd           # CentOS/RHEL/Fedora
```

Verify the changes took effect:

```wp-block-code
php -i | grep upload_max_filesize
```

\## Using .htaccess for Per-Directory Overrides

If you can’t edit php.ini directly, you can set upload limits per directory using `.htaccess`:

```wp-block-code
php_value upload_max_filesize 50M
php_value post_max_size 55M
php_value max_execution_time 300
php_value max_input_time 300
```

This requires `AllowOverride Options` or `AllowOverride All` in your Apache virtual host configuration. It doesn’t work with PHP-FPM or nginx — only with mod_php.

\## Nginx Configuration

If you use nginx with PHP-FPM, nginx has its own upload size limit:

```wp-block-code
# In http, server, or location block
client_max_body_size 50m;
```

Without this, nginx returns `413 Request Entity Too Large` for files exceeding its default 1MB limit, even if PHP is configured to accept larger uploads.

After changing nginx config:

```wp-block-code
sudo nginx -t          # Test configuration
sudo systemctl reload nginx
```

\## PHP-FPM Configuration

With PHP-FPM, the pool configuration can override php.ini settings:

```wp-block-code
# /etc/php/8.3/fpm/pool.d/www.conf
php_admin_value[upload_max_filesize] = 50M
php_admin_value[post_max_size] = 55M
```

Restart PHP-FPM after changes:

```wp-block-code
sudo systemctl restart php8.3-fpm
```

\## Handling Large File Uploads in Application Code

For files larger than a few hundred MB, consider alternative approaches:

\*\*Chunked uploads\*\* — break files into smaller pieces on the client side:

```wp-block-code
// JavaScript (client)
const CHUNK_SIZE = 5 * 1024 * 1024; // 5MB chunks
for (let start = 0; start < file.size; start += CHUNK_SIZE) {
  const chunk = file.slice(start, start + CHUNK_SIZE);
  const formData = new FormData();
  formData.append('chunk', chunk);
  formData.append('offset', start);
  formData.append('total', file.size);
  await fetch('/upload.php', { method: 'POST', body: formData });
}
```

\*\*Resumable uploads\*\* — use libraries like tus.io or Dropzone.js for production upload handling with progress, retry, and resume support.

\## Troubleshooting

\*\*Upload silently fails:\*\*

Check all three size limits — the most common issue is `post_max_size` being smaller than `upload_max_filesize`.

\*\*Error 413 from nginx:\*\*

Increase `client_max_body_size` in your nginx configuration.

\*\*Timeout during upload:\*\*

Increase `max_execution_time` and `max_input_time`. For very large files on slow connections, set both to `0` (no limit) temporarily.

\*\*Check effective settings:\*\*

Create a PHP info page to see all active values:

```wp-block-code
<?php phpinfo(); ?>
```

Access it in a browser and search for "upload" to see the effective configuration. Remove the file after checking for security.

\## Docker and Container Environments

In Docker containers running PHP, you can set upload limits without modifying php.ini:

```wp-block-code
# Dockerfile
FROM php:8.3-apache

# Set upload limits
RUN echo "upload_max_filesize = 50M" >> /usr/local/etc/php/conf.d/uploads.ini \
    && echo "post_max_size = 55M" >> /usr/local/etc/php/conf.d/uploads.ini \
    && echo "max_execution_time = 300" >> /usr/local/etc/php/conf.d/uploads.ini
```

Or pass via environment variable with a custom entrypoint:

```wp-block-code
# docker-compose.yml
services:
  php:
    image: php:8.3-apache
    environment:
      PHP_UPLOAD_MAX_FILESIZE: 50M
      PHP_POST_MAX_SIZE: 55M
```

The PHP Docker image automatically loads any `.ini` files from `/usr/local/etc/php/conf.d/`.

For nginx in Docker, add the client_max_body_size directive:

```wp-block-code
server {
    client_max_body_size 50m;
    location ~ \.php$ {
        fastcgi_pass php:9000;
        # ... other fastcgi params
    }
}
```
