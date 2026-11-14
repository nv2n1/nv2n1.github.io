---
title: "filter_create_fd(3)"
name: "filter_create_fd"
section: "3"
letter: "f"
url: "/docs/linux/man/3-filter_create_fd/"
description: "filter_create_fd – Create a sub process and return the requested pipes"
---

<h2 class="name">NAME</h2>
<p> filter_create_fd &#8211; Create a sub process and return the requested pipes </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;util/filter.h&gt;
</code></pre>
<pre><code>
NEOERR *filter_create_fd(const char *cmd, int *fdin, int *fdout, int *fderr,
                         pid_t *pid);
</code></pre>
<h2>ARGUMENTS</h2>
<p> cmd -&gt; the sub command to execute. Will be executed with<br />
 /bin/sh -c<br />
 fdin -&gt; pointer to return the stdin pipe, or NULL if you don&#8217;t<br />
 want the stdin pipe<br />
 fdout -&gt; pointer to return the stdout pipe, or NULL if you don&#8217;t<br />
 want the stdout pipe<br />
 fderr -&gt; pointer to return the stderr pipe, or NULL if you don&#8217;t<br />
 want the stderr pipe </p>
<h2>DESCRIPTION</h2>
<p> filter_create_fd and filter_create_fp are what popen </p>
<p> been: a mechanism to create sub processes and have pipes to all their input/output. The concept was taken from mutt, though python has something similar with popen3/popen4. You control which pipes the function returns by the fdin/fdout/fderr arguments. A NULL value means &quot;don&#8217;t create a pipe&quot;, a pointer to an int will cause the pipes to be created and the value of the file descriptor stored in the int. You will have to <a href="/docs/linux/man/2-close/">close</a>(2) the file descriptors yourself. </p>
<h2>RETURN VALUE</h2>
<p> fdin -&gt; the stdin file descriptor of the sub process<br />
 fdout -&gt; the stdout file descriptor of the sub process<br />
 fderr -&gt; the stderr file descriptor of the sub process<br />
 pid -&gt; the pid of the sub process </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-filter_wait/">filter_wait</a></code>(3), <a href="/docs/linux/man/3-filter_create_fp/">filter_create_fp</a><code>(3), filter_create_fd</code> </p>
<h2>Index</h2>
