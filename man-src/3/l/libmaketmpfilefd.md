---
title: "libmaketmpfilefd(3)"
name: "libmaketmpfilefd"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libmaketmpfilefd/"
description: "pm_make_tmpfile_fd() – create a temporary named file"
---

<h2 class="name">NAME</h2>
<p> pm_make_tmpfile_fd() &#8211; create a temporary named file</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netpbm/pm.h&gt;
pm_make_tmpfile(int *fdP,
                const char **filenameP);
</code></pre>
<h2>EXAMPLE</h2>
<p> This simple example creates a temporary file, writes &#8216;hello world&#8217; to it, then writes some search patterns to it, then uses it as input to <code>grep</code>: </p>
<pre><code>
#include &lt;netpbm/pm.h&gt;
int fd;
const char *myfilename;
pm_make_tmpfile_fd(&amp;fdP, &amp;myfilename);
write(fd, '^account:\s.*
', 16);
fprintf(fd, '^name:\s.*
', 13);
close(fd);
asprintfN(&amp;grepCommand, 'grep --file=' % s ' /tmp/infile &gt;/tmp/outfile');
system(grepCommand);
strfree(grepCommand);
unlink(myfilename);
strfree(myfilename);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This library function is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pm_make_tmpfile_fd()</code> is analogous to <code>pm_make_tmpfile()</code>(1) difference is that it opens the file as a low level file, as <code>open()</code> would, rather than as a stream, as <code>fopen()</code> would. </p>
<p> If you don&#8217;t need to access the file by name, use <code>pm_tmpfile_fd()</code> instead, because it&#8217;s cleaner. With <code>pm_tmpfile_fd()</code>, the operating system always deletes the temporary file when your program exits, if the program failed to clean up after itself. </p>
<h2>HISTORY</h2>
<p> <code>pm_tmpfile()</code> was introduced in Netpbm 10.42 (March 2008). </p>
<h2>Index</h2>
