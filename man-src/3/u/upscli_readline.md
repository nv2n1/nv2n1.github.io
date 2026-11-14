---
title: "upscli_readline(3)"
name: "upscli_readline"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_readline/"
description: "upscli_readline – read a single response from a UPS"
---

<p>upscli_readline &#8211; read a single response from a UPS</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
int upscli_readline(UPSCONN_t *ups, char *buf, size_t buflen);</code></pre>
<h2>Description</h2>
<p>The <code>upscli_readline()</code> function takes the pointer <i>ups</i> to a UPSCONN_t state structure, receives a single line from the server, and copies up to <i>buflen</i> bytes of the response into the buffer <i>buf</i>. </p>
<p> Some parsing of the string occurs during reception. In particular, ERR messages from <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) are detected and will cause this function to return -1.</p>
<h2>Return Value</h2>
<p>The <code>upscli_readline()</code> function returns 0 on success, or -1 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3), <code><a href="/docs/linux/man/3-upscli_get/">upscli_get</a></code>(3), <code><a href="/docs/linux/man/3-upscli_readline/">upscli_readline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_sendline/">upscli_sendline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_ssl/">upscli_ssl</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
