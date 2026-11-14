---
title: "zzip_realdir(3)"
name: "zzip_realdir"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_realdir/"
description: "zzip_file_real, zzip_dir_real, zzip_realdir, zzip_realfd – …"
---

<p>zzip_file_real, zzip_dir_real, zzip_realdir, zzip_realfd &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

int zzip_file_real((ZZIP_FILE * fp));

int zzip_dir_real((ZZIP_DIR * dir));

void *zzip_realdir((ZZIP_DIR * dir));

int zzip_realfd((ZZIP_FILE * fp));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_dir_real</code> function checks if the ZZIP_DIR-handle is wrapping a real directory or a zip-archive. Returns 1 for a stat&#8217;able directory, and 0 for a handle to zip-archive. </p>
<p> The <code>zzip_realdir</code> function returns the posix DIR* handle (if one exists). Check before with <code>zzip_dir_real</code> if the the ZZIP_DIR points to a real directory. </p>
<p> The <code>zzip_realfd</code> function returns the posix file descriptor (if one exists). Check before with <code>zzip_file_real</code> if the the ZZIP_FILE points to a real file.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
