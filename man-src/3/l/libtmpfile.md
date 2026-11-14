---
title: "libtmpfile(3)"
name: "libtmpfile"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libtmpfile/"
description: "pm_tmpfile() – create a temporary unnamed file"
---

<h2 class="name">NAME</h2>
<p> pm_tmpfile() &#8211; create a temporary unnamed file</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netpbm/pm.h&gt;
FILE *
pm_tmpfile(void);
</code></pre>
<h2>EXAMPLE</h2>
<p> This simple example creates a temporary file, writes &#8216;hello world&#8217; to it, then reads back and prints those contents. </p>
<pre><code>
#include &lt;netpbm/pm.h&gt;
FILE *myfileP;
myfile = pm_tmpfile();
fprintf(myfile, 'hello world
');
fseek(myfileP, 0, SEEK_SET);
fread(buffer, sizeof(buffer), 1, myfileP);
fprintf(STDOUT, 'temp file contains ' % s '
', buffer);
fclose(myfileP);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This library function is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pm_tmpfile()</code> creates and opens an unnamed temporary file. It is basically the same thing as the standard C library <code>tmpfile()</code> function, except that it uses the <code>TMPFILE</code> environment variable to decide where to create the temporary file. If <code>TMPFILE</code> is not set or is set to something unusable (e.g. too long), <code>pm_tmpfile()</code> falls back to the value of the standard C library symbol <code>P_tmpdir</code>, just like <code>tmpfile()</code>. </p>
<p> Unlike <code>tmpfile()</code>, <code>pm_tmpfile()</code> never returns NULL. If it fails, it issues a message to Standard Error and aborts the program, like most libnetpbm routines do. </p>
<p> If you need to refer to the temporary file by name, use <code>pm_make_tmpfile()</code> instead. </p>
<h2>HISTORY</h2>
<p> <code>pm_tmpfile()</code> was introduced in Netpbm 10.20 (January 2004). </p>
<h2>Index</h2>
