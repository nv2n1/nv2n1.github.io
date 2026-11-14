---
title: "rio_find_mport(9)"
name: "rio_find_mport"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_find_mport/"
description: "rio_find_mport – find RIO mport by its ID"
---

<p>rio_find_mport &#8211; find RIO mport by its ID</p>
<h2>Synopsis</h2>
<pre><code>struct rio_mport *rio_find_mport(int mport_id);</code></pre>
<h2>Arguments</h2>
<p><i>mport_id</i></p>
<dl>
<dd>
<dd>number (ID) of mport device</dl>
<h2>Description</h2>
<p>Given a RIO mport number, the desired mport is located in the global list of mports. If the mport is found, a pointer to its data structure is returned. If no mport is found, <code>NULL</code> is returned.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
