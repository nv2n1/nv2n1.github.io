---
title: "zzip_seterror(3)"
name: "zzip_seterror"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_seterror/"
description: "zzip_error, zzip_seterror – …"
---

<p>zzip_error, zzip_seterror &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

int zzip_error((ZZIP_DIR * dir));

void zzip_seterror((ZZIP_DIR * dir, int errcode));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_seterror</code> function just does dir-&gt;errcode = errcode</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
