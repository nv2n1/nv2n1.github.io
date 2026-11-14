---
title: "libssh2_keepalive_config(3)"
name: "libssh2_keepalive_config"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_keepalive_config/"
description: "libssh2_keepalive_config – short function description"
---

<h2>NAME</h2>
<p> libssh2_keepalive_config &#8211; short function description</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<pre><code>
void libssh2_keepalive_config(LIBSSH2_SESSION *session,
                              int want_reply,
                              unsigned interval);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Set how often keepalive messages should be sent. <code>want_reply</code> indicates whether the keepalive messages should request a response from the server. <code>interval</code> is number of seconds that can pass without any I/O, use 0 (the default) to disable keepalives. To avoid some busy-loop corner-cases, if you specify an interval of 1 it will be treated as 2. </p>
<p> Note that non-blocking applications are responsible for sending the keepalive messages using <code><a href="/docs/linux/man/3-libssh2_keepalive_send/">libssh2_keepalive_send</a>(3)</code>.</p>
<h2>RETURN VALUE</h2>
<p> Nothing</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2.5</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_keepalive_send/">libssh2_keepalive_send</a>(3)</code> </p>
<h2>Index</h2>
