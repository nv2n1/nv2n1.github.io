---
title: "libssh2_poll(3)"
name: "libssh2_poll"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_poll/"
description: "libssh2_poll – poll for activity on a socket, channel or listener"
---

<h2>NAME</h2>
<p> libssh2_poll &#8211; poll for activity on a socket, channel or listener</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_poll(LIBSSH2_POLLFD *fds, unsigned int nfds, long timeout);</p>
<h2>DESCRIPTION</h2>
<p> This function is deprecated. Do note use. We encourage users to instead use the <i><a href="/docs/linux/man/3-poll/">poll</a>(3)</i> or <i><a href="/docs/linux/man/3-select/">select</a>(3)</i> functions to check for socket activity or when specific sockets are ready to get recevied from or send to. </p>
<p> Poll for activity on a socket, channel, listener, or any combination of these three types. The calling semantics for this function generally match <i><a href="/docs/linux/man/2-poll/">poll</a>(2)</i> however the structure of fds is somewhat more complex in order to accommodate the disparate datatypes, POLLFD constants have been namespaced to avoid platform discrepancies, and revents has additional values defined.</p>
<h2>RETURN VALUE</h2>
<p> Number of fds with interesting events.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_poll_channel_read/">libssh2_poll_channel_read</a>(3)</code> </p>
<h2>Index</h2>
