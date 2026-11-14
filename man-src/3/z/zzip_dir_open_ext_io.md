---
title: "zzip_dir_open_ext_io(3)"
name: "zzip_dir_open_ext_io"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_dir_open_ext_io/"
description: "zzip_dir_open, zzip_dir_open_ext_io, zzip_dir_read – …"
---

<p>zzip_dir_open, zzip_dir_open_ext_io, zzip_dir_read &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

ZZIP_DIR *zzip_dir_open((zzip_char_t * filename, zzip_error_t *e));

ZZIP_DIR *zzip_dir_open_ext_io((zzip_char_t * filename, zzip_error_t *e, zzip_strings_t *ext, zzip_plugin_io_t io));

int zzip_dir_read((ZZIP_DIR * dir, ZZIP_DIRENT *d));</code></pre>
<h2>Description</h2>
<dd>the <code>zzip_dir_open_ext_io</code> function uses explicit ext and io instead of the internal defaults. Setting these to zero is equivalent to <code>zzip_dir_open</code> Note that the referenced ext_io plugin handlers structure must be static as it is not copied to the returned ZZIP_DIR structure. </p>
<p> fills the dirent-argument with the values and increments the read-pointer of the dir-argument. </p>
<p> returns 0 if there no entry (anymore).</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt; Tomi Ollila &lt;too [at] iki.fi&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 1999,2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
