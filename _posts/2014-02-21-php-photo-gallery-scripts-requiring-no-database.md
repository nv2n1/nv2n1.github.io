---
title: "When to Use File-Based Photo Galleries in PHP"
date: 2014-02-21 04:13:55 +0000
layout: post
canonical: https://www.systutorials.com/php-photo-gallery-scripts-requiring-no-database/
---

Self-hosting a photo gallery gives you control over your content. If you want to skip database management entirely, a handful of PHP solutions still work—though most are unmaintained. This post covers what’s still functional, where the limits are, and when you should choose something else instead.

## Static File-Based Gallery Scripts

### Single File PHP Gallery

**Status:** Unmaintained but functional for basic use cases

This is literally one PHP file that lives in your photos directory. It generates thumbnails on-the-fly and auto-detects subdirectories as sub-galleries.

**Pros:**

- Zero configuration needed
- Auto-discovers subdirectories as separate galleries
- Minimal server requirements (just PHP-GD for image processing)
- No config files or external dependencies

**Cons:**

- Performance tanks with large collections (thumbnail generation is CPU-intensive on every request)
- No thumbnail caching—every visitor triggers regeneration
- Very basic styling; customization is limited
- Code is old; verify compatibility with PHP 8.2+

**Setup:**

``` bash
# Download from GitHub (search "sfpg php" or "single file php gallery")
cp sfpg.php /var/www/html/photos/

# Access it
# http://yoursite.com/photos/
```

**Important:** Adjust PHP settings for larger galleries:

``` ini
memory_limit = 256M
max_execution_time = 60
upload_max_filesize = 100M
post_max_size = 100M
```

With hundreds of images, expect slow page loads. Consider pre-generating thumbnails with ImageMagick instead:

``` bash
mogrify -resize 300x300 -quality 85 -path ./thumbs *.jpg
```

### phpGraphy

**Status:** Development frozen around 2010–2012; still runs on modern PHP with caveats

phpGraphy is more feature-rich than Single File PHP Gallery. It handles EXIF metadata, comments, and ratings using flat files instead of a database.

**Pros:**

- Extracts and displays EXIF/IPTC metadata
- Comment and rating system stored in flat files
- More polished UI than minimal alternatives
- Themeable with CSS
- Basic user authentication support

**Cons:**

- Unmaintained; may need code tweaks for PHP 8+
- File-based comment/rating storage creates race conditions under concurrent load
- Requires proper directory permissions for writable folders
- Flat-file locking issues if multiple users rate/comment simultaneously

**Setup:**

``` bash
tar xzf phpgraphy-*.tar.gz
mv phpgraphy /var/www/html/gallery
cd /var/www/html/gallery

# Create writable directories for metadata, cache, comments
mkdir -p cache metadata comments
chmod 755 cache metadata comments

# Set proper ownership if running under a web server user
chown www-data:www-data cache metadata comments
```

Then access `http://yoursite.com/gallery/`

**Race condition mitigation:** If concurrent access is likely, add advisory file locking in the comment/rating handlers or use a simple SQLite database instead.

## Performance Tuning for File-Based Galleries

### Thumbnail Caching

On-the-fly thumbnail generation works for galleries under 100 images. Beyond that, pre-generate thumbnails or implement caching headers:

``` php
$thumbDir = './thumbs';
$thumbFile = $thumbDir . '/' . md5($imagePath) . '.jpg';

if (!file_exists($thumbFile)) {
    // Generate thumbnail
    $img = imagecreatefromjpeg($imagePath);
    $thumb = imagescale($img, 300);
    imagejpeg($thumb, $thumbFile, 85);
    imagedestroy($img);
    imagedestroy($thumb);
}

// Send with long cache headers
header('Cache-Control: public, max-age=31536000');
readfile($thumbFile);
```

### Image Optimization

Resize source images before uploading:

``` bash
# Batch resize all JPEGs to 2500px max width
mogrify -resize 2500x2500 -quality 85 -strip *.jpg
```

Stripping EXIF reduces file size; keep it only if you’re displaying metadata.

### Web Server Caching

Add caching headers in your web server config:

**Nginx:**

``` nginx
location ~* \.(jpg|jpeg|png|gif)$ {
    expires 30d;
    add_header Cache-Control "public, immutable";
}
```

**Apache (.htaccess):**

    <FilesMatch "\.(jpg|jpeg|png|gif)$">
        Header set Cache-Control "max-age=2592000, public"
    </FilesMatch>

## When Database-Free Actually Makes Sense

File-based galleries work if you:

- Host personal collections under 500 images
- Don’t need user comments, ratings, or authentication
- Have limited hosting options (shared hosting with no database access)
- Want zero maintenance overhead

## When You Should Use Something Else

If you need any of these, invest the setup time in a lightweight solution:

- User comments or ratings (requires locking to avoid data corruption)
- Large collections (1000+ images; file I/O bottlenecks)
- User accounts and permissions
- Search functionality across metadata

**Better alternatives:**

- **Lychee** – Modern, actively maintained, uses SQLite (single-file database), mobile-responsive
- **Piwigo** – Feature-rich, actively developed, supports both database and file-based metadata
- **Immich** – Self-hosted photo management with AI features, modern stack

For anything beyond a basic personal photo dump, database-backed solutions require less setup workaround code than trying to bolt features onto flat-file systems. The maintenance burden shifts to your backup strategy, not hand-rolled locking logic.
