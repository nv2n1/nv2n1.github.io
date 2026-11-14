---
title: "zzip_dir_alloc_ext_io(3)"
name: "zzip_dir_alloc_ext_io"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_dir_alloc_ext_io/"
description: "zzip_dir_alloc_ext_io, zzip_dir_alloc – …"
---

<p>zzip_dir_alloc_ext_io, zzip_dir_alloc &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

ZZIP_DIR *zzip_dir_alloc_ext_io((zzip_strings_t * ext, const zzip_plugin_io_t io));

ZZIP_DIR *zzip_dir_alloc((zzip_strings_t * fileext));</code></pre>
<h2>Description</h2>
<dd>the <code>zzip_dir_alloc</code> function is obsolete &#8211; it was generally used for implementation and exported to let other code build on it. It is now advised to use <code>zzip_dir_alloc_ext_io</code> now on explicitly, just set that second argument to zero to achieve the same functionality as the old style.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt; Tomi Ollila &lt;too [at] iki.fi&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 1999,2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
