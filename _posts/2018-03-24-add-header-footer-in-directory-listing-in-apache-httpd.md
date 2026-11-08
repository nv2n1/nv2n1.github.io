---
title: "Custom Headers and Footers in Apache Directory Listings"
date: 2018-03-24 08:22:23 +0000
author: "Eric Ma"
layout: post
categories: [system-administration-cloud]
canonical: /add-header-footer-in-directory-listing-in-apache-httpd/
---

Custom headers and footers in Apache directory listings let you add branding, instructions, or navigation without modifying the core file listing. This is useful for public file archives, download directories, or any indexed directory you want to customize.

## Basic Setup with .htaccess

Add these directives to `.htaccess` in the directory where you want custom listings:

``` apache
Options +Indexes
IndexOptions FancyIndexing VersionSort NameWidth=* HTMLTable Charset=UTF-8
HeaderName /header.html
ReadmeName /footer.html
IndexIgnore header.html footer.html .htaccess
```

The header file displays above the file listing, and the footer displays below it. Both paths are relative to your document root.

## Configuration Directives Explained

**Options +Indexes** — enables directory listing. Use `-Indexes` to disable it.

**IndexOptions** controls appearance:

- `FancyIndexing` — enables column headers and file type icons
- `VersionSort` — sorts filenames naturally (1, 2, 10 instead of 1, 10, 2)
- `NameWidth=*` — auto-sizes the filename column
- `HTMLTable` — renders listings as an HTML table for better styling
- `Charset=UTF-8` — sets character encoding

**HeaderName** specifies the header file. Apache searches for `.header.html`, `header.html`, or `HEADER.HTML` in order. Using `/header.html` forces it to look in the document root.

**ReadmeName** specifies the footer file with the same lookup logic.

**IndexIgnore** prevents these files (and `.htaccess`) from appearing in the listing.

## Creating Header and Footer Files

Create `header.html` and `footer.html` in your document root. Do **not** include `<html>` or `<body>` tags — Apache wraps the directory listing between them automatically.

``` html
<div class="header" style="background: #f0f0f0; padding: 15px; border-radius: 4px; margin-bottom: 20px;">
  <h1 style="margin: 0 0 10px 0;">File Archive</h1>
  <p style="margin: 0; color: #666;">Select a file to download. For questions, contact support.</p>
</div>
```

For the footer:

``` html
<hr style="margin-top: 20px; border: none; border-top: 1px solid #ccc;">
<div style="padding: 15px; text-align: center; font-size: 14px; color: #666;">
  <p>&copy; 2026 Your Organization</p>
  <p><a href="/">Back to Home</a> | <a href="/help">Help</a></p>
</div>
```

Use inline styles instead of external stylesheets to avoid CORS or CSP policy issues. The header and footer HTML fragments are injected directly into Apache’s auto-generated listing page.

## Directory-Specific Headers

For different headers in subdirectories, create `.htaccess` files in each subdirectory with their own `HeaderName` and `ReadmeName` directives:

``` apache
HeaderName /subdir-header.html
ReadmeName /subdir-footer.html
```

This overrides the parent directory’s settings for that branch only.

## Production Setup with Virtual Host Configuration

Using `.htaccess` requires `AllowOverride Indexes` and adds filesystem overhead on every request. For production, configure this in your virtual host instead:

``` apache
<Directory /var/www/html/files>
    Options +Indexes
    IndexOptions FancyIndexing VersionSort NameWidth=* HTMLTable Charset=UTF-8
    HeaderName /header.html
    ReadmeName /footer.html
    IndexIgnore header.html footer.html .htaccess
</Directory>
```

Reload Apache after changes:

``` bash
sudo systemctl reload apache2
```

or on RHEL/CentOS/Rocky:

``` bash
sudo systemctl reload httpd
```

## Troubleshooting

**Headers/footers not appearing:**

- Verify `.htaccess` is in the correct directory and readable
- Check that `AllowOverride Indexes` is set in your Apache configuration (or remove `.htaccess` and use virtual host config instead)
- Confirm the HTML files exist at the specified absolute paths
- Check Apache error logs: `sudo tail -f /var/log/apache2/error.log`
- Verify Options +Indexes isn’t disabled by a parent `<Directory>` block with `-Indexes`

**File paths not working:**

- Use absolute paths from the document root (`/header.html`)
- Relative paths work only if the file is in the same directory as `.htaccess`
- Leading `/` is recommended to avoid ambiguity

**Styling not applying:**

- Use inline `<style>` tags or inline `style` attributes instead of external stylesheets
- Verify the HTML fragments are well-formed (missing closing tags break the listing)
- Test in browser DevTools to confirm the header/footer fragments are present in the page source

**IndexIgnore not working:**

- Make sure the filenames match exactly (case-sensitive on Linux)
- Wildcards work: `IndexIgnore *.html` ignores all HTML files

## Performance Notes

Directory listing can be expensive on directories with thousands of files. `FancyIndexing` and `HTMLTable` add minimal overhead compared to plain listing, but sorting by date or size on every request requires filesystem stat calls. If you have performance concerns, consider serving a static index page instead for frequently accessed directories.
