---
title: "libssh2_keepalive_send(3)"
name: "libssh2_keepalive_send"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_keepalive_send/"
description: "libssh2_keepalive_send – short function description"
---

<h2>NAME</h2>
<p> libssh2_keepalive_send &#8211; short function description</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<pre><code>
int libssh2_keepalive_send(LIBSSH2_SESSION *session,
                           int *seconds_to_next);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Send a keepalive message if needed. <code>seconds_to_next</code> indicates how many seconds you can sleep after this call before you need to call it again.</p>
<h2>RETURN VALUE</h2>
<p> Returns 0 on success, or LIBSSH2_ERROR_SOCKET_SEND on I/O errors.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2.5</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_keepalive_config/">libssh2_keepalive_config</a>(3)</code> </p>
<h2>Index</h2>
