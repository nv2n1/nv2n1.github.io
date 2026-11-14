---
title: "upscli_fd(3)"
name: "upscli_fd"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_fd/"
description: "upscli_fd – Get file descriptor for connection"
---

<p>upscli_fd &#8211; Get file descriptor for connection</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
int upscli_fd(UPSCONN_t *ups);</code></pre>
<h2>Description</h2>
<p>The <code>upscli_fd()</code> function takes the pointer <i>ups</i> to a UPSCONN_t state structure and returns the value of the file descriptor for that connection, if any. </p>
<p> This may be useful for determining if the connection to <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) has been lost.</p>
<h2>Return Value</h2>
<p>The <code>upscli_fd()</code> function returns the file descriptor, which may be any non-negative number. It returns -1 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_connect/">upscli_connect</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
