---
title: "ne_get_response_header(3)"
name: "ne_get_response_header"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_get_response_header/"
description: "ne_get_response_header, ne_response_header_iterate – functions to access response headers"
---

<p>ne_get_response_header, ne_response_header_iterate &#8211; functions to access response headers</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_request.h&gt;

const char *ne_get_response_header(ne_request *request, const char *name);

void *ne_response_header_iterate(ne_request *request, void *cursor, const char **name, const char **value);</code></pre>
<h2>Description</h2>
<dd>To retrieve the value of a response header field, the <code>ne_get_response_header</code> function can be used, and is given the name of the header to return. </p>
<p> To iterate over all the response headers returned, the <code>ne_response_header_iterate</code> function can be used. This function takes a <i>cursor</i> parameter which should be NULL to retrieve the first header. The function stores the name and value of the next header header in the <i>name</i> and <i>value</i> parameters, and returns a new cursor pointer which can be passed to <code>ne_response_header_iterate</code> to retrieve the next header.</p>
<h2>Return Value</h2>
<p><code>ne_get_response_header</code> returns a string, or NULL if no header with that name was given. If used during request processing, the return value pointer is valid only until the next call to <code>ne_begin_request</code>, or else, until the request object is destroyed. </p>
<p> Likewise, the cursor, names, and values returned by <code>ne_response_header_iterate</code> are only valid until the next call to <code>ne_begin_request</code> or until the request object is destroyed.</p>
<h2>Examples</h2>
<p>The following code will output the value of the Last-Modified header for a resource: </p>
<pre><code>ne_request *req = ne_request_create(sess, &quot;GET&quot;, &quot;/foo.txt&quot;);
if (ne_request_dispatch(req) == NE_OK) {
    const char *mtime = ne_get_response_header(req, &quot;Last-Modified&quot;);
    if (mtime) {
        printf(&quot;/foo.txt has last-modified value %s
&quot;, mtime);
    }
}
ne_request_destroy(req);</code></pre>
<h2>See Also</h2>
<p>ne_request_create, ne_request_destroy.</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
