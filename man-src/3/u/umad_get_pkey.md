---
title: "umad_get_pkey(3)"
name: "umad_get_pkey"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_get_pkey/"
description: "umad_get_pkey – get pkey index from umad buffer"
---

<p>umad_get_pkey &#8211; get pkey index from umad buffer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_get_pkey(void *umad);</code></pre>
<h2>Description</h2>
<p><code>umad_get_pkey()</code> gets the pkey index from the specified <i>umad</i> buffer.</p>
<h2>Return Value</h2>
<p><code>umad_get_pkey()</code> returns value of pkey index (or zero if pkey index is not supported by user_mad interface).</p>
<h2>Author</h2>
<dl>
<dt>Sasha Khapyorsky &lt;sashak [at] voltaire.com&gt;</p>
<dd></dl>
