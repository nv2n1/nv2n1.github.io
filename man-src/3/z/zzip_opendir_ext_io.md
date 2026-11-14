---
title: "zzip_opendir_ext_io(3)"
name: "zzip_opendir_ext_io"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_opendir_ext_io/"
description: "zzip_opendir, zzip_opendir_ext_io – …"
---

<p>zzip_opendir, zzip_opendir_ext_io &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

ZZIP_DIR *zzip_opendir((zzip_char_t * filename));

ZZIP_DIR *zzip_opendir_ext_io((zzip_char_t * filename, int o_modes, zzip_strings_t *ext, zzip_plugin_io_t io));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_opendir_ext_io</code> function uses explicit ext and io instead of the internal defaults, setting them to zero is equivalent to <code>zzip_opendir</code></p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 1999,2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
