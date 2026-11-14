---
title: "zzip_strerror(3)"
name: "zzip_strerror"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_strerror/"
description: "zzip_strerror, zzip_strerror_of – …"
---

<p>zzip_strerror, zzip_strerror_of &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

zzip_char_t *zzip_strerror((int errcode));

zzip_char_t *zzip_strerror_of((ZZIP_DIR * dir));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_strerror_of</code> function fetches the errorcode from the <code>DIR-handle</code> and runs it through <code>zzip_strerror</code> to obtain the static string describing the error.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt; Tomi Ollila &lt;Tomi.Ollila [at] iki.fi&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 1999,2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
