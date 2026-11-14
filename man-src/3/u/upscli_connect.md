---
title: "upscli_connect(3)"
name: "upscli_connect"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_connect/"
description: "upscli_connect – Open a connection to a NUT upsd"
---

<p>upscli_connect &#8211; Open a connection to a NUT upsd</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
int upscli_connect(UPSCONN_t *ups, const char *host, int port, int flags);</code></pre>
<h2>Description</h2>
<p>The <code>upscli_connect()</code> function takes the pointer <i>ups</i> to a UPSCONN_t state structure and opens a TCP connection to the <i>host</i> on the given <i>port</i>. </p>
<p> <i>flags</i> may be either UPSCLI_CONN_TRYSSL to try a SSL connection, or UPSCLI_CONN_REQSSL to require a SSL connection. </p>
<p> If SSL mode is required, this function will only return successfully if it is able to establish a SSL connection with the server. Possible reasons for failure include no SSL support on the server, and if <code>upsclient</code> itself hasn&#8217;t been compiled with SSL support. </p>
<p> You must call <code><a href="/docs/linux/man/3-upscli_disconnect/">upscli_disconnect</a></code>(3) when finished with a connection, or your program will slowly leak memory and file descriptors.</p>
<h2>Return Value</h2>
<p>The <code>upscli_connect()</code> function modifies the UPSCONN_t structure and returns 0 on success, or -1 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_disconnect/">upscli_disconnect</a></code>(3), <code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3), <code><a href="/docs/linux/man/3-upscli_splitaddr/">upscli_splitaddr</a></code>(3), <code><a href="/docs/linux/man/3-upscli_splitname/">upscli_splitname</a></code>(3), <code><a href="/docs/linux/man/3-upscli_ssl/">upscli_ssl</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
