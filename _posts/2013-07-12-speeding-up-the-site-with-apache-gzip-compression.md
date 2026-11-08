---
title: "Apache GZIP vs. Brotli: Setup and Testing Guide"
date: 2013-07-12 16:46:13 +0000
author: "Eric Ma"
layout: post
categories: [system-administration-cloud]
canonical: /speeding-up-the-site-with-apache-gzip-compression/
---

HTTP compression reduces bandwidth usage and improves load times for clients. Apache’s mod_deflate and mod_brotli handle this transparently—the server compresses content before sending it, and modern browsers decompress it automatically.

## Enabling Compression via .htaccess

Add this to your `.htaccess` file in the website root:

``` apache
# Enable DEFLATE compression
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/plain text/html text/xml text/css
  AddOutputFilterByType DEFLATE application/xml application/xhtml+xml application/rss+xml
  AddOutputFilterByType DEFLATE application/javascript application/json
  AddOutputFilterByType DEFLATE text/javascript

  # Exclude already-compressed formats (images, fonts, archives)
  SetEnvIfNoCase Request_URI \.(?:gif|jpe?g|png|svg|woff2|woff|zip|gz|br)$ no-gzip dont-vary
</IfModule>
```

The `SetEnvIfNoCase` line prevents double-compression of already-compressed formats like images, WOFF2 fonts, and Brotli-encoded assets, which wastes CPU cycles and provides no benefit.

## Enabling via Apache Virtual Host Configuration

If `.htaccess` isn’t available or `AllowOverride` is disabled, edit your virtual host configuration in `/etc/apache2/sites-available/`:

``` apache
<Directory /var/www/yoursite>
  <IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/plain text/html text/xml text/css
    AddOutputFilterByType DEFLATE application/xml application/xhtml+xml application/rss+xml
    AddOutputFilterByType DEFLATE application/javascript application/json text/javascript
    SetEnvIfNoCase Request_URI \.(?:gif|jpe?g|png|svg|woff2|woff|zip|gz|br)$ no-gzip dont-vary
  </IfModule>
</Directory>
```

Reload Apache after editing:

``` bash
sudo systemctl reload apache2
```

## Configuring Compression Level

By default, mod_deflate uses compression level 6. Adjust this in your configuration:

``` apache
<IfModule mod_deflate.c>
  DeflateCompressionLevel 6
  AddOutputFilterByType DEFLATE text/html text/plain text/css application/javascript
</IfModule>
```

Compression levels range from 1 (fastest, larger output) to 9 (slowest, smallest output). Level 6 provides a good balance for most workloads:

- **Level 5**: For CPU-constrained or high-traffic sites; reduces compression overhead by ~10-15% while maintaining reasonable compression ratios
- **Level 6**: Default; suitable for most workloads
- **Level 7-8**: For low-traffic sites where bandwidth savings justify higher CPU usage

Monitor Apache CPU usage under load to test the impact on your specific workload:

``` bash
top -p $(pgrep -d ',' apache2)
```

## Excluding Specific URLs from Compression

Exclude endpoints that shouldn’t be compressed (pre-compressed content, streaming, large downloads):

``` apache
SetEnvIfNoCase Request_URI ^/api/download no-gzip
SetEnvIfNoCase Request_URI ^/stream/ no-gzip
SetEnvIfNoCase Request_URI ^/media/videos/ no-gzip
```

## Brotli Compression: Modern Alternative

Brotli (mod_brotli) offers better compression ratios than gzip and is supported by all modern browsers. Install it on Debian/Ubuntu:

``` bash
sudo apt install libbrotli1 mod-brotli
sudo a2enmod brotli
sudo systemctl reload apache2
```

Configure Brotli alongside gzip for maximum compatibility:

``` apache
<IfModule mod_brotli.c>
  AddOutputFilterByType BROTLI_COMPRESS text/html text/plain text/xml text/css
  AddOutputFilterByType BROTLI_COMPRESS text/javascript application/javascript application/json
</IfModule>

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css
  AddOutputFilterByType DEFLATE text/javascript application/javascript application/json
</IfModule>

SetEnvIfNoCase Request_URI \.(?:gif|jpe?g|png|svg|woff2|woff|zip|gz|br)$ no-gzip dont-vary
```

Apache will use Brotli if the client supports it, falling back to gzip otherwise.

## Verifying Compression

Check response headers with curl:

``` bash
curl -I -H "Accept-Encoding: gzip, deflate" https://example.com
```

You should see `Content-Encoding: gzip` or `Content-Encoding: br` in the response headers. To see actual compression in action and inspect decompressed content:

``` bash
curl -s -H "Accept-Encoding: gzip" https://example.com | gunzip | head -n 20
```

For detailed diagnostics including transfer size comparisons:

``` bash
curl -s -w "\nUncompressed size: %{size_download}\nCompressed size: %{size_request}\n" \
  -H "Accept-Encoding: gzip" https://example.com > /tmp/response.gz
```

Compare response sizes without compression vs. with compression:

``` bash
# Request without compression
curl -I -H "Accept-Encoding: " https://example.com | grep -i content-length

# Request with compression
curl -I -H "Accept-Encoding: gzip" https://example.com | grep -i content-length
```

## Measuring Compression Impact

Most sites see 60-80% reduction in HTML, CSS, and JavaScript transfer sizes. Monitor live impact by calculating average response sizes from Apache access logs:

``` bash
awk '{sum+=$10; count++} END {print "Average response size: " int(sum/count) " bytes"}' /var/log/apache2/access.log
```

Enable mod_logio for more accurate metrics of transferred (compressed) vs. actual content size:

``` bash
sudo a2enmod logio
```

Update your log format in `/etc/apache2/apache2.conf` or virtual host configuration to include `%I` (bytes received) and `%O` (bytes sent):

``` apache
LogFormat "%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\" %I" combined_io
CustomLog ${APACHE_LOG_DIR}/access.log combined_io
```

Then reload Apache and check the difference between `%I` and `%O` to see actual compression gains in production traffic.
