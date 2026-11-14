---
title: "gtk-update-icon-cache-3(1)"
name: "gtk-update-icon-cache-3"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtk-update-icon-cache-3/"
description: "gtk-update-icon-cache – Icon theme caching utility"
---

<h2 class="name">NAME</h2>
<p> gtk-update-icon-cache &#8211; Icon theme caching utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gtk-update-icon-cache</code> [&#8211;force] [&#8211;ignore-theme-index] [&#8211;index-only] [&#8211;source&nbsp;<wbr><i>NAME</i>] [&#8211;quiet] [&#8211;validate] <i>PATH</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>gtk-update-icon-cache</code></p>
<dd>creates mmapable cache files for icon themes. </p>
<p> It expects to be given the <i>PATH</i> to a icon theme directory containing an index.theme, e.g. /usr/share/icons/hicolor, and writes a icon-theme.cache containing cached information about the icons in the directory tree below the given directory. </p>
<p> GTK+ can use the cache files created by <code>gtk-update-icon-cache</code> to avoid a lot of system call and disk seek overhead when the application starts. Since the format of the cache files allows them to be mmaped shared between multiple applications, the overall memory consumption is reduced as well.</p>
<h2>OPTIONS</h2>
<p> &#8211;force, -f</p>
<dl>
<dt>
<dd> Overwrite an existing cache file even if it appears to be uptodate.</dl>
<p> &#8211;ignore-theme-index, -t</p>
<dl>
<dt>
<dd> Don&#8217;t check for the existence of index.theme in the icon theme directory. Without this option, <code>gtk-update-icon-cache</code> refuses to create an icon cache in a directory which does not appear to be the toplevel directory of an icon theme.</dl>
<p> &#8211;index-only, -i</p>
<dl>
<dt>
<dd> Don&#8217;t include image data in the cache.</dl>
<p> &#8211;source, -c</p>
<dl>
<dt>
<dd> Output a C header file declaring a constant <i>NAME</i> with the contents of the icon cache.</dl>
<p> &#8211;quiet, -q</p>
<dl>
<dt>
<dd> Turn off verbose output.</dl>
<p> &#8211;validate, -v</p>
<dl>
<dt>
<dd> Validate existing icon cache.</dl>
<h2>Index</h2>
