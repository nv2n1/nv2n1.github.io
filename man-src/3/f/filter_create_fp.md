---
title: "filter_create_fp(3)"
name: "filter_create_fp"
section: "3"
letter: "f"
url: "/docs/linux/man/3-filter_create_fp/"
description: "filter_create_fp – similar to filter_create_fd except with buffered FILE*"
---

<h2 class="name">NAME</h2>
<p> filter_create_fp &#8211; similar to filter_create_fd except with buffered FILE* </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;util/filter.h&gt;
</code></pre>
<pre><code>
NEOERR *filter_create_fp(const char *cmd, FILE **in, FILE **out, FILE **err,
                         pid_t *pid);
</code></pre>
<h2>ARGUMENTS</h2>
<p> cmd -&gt; the sub command to execute. Will be executed with<br />
 /bin/sh -c<br />
 in -&gt; pointer to return the stdin pipe, or NULL if you don&#8217;t<br />
 want the stdin pipe<br />
 out -&gt; pointer to return the stdout pipe, or NULL if you don&#8217;t<br />
 want the stdout pipe<br />
 err -&gt; pointer to return the stderr pipe, or NULL if you don&#8217;t<br />
 want the stderr pipe </p>
<h2>DESCRIPTION</h2>
<p> filter_create_fp is identical to filter_create_fd, except each of the pipes is wrapped in a buffered stdio FILE </p>
<h2>RETURN VALUE</h2>
<p> in -&gt; the stdin FILE of the sub process<br />
 out -&gt; the stdout FILE of the sub process<br />
 err -&gt; the stderr FILE of the sub process<br />
 pid -&gt; the pid of the sub process </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-filter_wait/">filter_wait</a></code>(3), <a href="/docs/linux/man/3-filter_create_fp/">filter_create_fp</a><code>(3), filter_create_fd</code> </p>
<h2>Index</h2>
