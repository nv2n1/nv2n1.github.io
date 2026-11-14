---
title: "zzip_dir_fdopen_ext_io(3)"
name: "zzip_dir_fdopen_ext_io"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_dir_fdopen_ext_io/"
description: "zzip_dir_fdopen, zzip_dir_fdopen_ext_io – …"
---

<p>zzip_dir_fdopen, zzip_dir_fdopen_ext_io &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

ZZIP_DIR *zzip_dir_fdopen((int fd, zzip_error_t *errcode_p));

ZZIP_DIR *zzip_dir_fdopen_ext_io((int fd, zzip_error_t *errcode_p, zzip_strings_t *ext, const zzip_plugin_io_t io));</code></pre>
<h2>Description</h2>
<dd>the <code>zzip_dir_fdopen_ext_io</code> function uses explicit ext and io instead of the internal defaults, setting these to zero is equivalent to <code>zzip_dir_fdopen</code></p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt; Tomi Ollila &lt;too [at] iki.fi&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 1999,2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
