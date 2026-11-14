---
title: "rio_destid_free(9)"
name: "rio_destid_free"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_destid_free/"
description: "rio_destid_free – free a previously allocated destID"
---

<p>rio_destid_free &#8211; free a previously allocated destID</p>
<h2>Synopsis</h2>
<pre><code>void rio_destid_free(struct rio_net *net, u16 destid);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>RIO network</dl>
<p> <i>destid</i></p>
<dl>
<dd>destID to free</dl>
<h2>Description</h2>
<p>Makes the specified destID available for use.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
