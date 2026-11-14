---
title: "libtmpfilefd(3)"
name: "libtmpfilefd"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libtmpfilefd/"
description: "pm_tmpfile_fd() – create a temporary unnamed file"
---

<h2 class="name">NAME</h2>
<p> pm_tmpfile_fd() &#8211; create a temporary unnamed file</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netpbm/pm.h&gt;
FILE *
pm_tmpfile_fd(void);
</code></pre>
<h2>EXAMPLE</h2>
<p> This simple example creates a temporary file, writes &#8216;hello world&#8217; to it, then reads back and prints those contents. </p>
<pre><code>
#include &lt;netpbm/pm.h&gt;
int fd;
fd = pm_tmpfile();
write(fd, 'hello world
', 17);
lseek(fd, 0, SEEK_SET);
read(fd, buffer, sizeof(buffer));
fprintf(STDOUT, 'temp file contains ' % s '
', buffer);
close(fd);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This library function is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pm_tmpfile_fd()</code> is analogous to <code>pm_tmpfile()</code>(1) that it opens the file as a low level file, as <code>open()</code> would, rather than as a stream, as <code>fopen()</code> would. </p>
<p> If you need to refer to the temporary file by name, use <code>pm_make_tmpfile_fd()</code> instead. </p>
<h2>HISTORY</h2>
<p> <code>pm_tmpfile()</code> was introduced in Netpbm 10.42 (March 2008). </p>
<h2>Index</h2>
