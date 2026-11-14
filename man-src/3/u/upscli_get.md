---
title: "upscli_get(3)"
name: "upscli_get"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_get/"
description: "upscli_get – retrieve data from a UPS"
---

<p>upscli_get &#8211; retrieve data from a UPS</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;</code></pre>
<pre>int upscli_get(UPSCONN_t *ups, int numq, const char **query,
 int *numa, char ***answer)</pre>
<h2>Description</h2>
<p>The <code>upscli_get()</code> function takes the pointer <i>ups</i> to a UPSCONN_t state structure, and the pointer <i>query</i> to an array of <i>numq</i> query elements. It builds a properly-formatted request from those elements and transmits it to <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8). </p>
<p> Upon success, the response will be split into separate components. A pointer to those components will be returned in <i>answer</i>. The number of usable answer components will be returned in <i>numa</i>.</p>
<h2>Uses</h2>
<p>This function implements the &quot;GET&quot; command in the protocol. As a result, you can use it to request many different things from the server. Some examples are: </p>
<dl>
<dd>&bull; GET NUMLOGINS &lt;ups&gt;</dl>
<dl>
<dd>&bull; GET UPSDESC &lt;ups&gt;</dl>
<dl>
<dd>&bull; GET VAR &lt;ups&gt; &lt;var&gt;</dl>
<dl>
<dd>&bull; GET TYPE &lt;ups&gt; &lt;var&gt;</dl>
<dl>
<dd>&bull; GET DESC &lt;ups&gt; &lt;var&gt;</dl>
<dl>
<dd>&bull; GET CMDDESC &lt;ups&gt; &lt;cmd&gt;</dl>
<h2>Query Formatting</h2>
<p>To generate a request for GET NUMLOGINS su700, you would populate query and numq as follows: </p>
<dl>
<dd>
<pre>int numq;
const char *query[2];</pre>
</dl>
<dl>
<dd>
<pre>query[0] = &quot;NUMLOGINS&quot;;
query[1] = &quot;su700&quot;;
numq = 2;</pre>
</dl>
<p> All escaping of special characters and quoting of elements with spaces is handled for you inside this function.</p>
<h2>Answer Formatting</h2>
<p>The raw response from upsd to the above query would be NUMLOGINS su700 1. Since this is split up for you, the values work out like this: </p>
<dl>
<dd>
<pre>numa = 3;
answer[0] = &quot;NUMLOGINS&quot;
answer[1] = &quot;su700&quot;
answer[2] = &quot;1&quot;</pre>
</dl>
<p> Notice that the value which you seek typically starts at answer[numq].</p>
<h2>Error Checking</h2>
<p>This function will check your query against the response from <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8). For example, if you send &quot;VAR&quot; &quot;su700&quot; &quot;ups.status&quot;, it will expect to see those at the beginning of the response. </p>
<p> If the results from <code>upsd</code> do not pass this case-insensitive test against your request, this function will return an error. When this happens, <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) will return <i>UPSCLI_ERR_PROTOCOL</i>.</p>
<h2>Answer Array Lifetime</h2>
<p>The pointers contained within the <i>answer</i> array are only valid until the next call to a <i>upsclient</i> function which references them. If you need to use data from multiple calls, you must copy it somewhere else first. </p>
<p> The <i>answer</i> array and its elements may change locations, so you must not rely on previous addresses. You must only use the addresses which were returned by the most recent call. You also must not attempt to use more than <i>numa</i> elements in <i>answer</i>. Such behavior is undefined, and may yield bogus data or a crash. </p>
<p> The array will be deleted after calling <code><a href="/docs/linux/man/3-upscli_disconnect/">upscli_disconnect</a></code>(3). Any access after that point is also undefined.</p>
<h2>Return Value</h2>
<p>The <code>upscli_get()</code> function returns 0 on success, or -1 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_list_start/">upscli_list_start</a></code>(3), <code><a href="/docs/linux/man/3-upscli_list_next/">upscli_list_next</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
