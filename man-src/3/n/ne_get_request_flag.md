---
title: "ne_get_request_flag(3)"
name: "ne_get_request_flag"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_get_request_flag/"
description: "ne_set_request_flag, ne_get_request_flag – set and retrieve per-request flags"
---

<p>ne_set_request_flag, ne_get_request_flag &#8211; set and retrieve per-request flags</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_request.h&gt;

void ne_set_request_flag(ne_request *req, ne_request_flag flag, int value);

int ne_get_request_flag(ne_request *req, ne_request_flag flag);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_set_request_flag</code> function enables or disables a per-request flag. Passing a non-zero <i>value</i> argument enables the flag, and zero disables it. </p>
<p> The following flags are defined: </p>
<p> <code>NE_REQFLAG_EXPECT100</code></p>
<dl>
<dd>enable this flag to use the &quot;Expect: 100-continue&quot; feature of HTTP/1.1, which allows the server to process request headers without reading the entire request body. This saves time and bandwidth if the server gives an authentication challenge (requiring the request to be resent), but has interoperability problems with some older servers.</dl>
<p> <code>NE_REQFLAG_IDEMPOTENT</code></p>
<dl>
<dd>disable this flag if the request uses a non-idempotent method such as POST</dl>
<h2>Return Value</h2>
<p>The <code>ne_get_request_flag</code> function returns zero if a flag is disabled, less than zero if the flag is not supported, or greater than zero if the flag is enabled.</p>
<h2>See Also</h2>
<p>ne_request_create.</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
