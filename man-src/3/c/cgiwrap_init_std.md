---
title: "cgiwrap_init_std(3)"
name: "cgiwrap_init_std"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgiwrap_init_std/"
description: "cgiwrap_init_std – Initialize cgiwrap with default functions"
---

<h2 class="name">NAME</h2>
<p> cgiwrap_init_std &#8211; Initialize cgiwrap with default functions </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgiwrap.h&gt;
</code></pre>
<pre><code>
void cgiwrap_init_std(int argc, char **argv, char **envp);
</code></pre>
<h2>ARGUMENTS</h2>
<p> the arguments to main, namely argc/argv/envp </p>
<h2>DESCRIPTION</h2>
<p> cgiwrap_init_std will initialize the cgiwrap subsystem to use the default CGI functions, ie getenv/putenv/stdio. In reality, all this is doing is setting up the data for the cgiwrap_iterenv() function. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgiwrap_iterenv/">cgiwrap_iterenv</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_putenv/">cgiwrap_putenv</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_emu/">cgiwrap_init_emu</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writef/">cgiwrap_writef</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_std/">cgiwrap_init_std</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writevf/">cgiwrap_writevf</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_read/">cgiwrap_read</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_write/">cgiwrap_write</a><code>(3), cgiwrap_getenv</code> </p>
<h2>Index</h2>
