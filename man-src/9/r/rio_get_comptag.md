---
title: "rio_get_comptag(9)"
name: "rio_get_comptag"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_get_comptag/"
description: "rio_get_comptag – Begin or continue searching for a RIO device by component tag"
---

<p>rio_get_comptag &#8211; Begin or continue searching for a RIO device by component tag</p>
<h2>Synopsis</h2>
<pre><code>struct rio_dev *rio_get_comptag(u32 comp_tag, struct rio_dev *from);</code></pre>
<h2>Arguments</h2>
<p><i>comp_tag</i></p>
<dl>
<dd>
<dd>RIO component tag to match</dl>
<p> <i>from</i></p>
<dl>
<dd>Previous RIO device found in search, or <code>NULL</code> for new search</dl>
<h2>Description</h2>
<p>Iterates through the list of known RIO devices. If a RIO device is found with a matching <i>comp_tag</i>, a pointer to its device structure is returned. Otherwise, <code>NULL</code> is returned. A new search is initiated by passing <code>NULL</code> to the <i>from</i> argument. Otherwise, if <i>from</i> is not <code>NULL</code>, searches continue from next device on the global list.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
