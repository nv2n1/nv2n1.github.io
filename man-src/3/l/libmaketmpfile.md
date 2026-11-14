---
title: "libmaketmpfile(3)"
name: "libmaketmpfile"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libmaketmpfile/"
description: "pm_make_tmpfile() – create a temporary named file"
---

<h2 class="name">NAME</h2>
<p> pm_make_tmpfile() &#8211; create a temporary named file</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netpbm/pm.h&gt;
pm_make_tmpfile(FILE **fileP,
                const char **filenameP);
</code></pre>
<h2>EXAMPLE</h2>
<p> This simple example creates a temporary file, writes &#8216;hello world&#8217; to it, then writes some search patterns to it, then uses it as input to <code>grep</code>: </p>
<pre><code>
#include &lt;netpbm/pm.h&gt;
FILE *myfileP;
const char *myfilename;
pm_make_tmpfile(&amp;myfileP, &amp;myfilename);
fprintf(myfile, '^account:\s.*
');
fprintf(myfile, '^name:\s.*
');
fclose(myFileP);
asprintfN(&amp;grepCommand, 'grep --file=' % s ' /tmp/infile &gt;/tmp/outfile');
system(grepCommand);
strfree(grepCommand);
unlink(myfilename);
strfree(myfilename);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This library function is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pm_make_tmpfile()</code> creates and opens a temporary file, returning to you a stream file handle for it and its name. </p>
<p> <code>pm_make_tmpfile()</code> chooses a file name that is not already in use, with proper interlocking to make sure that it actually creates a file and opens the new file, as opposed to merely opening an existing file. </p>
<p> If you don&#8217;t need to access the file by name, use <code>pm_tmpfile()</code> instead, because it&#8217;s cleaner. With <code>pm_tmpfile()</code>, the operating system always deletes the temporary file when your program exits, if the program failed to clean up after itself. </p>
<p> The temporary file goes in the directory named by the <code>TMPFILE</code> environment variable. If <code>TMPFILE</code> is not set or is set to something unusable (e.g. too long), <code>pm_tmpfile()</code> falls back to the value of the standard C library symbol <code>P_tmpdir</code> (like the standard C library&#8217;s <code>tmpfile()</code>). </p>
<p> The name of the file within that directory is like <code>myprog_blrfx</code>, where <code>myprog</code> is the name of your program (arg 0) and the rest is an arbitrary discriminator. </p>
<p> If <code>pm_make_tmpfile()</code> is unable to create a temporary file, it issues a message to Standard Error and aborts the program. </p>
<h2>HISTORY</h2>
<p> <code>pm_tmpfile()</code> was introduced in Netpbm 10.27 (March 2005). </p>
<h2>Index</h2>
