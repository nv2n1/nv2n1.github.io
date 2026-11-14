---
title: "upscli_list_next(3)"
name: "upscli_list_next"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_list_next/"
description: "upscli_list_next – retrieve list items from a UPS"
---

<p>upscli_list_next &#8211; retrieve list items from a UPS</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;</code></pre>
<pre>int upscli_list_next(UPSCONN_t *ups, int numq, const char **query,
 int *numa, char ***answer)</pre>
<h2>Description</h2>
<p>The <code>upscli_list_next()</code> function takes the pointer <i>ups</i> to a UPSCONN_t state structure, and the pointer <i>query</i> to an array of <i>numq</i> query elements. It performs a read from the network and expects to find either another list item or the end of a list. </p>
<p> You must call <code><a href="/docs/linux/man/3-upscli_list_start/">upscli_list_start</a></code>(3) before calling this function. </p>
<p> This function will return 1 and set values in <i>numa</i> and <i>answer</i> if a list item is received. If the list is done, it will return 0, and the values in <i>numa</i> and <i>answer</i> are undefined. </p>
<p> Calling this function after it returns something other than 1 is undefined.</p>
<h2>Query Formatting</h2>
<p>You may not change the values of <i>numq</i> or <i>query</i> between the call to <code><a href="/docs/linux/man/3-upscli_list_start/">upscli_list_start</a></code>(3) and the first call to this function. You also may not change the values between calls to this function.</p>
<h2>Answer Formatting</h2>
<p>The contents of <i>numa</i> and <i>answer</i> work just like a call to <code><a href="/docs/linux/man/3-upscli_get/">upscli_get</a></code>(3). The values returned by <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) are identical to a single item request, so this is not surprising.</p>
<h2>Error Checking</h2>
<p>This function checks the response from <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) against your query. If the response is not part of the list you have requested, it will return an error code. </p>
<p> When this happens, <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) will return UPSCLI_ERR_PROTOCOL.</p>
<h2>Return Value</h2>
<p>The <code>upscli_list_next()</code> function returns 1 when list data is present, 0 if the list is finished, or -1 if an error occurs. </p>
<p> It is possible to have an empty list. The function will return 0 for its first call in that case.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_list_start/">upscli_list_start</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
