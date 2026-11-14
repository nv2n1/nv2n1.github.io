---
title: "cgiwrap_putenv(3)"
name: "cgiwrap_putenv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgiwrap_putenv/"
description: "cgiwrap_putenv – wrap the putenv call"
---

<h2 class="name">NAME</h2>
<p> cgiwrap_putenv &#8211; wrap the putenv call </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgiwrap.h&gt;
</code></pre>
<pre><code>
NEOERR *cgiwrap_putenv(const char *k, const char *v);
</code></pre>
<h2>ARGUMENTS</h2>
<p> k &#8211; the env var name<br />
 v &#8211; the new value for env var k </p>
<h2>DESCRIPTION</h2>
<p> cgiwrap_putenv wraps the putenv call. This is mostly used by the cgi_debug_init function to create an artificial environment. This version differs from the system version by having separate arguments for the variable name and value, which makes life easier for the caller (usually), and keeps most wrapping callbacks from having to implement a parser to separate them. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgiwrap_iterenv/">cgiwrap_iterenv</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_putenv/">cgiwrap_putenv</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_emu/">cgiwrap_init_emu</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writef/">cgiwrap_writef</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_std/">cgiwrap_init_std</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writevf/">cgiwrap_writevf</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_read/">cgiwrap_read</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_write/">cgiwrap_write</a><code>(3), cgiwrap_getenv</code> </p>
<h2>Index</h2>
