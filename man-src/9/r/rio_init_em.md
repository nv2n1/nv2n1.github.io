---
title: "rio_init_em(9)"
name: "rio_init_em"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_init_em/"
description: "rio_init_em – Initializes RIO Error Management (for switches)"
---

<p>rio_init_em &#8211; Initializes RIO Error Management (for switches)</p>
<h2>Synopsis</h2>
<pre><code>void rio_init_em(struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device</dl>
<h2>Description</h2>
<p>For each enumerated switch, call device-specific error management initialization routine (if supplied by the switch driver).</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
