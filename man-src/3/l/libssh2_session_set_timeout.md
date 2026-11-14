---
title: "libssh2_session_set_timeout(3)"
name: "libssh2_session_set_timeout"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_set_timeout/"
description: "libssh2_session_set_timeout – set timeout for blocking functions"
---

<h2>NAME</h2>
<p> libssh2_session_set_timeout &#8211; set timeout for blocking functions</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<pre><code>
void libssh2_session_set_timeout(LIBSSH2_SESSION *session, long timeout);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Set the <code>timeout</code> in milliseconds for how long a blocking the libssh2 function calls may wait until they consider the situation an error and return LIBSSH2_ERROR_TIMEOUT. </p>
<p> By default or if you set the timeout to zero, libssh2 has no timeout for blocking functions.</p>
<h2>RETURN VALUE</h2>
<p> Nothing</p>
<h2>AVAILABILITY</h2>
<p> Added in 1.2.9</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_get_timeout/">libssh2_session_get_timeout</a>(3)</code> </p>
<h2>Index</h2>
