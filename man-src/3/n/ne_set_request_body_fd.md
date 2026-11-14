---
title: "ne_set_request_body_fd(3)"
name: "ne_set_request_body_fd"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_set_request_body_fd/"
description: "ne_set_request_body_buffer, ne_set_request_body_fd, ne_set_request_body_fd64 – include a message body with a request"
---

<p>ne_set_request_body_buffer, ne_set_request_body_fd, ne_set_request_body_fd64 &#8211; include a message body with a request</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_request.h&gt;

void ne_set_request_body_buffer(ne_request *req, const char *buf, size_t count);

int ne_set_request_body_fd(ne_request *req, int fd, off_t begin, off_t length);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_set_request_body_buffer</code> function specifies that a message body should be included with the body, which is stored in the <i>count</i> bytes buffer <i>buf</i>. </p>
<p> The <code>ne_set_request_body_fd</code> function can be used to include a message body with a request which is read from a file descriptor. The body is read from the file descriptor <i>fd</i>, which must be a associated with a seekable file (not a pipe, socket, or FIFO). <i>count</i> bytes are read, beginning at offset <i>begin</i> (hence, passing <i>begin</i> as zero means the body is read from the beginning of the file). </p>
<p> For all the above functions, the source of the request body must survive until the request has been dispatched; neither the memory buffer passed to <code>ne_set_request_body_buffer</code> nor the file descriptor passed to <code>ne_set_request_body_fd</code> are copied internally.</p>
<h2>See Also</h2>
<p>ne_request_create</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
