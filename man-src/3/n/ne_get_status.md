---
title: "ne_get_status(3)"
name: "ne_get_status"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_get_status/"
description: "ne_get_status – retrieve HTTP response status for request"
---

<p>ne_get_status &#8211; retrieve HTTP response status for request</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_request.h&gt;

const ne_status *ne_get_status(const ne_request *request);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_get_status</code> function returns a pointer to the HTTP status object giving the result of a request. The object returned only becomes valid once the request has been <i>successfully</i> dispatched (the return value of <code>ne_request_dispatch</code> or <code>ne_begin_request</code> was zero). The object remains valid until the associated request object is destroyed.</p>
<h2>See Also</h2>
<p>ne_status, ne_request_create</p>
<h2>Example</h2>
<p>Display the response status code of applying the HEAD method to some resource. </p>
<pre><code>ne_request *req = ne_request_create(sess, &quot;HEAD&quot;, &quot;/foo/bar&quot;);
if (ne_request_dispatch(req))
    /* handle errors... */
    else printf(&quot;Response status code was %d
&quot;, ne_get_status(req)-&gt;code);
ne_request_destroy(req);</code></pre>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
