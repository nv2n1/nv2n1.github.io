---
title: "gtk4-update-icon-cache(1)"
name: "gtk4-update-icon-cache"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk4-update-icon-cache/"
description: "gtk4-update-icon-cache – Icon theme caching utility"
---

<h2 class="name">NAME</h2>
<p> gtk4-update-icon-cache &#8211; Icon theme caching utility </p>
<h2>SYNOPSIS</h2>
<pre>
<code>gtk4-update-icon-cache</code> [OPTIONS...] &lt;PATH&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> <code>gtk4-update-icon-cache</code> creates <code><a href="/docs/linux/man/2-mmap/">mmap</a>(2)</code>-able cache files for icon themes. </p>
<p> It expects to be given the <code>PATH</code> to an icon theme directory containing an <code>index.theme</code>, e.g. <code>/usr/share/icons/hicolor</code>, and writes a <code>icon-theme.cache</code> containing cached information about the icons in the directory tree below the given directory. </p>
<p> GTK can use the cache files created by <code>gtk4-update-icon-cache</code> to avoid a lot of system call and disk seek overhead when the application starts. Since the format of the cache files allows them to be shared across multiple processes, for instance using the POSIX <code><a href="/docs/linux/man/2-mmap/">mmap</a>(2)</code> system call, the overall memory consumption is reduced as well.</p>
<h2>OPTIONS</h2>
<p> <code>-f, &#8211;force</code> Overwrite an existing cache file even if it appears to be up-to-date. </p>
<p> <code>-t, &#8211;ignore-theme-index</code> Don&#8217;t check for the existence of <code>index.theme</code> in the icon theme directory. Without this option, <code>gtk4-update-icon-cache</code> refuses to create an icon cache in a directory which does not appear to be the toplevel directory of an icon theme. </p>
<p> <code>-i, &#8211;index-only</code> Don&#8217;t include image data in the cache. </p>
<p> <code>&#8211;include-image-data</code> Include image data in the cache. </p>
<p> <code>-c, &#8211;source &lt;NAME&gt;</code> Output a C header file declaring a constant <code>NAME</code> with the contents of the icon cache. </p>
<p> <code>-q, &#8211;quiet</code> Turn off verbose output. </p>
<p> <code>-v, &#8211;validate</code> Validate existing icon cache. </p>
<h2>Index</h2>
