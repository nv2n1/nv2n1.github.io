---
title: "upscli_list_start(3)"
name: "upscli_list_start"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_list_start/"
description: "upscli_list_start – begin multi-item retrieval from a UPS"
---

<p>upscli_list_start &#8211; begin multi-item retrieval from a UPS</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;
int upscli_list_start(UPSCONN_t *ups, int numq, const char **query)</code></pre>
<h2>Description</h2>
<p>The <code>upscli_list_start()</code> function takes the pointer <i>ups</i> to a UPSCONN_t state structure, and the pointer <i>query</i> to an array of <i>numq</i> query elements. It builds a properly-formatted request from those elements and transmits it to <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8). </p>
<p> Upon success, the caller must call <code><a href="/docs/linux/man/3-upscli_list_next/">upscli_list_next</a></code>(3) to retrieve the elements of the list. Failure to retrieve the list will most likely result in the client getting out of sync with the server due to buffered data.</p>
<h2>Uses</h2>
<p>This function implements the &quot;LIST&quot; command in the protocol. As a result, you can use it to request many different things from the server. Some examples are: </p>
<dl>
<dd>&bull; LIST UPS</dl>
<dl>
<dd>&bull; LIST VAR &lt;ups&gt;</dl>
<dl>
<dd>&bull; LIST RW &lt;ups&gt;</dl>
<dl>
<dd>&bull; LIST CMD &lt;ups&gt;</dl>
<dl>
<dd>&bull; LIST ENUM &lt;ups&gt; &lt;var&gt;</dl>
<dl>
<dd>&bull; LIST RANGE &lt;ups&gt; &lt;var&gt;</dl>
<h2>Query Formatting</h2>
<p>To see the list of variables on a UPS called <i>su700</i>, the protocol command would be LIST VAR su700. To start that list with this function, you would populate query and numq as follows: </p>
<dl>
<dd>
<pre>int numq;
const char *query[2];</pre>
</dl>
<dl>
<dd>
<pre>query[0] = &quot;VAR&quot;;
query[1] = &quot;su700&quot;;
numq = 2;</pre>
</dl>
<p> All escaping of special characters and quoting of elements with spaces are handled for you inside this function.</p>
<h2>Error Checking</h2>
<p>This function checks the response from <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) against your query. If it is not starting a list, or is starting the wrong type of list, it will return an error code. </p>
<p> When this happens, <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) will return UPSCLI_ERR_PROTOCOL.</p>
<h2>Return Value</h2>
<p>The <code>upscli_list_start()</code> function returns 0 on success, or -1 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3), <code><a href="/docs/linux/man/3-upscli_get/">upscli_get</a></code>(3), <code><a href="/docs/linux/man/3-upscli_readline/">upscli_readline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_sendline/">upscli_sendline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_ssl/">upscli_ssl</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
