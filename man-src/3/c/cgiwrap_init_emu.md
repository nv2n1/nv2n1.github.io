---
title: "cgiwrap_init_emu(3)"
name: "cgiwrap_init_emu"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgiwrap_init_emu/"
description: "cgiwrap_init_emu – initialize cgiwrap for emulated use"
---

<h2 class="name">NAME</h2>
<p> cgiwrap_init_emu &#8211; initialize cgiwrap for emulated use </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgiwrap.h&gt;
</code></pre>
<pre><code>
void cgiwrap_init_emu(void *data, READ_FUNC read_cb,
                      WRITEF_FUNC writef_cb, WRITE_FUNC write_cb, GETENV_FUNC getenv_cb,
                      PUTENV_FUNC putenv_cb, ITERENV_FUNC iterenv_cb);
</code></pre>
<h2>ARGUMENTS</h2>
<p> data &#8211; user data to be passed to the specified callbacks<br />
 read_cb &#8211; a cb to replace fread(stdin)<br />
 writef_cb &#8211; a cb to repalce fprintf(stdout)<br />
 write_cb &#8211; a cb to replace fwrite(stdout)<br />
 getenv_cb &#8211; a cb to replace getenv<br />
 putenv_cb &#8211; a cb to replace putenv<br />
 iterenv_cb &#8211; a cb to replace the default environment iteration<br />
 function (which just wraps walking the envp array) </p>
<h2>DESCRIPTION</h2>
<p> cgiwrap_init_emu sets up the cgiwrap subsystem for use in an emulated environment where you are providing routines to use in place of the standard routines, ie when used to interface with a server or scripting language. See cgi/cgiwrap.h for the exact definitions of the callback functions. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgiwrap_iterenv/">cgiwrap_iterenv</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_putenv/">cgiwrap_putenv</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_emu/">cgiwrap_init_emu</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writef/">cgiwrap_writef</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_std/">cgiwrap_init_std</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writevf/">cgiwrap_writevf</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_read/">cgiwrap_read</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_write/">cgiwrap_write</a><code>(3), cgiwrap_getenv</code> </p>
<h2>Index</h2>
