---
title: "cgiwrap_write(3)"
name: "cgiwrap_write"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgiwrap_write/"
description: "cgiwrap_write – wrapper for the fwrite(stdout)"
---

<h2 class="name">NAME</h2>
<p> cgiwrap_write &#8211; wrapper for the fwrite(stdout) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgiwrap.h&gt;
</code></pre>
<pre><code>
NEOERR *cgiwrap_write(const char *buf, int buf_len);
</code></pre>
<h2>ARGUMENTS</h2>
<p> buf &#8211; a character buffer<br />
 buf_len &#8211; the length of the buffer in buf </p>
<h2>DESCRIPTION</h2>
<p> cgiwrap_write is the block data output function for cgiwrap that replaces fwrite(stdout) in regular CGIs </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgiwrap_iterenv/">cgiwrap_iterenv</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_putenv/">cgiwrap_putenv</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_emu/">cgiwrap_init_emu</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writef/">cgiwrap_writef</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_std/">cgiwrap_init_std</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writevf/">cgiwrap_writevf</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_read/">cgiwrap_read</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_write/">cgiwrap_write</a><code>(3), cgiwrap_getenv</code> </p>
<h2>Index</h2>
