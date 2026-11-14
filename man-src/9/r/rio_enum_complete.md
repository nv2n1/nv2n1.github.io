---
title: "rio_enum_complete(9)"
name: "rio_enum_complete"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_enum_complete/"
description: "rio_enum_complete – Tests if enumeration of a network is complete"
---

<p>rio_enum_complete &#8211; Tests if enumeration of a network is complete</p>
<h2>Synopsis</h2>
<pre><code>int rio_enum_complete(struct rio_mport *port);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>Master port to send transaction</dl>
<h2>Description</h2>
<p>Tests the PGCCSR discovered bit for non-zero value (enumeration complete flag). Return <code>1</code> if enumeration is complete or <code>0</code> if enumeration is incomplete.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
