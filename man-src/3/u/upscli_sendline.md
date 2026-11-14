---
title: "upscli_sendline(3)"
name: "upscli_sendline"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_sendline/"
description: "upscli_sendline – send a single command to a UPS"
---

<p>upscli_sendline &#8211; send a single command to a UPS</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
int upscli_sendline(UPSCONN_t *ups, const char *buf, size_t buflen);</code></pre>
<h2>Description</h2>
<p>The <code>upscli_sendline()</code> function takes the pointer <i>ups</i> to a UPSCONN_t state structure and transmits a buffer <i>buf</i> of size <i>buflen</i> to the server. </p>
<p> The data in <i>buf</i> must be a fully formatted protocol command as no parsing of the buffer occurs within this function.</p>
<h2>Return Value</h2>
<p>The <code>upscli_sendline()</code> function returns 0 on success, or -1 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3), <code><a href="/docs/linux/man/3-upscli_get/">upscli_get</a></code>(3), <code><a href="/docs/linux/man/3-upscli_readline/">upscli_readline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_sendline/">upscli_sendline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_ssl/">upscli_ssl</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
