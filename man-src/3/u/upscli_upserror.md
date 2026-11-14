---
title: "upscli_upserror(3)"
name: "upscli_upserror"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_upserror/"
description: "upscli_upserror – Get current error number for connection"
---

<p>upscli_upserror &#8211; Get current error number for connection</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
int upscli_upserror(UPSCONN_t *ups);</code></pre>
<h2>Description</h2>
<p>The <code>upscli_upserror</code>() function takes the pointer <i>ups</i> to a UPSCONN_t state structure and returns the value of the internal error number, if any. </p>
<p> This is typically used to check for certain error values like UPSCLI_ERR_UNKCOMMAND. That specific error can be used for detecting older versions of <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) which might not support a given command. </p>
<p> Some error messages have additional meanings, so you should use <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3) to obtain readable error messages.</p>
<h2>Return Value</h2>
<p>The <code>upscli_upserror</code>() function returns one of the UPSCLI_ERR_* values from upsclient.h, or 0 if no error has occurred.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_readline/">upscli_readline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_sendline/">upscli_sendline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3) </p>
