---
title: "cgiwrap_iterenv(3)"
name: "cgiwrap_iterenv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgiwrap_iterenv/"
description: "cgiwrap_iterenv – iterater for env vars"
---

<h2 class="name">NAME</h2>
<p> cgiwrap_iterenv &#8211; iterater for env vars </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgiwrap.h&gt;
</code></pre>
<pre><code>
NEOERR *cgiwrap_iterenv(int n, char **k, char **v);
</code></pre>
<h2>ARGUMENTS</h2>
<p> n &#8211; variable to return. This should start at 0 and increment<br />
 until you receive a NULL return value. </p>
<h2>DESCRIPTION</h2>
<p> cgiwrap_iterenv allows a program to iterate over all the environment variables. This is probably mostly used by the default debug output. </p>
<h2>RETURN VALUE</h2>
<p> k &#8211; a malloc&#8217;d copy of the variable name<br />
 v &#8211; a malloc&#8217;d copy of the variable value </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgiwrap_iterenv/">cgiwrap_iterenv</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_putenv/">cgiwrap_putenv</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_emu/">cgiwrap_init_emu</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writef/">cgiwrap_writef</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_std/">cgiwrap_init_std</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writevf/">cgiwrap_writevf</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_read/">cgiwrap_read</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_write/">cgiwrap_write</a><code>(3), cgiwrap_getenv</code> </p>
<h2>Index</h2>
