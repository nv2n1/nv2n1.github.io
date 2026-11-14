---
title: "umad_set_pkey(3)"
name: "umad_set_pkey"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_set_pkey/"
description: "umad_set_pkey – set pkey index within umad buffer"
---

<p>umad_set_pkey &#8211; set pkey index within umad buffer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_set_pkey(void *umad, int pkey_index);</code></pre>
<h2>Description</h2>
<p><code>umad_set_pkey()</code> sets the pkey index within the specified <i>umad</i> buffer.</p>
<h2>Return Value</h2>
<p><code>umad_set_pkey()</code> returns 0 on success, and a negative value on an error.</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
