---
title: "cgiwrap_read(3)"
name: "cgiwrap_read"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgiwrap_read/"
description: "cgiwrap_read – cgiwrap input function"
---

<h2 class="name">NAME</h2>
<p> cgiwrap_read &#8211; cgiwrap input function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgiwrap.h&gt;
</code></pre>
<pre><code>
void cgiwrap_read(char *buf, int buf_len, int *read_len);
</code></pre>
<h2>ARGUMENTS</h2>
<p> buf &#8211; a pre-allocated buffer to read the data into<br />
 buf_len &#8211; the size of the pre-allocated buffer </p>
<h2>DESCRIPTION</h2>
<p> cgiwrap_read is used to read incoming data from the client, usually from a POST or PUT HTTP request. It wraps the part of fread(stdin). </p>
<h2>RETURN VALUE</h2>
<p> read_len &#8211; the number of bytes read into buf </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgiwrap_iterenv/">cgiwrap_iterenv</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_putenv/">cgiwrap_putenv</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_emu/">cgiwrap_init_emu</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writef/">cgiwrap_writef</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_init_std/">cgiwrap_init_std</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_writevf/">cgiwrap_writevf</a><code>(3), <a href="/docs/linux/man/3-cgiwrap_read/">cgiwrap_read</a></code>(3), <a href="/docs/linux/man/3-cgiwrap_write/">cgiwrap_write</a><code>(3), cgiwrap_getenv</code> </p>
<h2>Index</h2>
