---
title: "rio_release_dev(9)"
name: "rio_release_dev"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_release_dev/"
description: "rio_release_dev – Frees a RIO device struct"
---

<p>rio_release_dev &#8211; Frees a RIO device struct</p>
<h2>Synopsis</h2>
<pre><code>void rio_release_dev(struct device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>LDM device associated with a RIO device struct</dl>
<h2>Description</h2>
<p>Gets the RIO device struct associated a RIO device struct. The RIO device struct is freed.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
