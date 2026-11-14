---
title: "ares_fds(3)"
name: "ares_fds"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_fds/"
description: "ares_fds – Get file descriptors to select on for name service"
---

<h2>NAME</h2>
<p> ares_fds &#8211; Get file descriptors to select on for name service</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_fds(ares_channel channel, fd_set *read_fds,
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_fds</code> function retrieves the set of file descriptors which the calling application should select on for reading and writing for the processing of name service queries pending on the name service channel identified by <i>channel</i>. File descriptors will be set in the file descriptor sets pointed to by <i>read_fds</i> and <i>write_fds</i> as appropriate. File descriptors already set in <i>read_fds</i> and <i>write_fds</i> will remain set; initialization of the file descriptor sets (using <code>FD_ZERO</code>) is the responsibility of the caller.</p>
<h2>RETURN VALUES</h2>
<p> <code>ares_fds</code> returns one greater than the number of the highest socket set in either <i>read_fds</i> or <i>write_fds</i>. If no queries are active, <code>ares_fds</code> will return 0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_timeout/">ares_timeout</a></code>(3), <code><a href="/docs/linux/man/3-ares_process/">ares_process</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
