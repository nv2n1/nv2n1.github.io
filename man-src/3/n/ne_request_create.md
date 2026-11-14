---
title: "ne_request_create(3)"
name: "ne_request_create"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_request_create/"
description: "ne_request_create, ne_request_dispatch, ne_request_destroy – low-level HTTP request handling"
---

<p>ne_request_create, ne_request_dispatch, ne_request_destroy &#8211; low-level HTTP request handling</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_request.h&gt;

ne_request *ne_request_create(ne_session *session, const char *method, const char *path);

int ne_request_dispatch(ne_request *req);

void ne_request_destroy(ne_request *req);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_request</code> object represents an HTTP request and the associated response. The <code>ne_request_create</code> function creates a new request object for the given <i>session</i>. The target resource for the request is identified by the <i>path</i>, and the method to be performed on that resource via the <i>method</i> parameter. </p>
<p> The <i>path</i> string used must conform to the abs_path definition given in RFC2396, with an optional &quot;?query&quot; part, and must be URI-escaped by the caller (for instance, using <code>ne_path_escape</code>). If the string comes from an untrusted source, failure to perform URI-escaping results in a security vulnerability. </p>
<p> To dispatch a request, and process the response, the <code>ne_request_dispatch</code> function can be used. An alternative is to use the (more complex, but more flexible) combination of the <code>ne_begin_request</code>, <code>ne_end_request</code>, and <code>ne_read_response_block</code> functions; see <code>ne_begin_request</code>. </p>
<p> To add extra headers in the request, the functions ne_add_request_header and ne_print_request_header can be used. To include a message body with the request, one of the functions <code>ne_set_request_body_buffer</code>, ne_set_request_body_fd, or <code>ne_set_request_body_provider</code> can be used. </p>
<p> The return value of <code>ne_request_dispatch</code> indicates merely whether the request was sent and the response read successfully. To discover the result of the operation, ne_get_status, along with any processing of the response headers and message body. </p>
<p> A request can only be dispatched once: calling <code>ne_request_dispatch</code> more than once on a single <code>ne_request</code> object produces undefined behaviour. Once all processing associated with the request object is complete, use the <code>ne_request_destroy</code> function to destroy the resources associated with it. Any subsequent use of the request object produces undefined behaviour. </p>
<p> If a request is being using a non-idempotent method such as POST, the NE_REQFLAG_IDEMPOTENT flag should be disabled; see ne_set_request_flag.</p>
<h2>Return Value</h2>
<p>The <code>ne_request_create</code> function returns a pointer to a request object (and never NULL). </p>
<p> The <code>ne_request_dispatch</code> function returns zero if the request was dispatched successfully, and a non-zero error code otherwise.</p>
<h2>Errors</h2>
<p><code>NE_ERROR</code></p>
<dl>
<dd>Request failed (see session error string)</dl>
<p> <code>NE_LOOKUP</code></p>
<dl>
<dd>The DNS lookup for the server (or proxy server) failed.</dl>
<p> <code>NE_AUTH</code></p>
<dl>
<dd>Authentication failed on the server.</dl>
<p> <code>NE_PROXYAUTH</code></p>
<dl>
<dd>Authentication failed on the proxy server.</dl>
<p> <code>NE_CONNECT</code></p>
<dl>
<dd>A connection to the server could not be established.</dl>
<p> <code>NE_TIMEOUT</code></p>
<dl>
<dd>A timeout occurred while waiting for the server to respond.</dl>
<h2>Example</h2>
<p>An example of applying a MKCOL operation to the resource at the location <a rel="nofollow" href="http://www.example.com/foo/bar/:">http://www.example.com/foo/bar/:</a> </p>
<pre><code>ne_session *sess = ne_session_create(&quot;http&quot;, &quot;www.example.com&quot;, 80);
ne_request *req = ne_request_create(sess, &quot;MKCOL&quot;, &quot;/foo/bar/&quot;);
if (ne_request_dispatch(req)) {
    printf(&quot;Request failed: %s
&quot;, ne_get_error(sess));
}
ne_request_destroy(req);</code></pre>
<h2>See Also</h2>
<p>ne_get_error, ne_set_error, ne_get_status, ne_add_request_header, ne_set_request_body_buffer, ne_set_request_flag.</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
