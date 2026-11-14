---
title: "libssh2_session_get_timeout(3)"
name: "libssh2_session_get_timeout"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_get_timeout/"
description: "libssh2_session_get_timeout – get the timeout for blocking functions"
---

<h2>NAME</h2>
<p> libssh2_session_get_timeout &#8211; get the timeout for blocking functions</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<pre><code>
long libssh2_session_get_timeout(LIBSSH2_SESSION *session);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Returns the <code>timeout</code> (in milliseconds) for how long a blocking the libssh2 function calls may wait until they consider the situation an error and return LIBSSH2_ERROR_TIMEOUT. </p>
<p> By default libssh2 has no timeout (zero) for blocking functions.</p>
<h2>RETURN VALUE</h2>
<p> The value of the timeout setting.</p>
<h2>AVAILABILITY</h2>
<p> Added in 1.2.9</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_set_timeout/">libssh2_session_set_timeout</a>(3)</code> </p>
<h2>Index</h2>
