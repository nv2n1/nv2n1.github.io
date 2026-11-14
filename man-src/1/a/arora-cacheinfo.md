---
title: "arora-cacheinfo(1)"
name: "arora-cacheinfo"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arora-cacheinfo/"
description: "arora-cacheinfo – a tool for extracting files and metadata out of Arora cache files."
---

<h2 class="name">NAME</h2>
<p> arora-cacheinfo &#8211; a tool for extracting files and metadata out of Arora cache files.</p>
<h2>SYNOPSIS</h2>
<p> <code>arora-cacheinfo [-o cachefile] [file | url]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Arora-cacheinfo</code> is a tool for extracting files and displaying metadata out of an Arora cache files that are stored on the disk. Every cache file contains both the cached file (sometimes compressed) and metadata associated with it such as expiration date. Cache files names always include the md5sum of the url and passing a url to arora-cacheinfo.1 will automatically determine the correct matching cache file name. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o cachefile</code></p>
<dd> Write the cached file if it exists to <code>cachefile</code></p>
<dt><code>file</code></p>
<dd> Specify the file to read from.</p>
<dt><code>url</code></p>
<dd> Specify the url from which to compute the file to read from.</p>
<dt>
<dd></dl>
<h2>BUGS</h2>
<p> Please report bugs to <i><a rel="nofollow" href="http://code.google.com/p/arora/issues/list">http://code.google.com/p/arora/issues/list</a></i>. </p>
<h2>AUTHOR</h2>
<p> The author of arora-cacheinfo is Benjamin C. Meyer &lt;ben [at] meyerhome.net&gt;. </p>
<p> This manual page was written by Benjamin C. Meyer &lt;ben [at] meyerhome.net&gt; </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
