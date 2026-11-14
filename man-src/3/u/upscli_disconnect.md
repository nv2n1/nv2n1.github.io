---
title: "upscli_disconnect(3)"
name: "upscli_disconnect"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_disconnect/"
description: "upscli_disconnect – disconnect from a UPS server"
---

<p>upscli_disconnect &#8211; disconnect from a UPS server</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
int upscli_disconnect(UPSCONN_t *ups);</code></pre>
<h2>Description</h2>
<p>The <code>upscli_disconnect()</code> function takes the pointer <i>ups</i> to a UPSCONN_t state structure, shuts down the connection to the server, and frees dynamic memory used by the state structure. The UPSCONN_t structure is no longer valid after this function is called. </p>
<p> This function must be called, or your program will leak memory and file descriptors.</p>
<h2>Return Value</h2>
<p>The <code>upscli_disconnect()</code> function returns 0 on success, or -1 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_connect/">upscli_connect</a></code>(3), <code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
