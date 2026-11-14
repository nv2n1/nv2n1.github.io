---
title: "upscli_strerror(3)"
name: "upscli_strerror"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_strerror/"
description: "upscli_strerror – return string describing error condition"
---

<p>upscli_strerror &#8211; return string describing error condition</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
char *upscli_strerror(UPSCONN_t *ups);</code></pre>
<h2>Description</h2>
<p>The <code>upscli_strerror</code>() function takes the pointer <i>ups</i> to a UPSCONN_t state structure and returns a string describing the last error which occurred on this connection. The string is valid until the next call to <code>upscli_strerror</code>().</p>
<h2>Return Value</h2>
<p>The <code>upscli_strerror</code>() function returns a description of the error, or an unknown error message if the error code is not recognized.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3), <code><a href="/docs/linux/man/3-upscli_get/">upscli_get</a></code>(3), <code><a href="/docs/linux/man/3-upscli_readline/">upscli_readline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_sendline/">upscli_sendline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_ssl/">upscli_ssl</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
