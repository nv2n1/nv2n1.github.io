---
title: "rio_init_dbell_res(9)"
name: "rio_init_dbell_res"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_init_dbell_res/"
description: "rio_init_dbell_res – Initialize a RIO doorbell resource"
---

<p>rio_init_dbell_res &#8211; Initialize a RIO doorbell resource</p>
<h2>Synopsis</h2>
<pre><code>void rio_init_dbell_res(struct resource *res, u16 start, u16 end);</code></pre>
<h2>Arguments</h2>
<p><i>res</i></p>
<dl>
<dd>
<dd>resource struct</dl>
<p> <i>start</i></p>
<dl>
<dd>start of doorbell range</dl>
<p> <i>end</i></p>
<dl>
<dd>end of doorbell range</dl>
<h2>Description</h2>
<p>This function is used to initialize the fields of a resource for use as a doorbell resource. It initializes a range of doorbell messages using the start and end arguments.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
