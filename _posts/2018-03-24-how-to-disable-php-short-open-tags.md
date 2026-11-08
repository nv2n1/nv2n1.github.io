---
title: "Disabling PHP Short Open Tags"
date: 2018-03-24 11:53:43 +0000
modified: 2026-04-12 16:05:07 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-disable-php-short-open-tags/
---

Short open tags (`<?` `?>`) create compatibility issues with XML declarations and are considered poor practice. While they’re disabled by default in modern PHP versions, you may need to manage this setting when working with legacy code or specific server configurations.

## Configuration Methods

### Via php.ini

The primary way to control short open tags is through the `php.ini` configuration file:

``` ini
short_open_tag = Off
```

Locate your active `php.ini` file:

``` bash
php --ini
```

This outputs the configuration file path. Edit it directly:

``` bash
sudo nano /etc/php/8.3/cli/php.ini
```

Then restart your web server:

``` bash
sudo systemctl restart nginx
# or for Apache
sudo systemctl restart apache2
```

### Via .htaccess (Apache only)

If you can’t modify `php.ini`, use `.htaccess` in your project root:

``` apache
php_flag short_open_tag Off
```

This requires `mod_php` and won’t work with PHP-FPM configurations.

### Via .user.ini (PHP-FPM)

For PHP-FPM setups, create a `.user.ini` file in your project root:

``` ini
short_open_tag = Off
```

This takes effect within seconds (check `user_ini.cache_ttl` in `php.ini` if changes don’t apply immediately).

### Via docker-compose or environment

In containerized environments, override settings at runtime:

``` dockerfile
RUN echo "short_open_tag = Off" >> /etc/php/8.3/fpm/php.ini
```

## Verification

Check your current setting:

``` bash
php -i | grep "short_open_tag"
# Output: short_open_tag => Off => Off
```

Or in a PHP script:

``` php
<?php
echo ini_get('short_open_tag') ? 'On' : 'Off';
```

## Why This Matters

Modern frameworks (Laravel, Symfony, Drupal) and CMSs (WordPress) enforce the full `<?php` tag syntax. Short tags conflict with:

- XML declarations (`<?xml version="1.0"?>`)
- XHTML processing instructions
- Server configurations where short tags are disabled

PHP 8.0+ disables short open tags by default. If you’re stuck supporting legacy code that uses them, use a code migration tool instead:

``` bash
# Find all short tags in your codebase
grep -r "<?" --include="*.php" . | grep -v "<?php"
```

Then convert them systematically rather than relying on the setting being enabled across all environments.

## Edge Cases

If you inherit a large codebase with short tags enabled everywhere, consider:

1.  **Automated replacement**: Use sed to convert files

    ``` bash
    find . -name "*.php" -exec sed -i 's/<?\s/<?php /g' {} \;
    ```

2.  **Gradual migration**: Keep short tags disabled in production while fixing code in development

3.  **AST-based tools**: Use tools like PHP-Parser for safer refactoring of complex codebases

Always verify your application works after disabling short open tags—this surfaces incompatible code before it reaches production.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
