---
title: "zzip_rewinddir(3)"
name: "zzip_rewinddir"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_rewinddir/"
description: "zzip_rewinddir, zzip_telldir, zzip_seekdir, zzip_telldir32, zzip_seekdir32 –"
---

<p>zzip_rewinddir, zzip_telldir, zzip_seekdir, zzip_telldir32, zzip_seekdir32 &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

void zzip_rewinddir((ZZIP_DIR * dir));

zzip_off_t zzip_telldir((ZZIP_DIR * dir));

void zzip_seekdir((ZZIP_DIR * dir, zzip_off_t offset));

long zzip_telldir32((ZZIP_DIR * dir));

void zzip_seekdir32((ZZIP_DIR * dir, long offset));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_rewinddir</code> function is the equivalent of a <code><a href="/docs/linux/man/2-rewinddir/">rewinddir</a>(2)</code> for a realdir or the zipfile in place of a directory. The ZZIP_DIR handle returned from <code>zzip_opendir</code> has a flag saying realdir or zipfile. As for a zipfile, the filenames will include the filesubpath, so take care. </p>
<p> The <code>zzip_telldir</code> function is the equivalent of <code><a href="/docs/linux/man/2-telldir/">telldir</a>(2)</code> for a realdir or zipfile. </p>
<p> The <code>zzip_seekdir</code> function is the equivalent of <code><a href="/docs/linux/man/2-seekdir/">seekdir</a>(2)</code> for a realdir or zipfile. </p>
<p> The <code>zzip_telldir32</code> function is provided for users who can not use any largefile-mode. </p>
<p> The <code>zzip_seekdir32</code> function is provided for users who can not use any largefile-mode.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 1999,2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
