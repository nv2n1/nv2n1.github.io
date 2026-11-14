---
title: "filter_wait(3)"
name: "filter_wait"
section: "3"
letter: "f"
url: "/docs/linux/man/3-filter_wait/"
description: "filter_wait – wrap waitpid to decode the exitcode and why your filter quit"
---

<h2 class="name">NAME</h2>
<p> filter_wait &#8211; wrap waitpid to decode the exitcode and why your filter quit </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;util/filter.h&gt;
</code></pre>
<pre><code>
NEOERR *filter_wait(pid_t pid, int options, int *exitcode);
</code></pre>
<h2>ARGUMENTS</h2>
<p> pid -&gt; the process identifier to wait for<br />
 options -&gt; the options to pass to waitpid (see <a href="/docs/linux/man/2-wait/">wait</a>(2)) </p>
<h2>DESCRIPTION</h2>
<p> filter_wait wraps the waitpid call and raises an error (with description) if the call failed. Note that if the ask for the exitcode and the process exited with a code other than zero, we don&#8217;t raise an error. If you don&#8217;t ask for the exitcode, and it is non-zero, we raise an error </p>
<h2>RETURN VALUE</h2>
<p> exitcode -&gt; the exitcode if the process existed normally </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-filter_wait/">filter_wait</a></code>(3), <a href="/docs/linux/man/3-filter_create_fp/">filter_create_fp</a><code>(3), filter_create_fd</code> </p>
<h2>Index</h2>
