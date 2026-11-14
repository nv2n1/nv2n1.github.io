---
title: "zzip_dir_close(3)"
name: "zzip_dir_close"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_dir_close/"
description: "zzip_dir_free, zzip_dir_close – …"
---

<p>zzip_dir_free, zzip_dir_close &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

int zzip_dir_free((ZZIP_DIR * dir));

int zzip_dir_close((ZZIP_DIR * dir));</code></pre>
<h2>Description</h2>
<dd>It will also <code><a href="/docs/linux/man/2-free/">free</a>(2)</code> the <code>ZZIP_DIR-handle</code> given. the counterpart for <code>zzip_dir_open</code> see also <code>zzip_dir_free</code></p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt; Tomi Ollila &lt;too [at] iki.fi&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 1999,2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
