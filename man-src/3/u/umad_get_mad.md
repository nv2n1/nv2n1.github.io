---
title: "umad_get_mad(3)"
name: "umad_get_mad"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_get_mad/"
description: "umad_get_mad – get the MAD pointer of a umad buffer"
---

<p>umad_get_mad &#8211; get the MAD pointer of a umad buffer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

void *umad_get_mad(void *umad);</code></pre>
<h2>Description</h2>
<p><code>umad_get_mad()</code> returns a pointer to the MAD contained within the <i>umad</i> buffer.</p>
<h2>Return Value</h2>
<p><code>umad_get_mad()</code> returns a pointer to the MAD contained within the supplied <i>umad</i> buffer.</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
