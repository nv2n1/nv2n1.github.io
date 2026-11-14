---
title: "cgiwrap_getenv(3)"
name: "cgiwrap_getenv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgiwrap_getenv/"
description: "cgiwrap_getenv – the wrapper for getenv"
---

<h2 class="name">NAME</h2>
<p> cgiwrap_getenv &#8211; the wrapper for getenv </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgiwrap.h&gt;
</code></pre>
<pre><code>
NEOERR *cgiwrap_getenv(const char *k, char **v);
</code></pre>
<h2>ARGUMENTS</h2>
<p> k &#8211; the environment variable to lookup </p>
<h2>DESCRIPTION</h2>
<p> cgiwrap_getenv wraps the getenv function for access to environment variables, which are used to pass data to CGI scripts. This version differs from the system getenv in that it makes a copy of the value it returns, which gets around problems when wrapping this routine in garbage collected/reference counted languages by moving the ownership of the data to the calling function. </p>
<h2>RETURN VALUE</h2>
<p> v &#8211; a newly allocated copy of the value of that variable, or<br />
 NULL if not found. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgiwrap_iterenv/">cgiwrap_iterenv</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_putenv/">cgiwrap_putenv</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_emu/">cgiwrap_init_emu</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writef/">cgiwrap_writef</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_std/">cgiwrap_init_std</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writevf/">cgiwrap_writevf</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_read/">cgiwrap_read</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_write/">cgiwrap_write</a><code>(3), cgiwrap_getenv</code> </p>
<h2>Index</h2>
