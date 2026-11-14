---
title: "upscli_ssl(3)"
name: "upscli_ssl"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_ssl/"
description: "upscli_ssl – Check SSL mode for current connection"
---

<p>upscli_ssl &#8211; Check SSL mode for current connection</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
int upscli_ssl(UPSCONN_t *ups);</code></pre>
<h2>Description</h2>
<p>The <code>upscli_ssl</code>() function takes the pointer <i>ups</i> to a UPSCONN_t state structure. It only returns 1 if SSL support has been compiled into the <code><a href="/docs/linux/man/3-upsclient/">upsclient</a></code>(3) library, and if it was successfully enabled for this connection.</p>
<h2>Return Value</h2>
<p>The <code>upscli_ssl</code>() function returns 1 if SSL is running, and 0 if not. It returns -1 in the event of an error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3), <code><a href="/docs/linux/man/3-upscli_get/">upscli_get</a></code>(3), <code><a href="/docs/linux/man/3-upscli_readline/">upscli_readline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_sendline/">upscli_sendline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
