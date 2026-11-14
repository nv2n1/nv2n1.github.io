---
title: "ares_process(3)"
name: "ares_process"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_process/"
description: "ares_process – Process events for name resolution"
---

<h2>NAME</h2>
<p> ares_process &#8211; Process events for name resolution</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
void ares_process(ares_channel channel, fd_set *read_fds,
</code></pre>
<p> <code>void ares_process_fd(ares_channel </code><i>channel</i>, <code>ares_socket_t </code><i>read_fd</i>,</p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-ares_process/">ares_process</a>(3)</code> function handles input/output events and timeouts associated with queries pending on the name service channel identified by <i>channel</i>. The file descriptor sets pointed to by <i>read_fds</i> and <i>write_fds</i> should have file descriptors set in them according to whether the file descriptors specified by <i><a href="/docs/linux/man/3-ares_fds/">ares_fds</a>(3)</i> are ready for reading and writing. (The easiest way to determine this information is to invoke <code>select</code> with a timeout no greater than the timeout given by <i><a href="/docs/linux/man/3-ares_timeout/">ares_timeout</a>(3)</i> ). </p>
<p> The <code>ares_process</code> function will invoke callbacks for pending queries if they complete successfully or fail. </p>
<p> <code><a href="/docs/linux/man/3-ares_process_fd/">ares_process_fd</a>(3)</code> works the same way but acts and operates only on the specific file descriptors (sockets) you pass in to the function. Use ARES_SOCKET_BAD for &quot;no action&quot;. This function is of course provided to allow users of c-ares to void select() in their applications and within c-ares.</p>
<h3>EXAMPLE</h3>
<p> The following code fragment waits for all pending queries on a channel to complete: </p>
<dl>
<dt>
<dd>
<pre><code>
int nfds, count;
fd_set readers, writers;
struct timeval tv, *tvp;
while (1) {
    FD_ZERO(&amp;readers);
    FD_ZERO(&amp;writers);
    nfds = ares_fds(channel, &amp;readers, &amp;writers);
    if (nfds == 0)
        break;
    tvp = ares_timeout(channel, NULL, &amp;tv);
    count = select(nfds, &amp;readers, &amp;writers, NULL, tvp);
    ares_process(channel, &amp;readers, &amp;writers);
}
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_fds/">ares_fds</a></code>(3), <code><a href="/docs/linux/man/3-ares_timeout/">ares_timeout</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
