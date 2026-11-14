---
title: "rio_alloc_net(9)"
name: "rio_alloc_net"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_alloc_net/"
description: "rio_alloc_net – Allocate and initialize a new RIO network data structure"
---

<p>rio_alloc_net &#8211; Allocate and initialize a new RIO network data structure</p>
<h2>Synopsis</h2>
<pre><code>struct rio_net *rio_alloc_net(struct rio_mport *mport);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>Master port associated with the RIO network</dl>
<h2>Description</h2>
<p>Allocates a RIO network structure, initializes per-network list heads, and adds the associated master port to the network list of associated master ports. Returns a RIO network pointer on success or <code>NULL</code> on failure.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
