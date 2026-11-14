---
title: "zzip_get_default_io(3)"
name: "zzip_get_default_io"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_get_default_io/"
description: "zzip_init_io, zzip_get_default_io – …"
---

<p>zzip_init_io, zzip_get_default_io &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

int zzip_init_io((zzip_plugin_io_handlers_t io, int flags));

zzip_plugin_io_t zzip_get_default_io((void));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_get_default_io</code> function returns a zzip_plugin_io_t handle to static defaults wrapping the posix io file functions for actual file access. The returned structure is shared by all threads in the system.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt; Mike Nordell &lt;tamlin- [at] -algonet-se&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
