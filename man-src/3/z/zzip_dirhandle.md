---
title: "zzip_dirhandle(3)"
name: "zzip_dirhandle"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_dirhandle/"
description: "zzip_dirhandle, zzip_dirfd – …"
---

<p>zzip_dirhandle, zzip_dirfd &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

ZZIP_DIR *zzip_dirhandle((ZZIP_FILE * fp));

int zzip_dirfd((ZZIP_DIR * dir));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_dirfd</code> function will just return dir-&gt;fd </p>
<p> If a ZZIP_DIR does point to a zipfile then the file-descriptor of that zipfile is returned, otherwise a NULL is returned and the ZZIP_DIR wraps a real directory DIR (if you have dirent on your system).</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
