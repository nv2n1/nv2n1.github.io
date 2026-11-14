---
title: "libssh2_sftp_get_channel(3)"
name: "libssh2_sftp_get_channel"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_get_channel/"
description: "libssh2_sftp_get_channel – return the channel of sftp"
---

<h2>NAME</h2>
<p> libssh2_sftp_get_channel &#8211; return the channel of sftp</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#include &lt;libssh2_sftp.h&gt;
</code></pre>
<p> LIBSSH2_CHANNEL *libssh2_sftp_get_channel(LIBSSH2_SFTP *sftp);</p>
<h2>DESCRIPTION</h2>
<p> <i>sftp</i> &#8211; SFTP instance as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<p> Return the channel of the given sftp handle.</p>
<h2>RETURN VALUE</h2>
<p> The channel of the SFTP instance or NULL if something was wrong.</p>
<h2>AVAILABILITY</h2>
<p> Added in 1.4.0</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<h2>Index</h2>
