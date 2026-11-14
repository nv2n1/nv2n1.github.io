---
title: "cgiwrap_writef(3)"
name: "cgiwrap_writef"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgiwrap_writef/"
description: "cgiwrap_writef – a wrapper for printf"
---

<h2 class="name">NAME</h2>
<p> cgiwrap_writef &#8211; a wrapper for printf </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgiwrap.h&gt;
</code></pre>
<pre><code>
NEOERR *cgiwrap_writef(const char *fmt, ...)
    ATTRIBUTE_PRINTF(1, 2);
</code></pre>
<h2>ARGUMENTS</h2>
<p> fmt &#8211; standard printf fmt string and args </p>
<h2>DESCRIPTION</h2>
<p> cgiwrap_writef is the formatted output command that replaces printf or fprintf(stdout) in a standard CGI </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgiwrap_iterenv/">cgiwrap_iterenv</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_putenv/">cgiwrap_putenv</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_emu/">cgiwrap_init_emu</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writef/">cgiwrap_writef</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_std/">cgiwrap_init_std</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writevf/">cgiwrap_writevf</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_read/">cgiwrap_read</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_write/">cgiwrap_write</a><code>(3), cgiwrap_getenv</code> </p>
<h2>Index</h2>
