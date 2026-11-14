---
title: "umad_status(3)"
name: "umad_status"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_status/"
description: "umad_status – get the status of a umad buffer"
---

<p>umad_status &#8211; get the status of a umad buffer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_status(void *umad);</code></pre>
<h2>Description</h2>
<p><code>umad_status()</code> get the internal <i>umad</i> status field.</p>
<h2>Return Value</h2>
<p>After a packet is received, <code>umad_status()</code> returns 0 on a successful receive, or a non zero status. ETIMEDOUT means that the packet had a send-timeout indication. In this case, the transaction ID will be set to the TID of the original request.</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
