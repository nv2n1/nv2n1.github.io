---
title: "rio_query_mport(9)"
name: "rio_query_mport"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_query_mport/"
description: "rio_query_mport – Query mport device attributes"
---

<p>rio_query_mport &#8211; Query mport device attributes</p>
<h2>Synopsis</h2>
<pre><code>int rio_query_mport(struct rio_mport *port, struct rio_mport_attr *mport_attr);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>mport device to query</dl>
<p> <i>mport_attr</i></p>
<dl>
<dd>mport attributes data structure</dl>
<h2>Description</h2>
<p>Returns attributes of specified mport through the pointer to attributes data structure.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
