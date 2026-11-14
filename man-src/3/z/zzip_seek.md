---
title: "zzip_seek(3)"
name: "zzip_seek"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_seek/"
description: "zzip_seek, zzip_seek32 – …"
---

<p>zzip_seek, zzip_seek32 &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

zzip_off_t zzip_seek((ZZIP_FILE * fp, zzip_off_t offset, int whence));

long zzip_seek32((ZZIP_FILE * fp, long offset, int whence));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_seek32</code> function is provided for users who can not use any largefile-mode.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt; Tomi Ollila &lt;Tomi.Ollila [at] iki.fi&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 1999,2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
