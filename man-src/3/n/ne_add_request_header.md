---
title: "ne_add_request_header(3)"
name: "ne_add_request_header"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_add_request_header/"
description: "ne_add_request_header, ne_print_request_header – add headers to a request"
---

<p>ne_add_request_header, ne_print_request_header &#8211; add headers to a request</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_request.h&gt;

void ne_add_request_header(ne_request *request, const char *name, const char *value);

void ne_print_request_header(ne_request *request, const char *name, const char *format, ...);</code></pre>
<h2>Description</h2>
<dd>The functions <code>ne_add_request_header</code> and <code>ne_print_request_header</code> can be used to add headers to a request, before it is sent. </p>
<p> <code>ne_add_request_header</code> simply adds a header of given <i>name</i>, with given <i>value</i>. </p>
<p> <code>ne_print_request_header</code> adds a header of given <i>name</i>, taking the value from the <code>printf</code>-like <i>format</i> string parameter and subsequent variable-length argument list.</p>
<h2>See Also</h2>
<p>ne_request_create</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
